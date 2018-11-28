#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

int     n, m;
int     a   [3000];
int     b   [3000];

void init()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i ++)
    {
        scanf("%d", a + i);        
        a[i] --;
    }
    for (int i = 0; i < m; i ++)
    {
        scanf("%d", b + i);        
        b[i] --;
    }
}

struct Edge
{
    int v;
    int u;
    bool mark;
    Edge* rev;
};

int top;
Edge    memo    [50000];

vector<Edge*> list    [3000];

void addEdge(int a, int b, bool oneway)
{
    Edge* t;
        
    t = &memo[top ++];
    t->v = a;
    t->u = b;
    list[a].push_back(t);
    t->rev = NULL;

    if (! oneway)
    {
        Edge* q;        
        q = &memo[top ++];
        q->v = b;
        q->u = a; 
        list[b].push_back(q);
        t->rev = q;
        q->rev = t;
    }
}

int nodecc;

inline int clockdist(int p, int r)
{
    if (r >= p) return r - p;
    else return r + n - p;
}

void visit(int i, int j, Edge* eij)
{
    //fprintf(stderr, "(%d -> %d)", i, j);
    eij->mark = 1;

    int v = -1;
    int mx = -1;
    Edge* ejv;

    nodecc ++;

    for (int p = 0; p < list[j].size(); p ++)
    {   
        int k = list[j][p]->u;
        if (clockdist(j, k) + clockdist(k, i) == clockdist(j, i) && k != i)
        {
            if (clockdist(j, k) > mx)
            {
                mx = clockdist(j, k);
                v = k;
                ejv = list[j][p];
            }
        }
    }

    if (! ejv->mark)
    {
        visit(j, v, ejv);
    }
}

int usep;
bool used    [5200];
int color[15200];

Edge* queue[10000];
int head, tail;

int ans;
int stcolor;
int prevcolor;

int getColor()
{
    while (used[usep]) usep ++;
    used[usep] = 1;

    if (usep < ans) return usep;
    while (usep % ans == stcolor || usep % ans == prevcolor)
    {
        used[ ++ usep] = 1;
    }
    return usep % ans;
}

void paint(int i, int j, Edge* eij)
{
    //fprintf(stderr, "(%d -> %d)", i, j);
    eij->mark = 1;

    if (eij->rev && ! eij->rev->mark)
    {
        queue[++ tail] = eij->rev;
    }

    int v = -1;
    int mx = -1;
    Edge* ejv;

    nodecc ++;

    for (int p = 0; p < list[j].size(); p ++)
    {   
        int k = list[j][p]->u;
        if (clockdist(j, k) + clockdist(k, i) == clockdist(j, i) && k != i)
        {
            if (clockdist(j, k) > mx)
            {
                mx = clockdist(j, k);
                v = k;
                ejv = list[j][p];
            }
        }
    }

    prevcolor = color[j];
    if (color[v] < 0)
        color[v] = getColor();

    if (! ejv->mark)
    {
        paint(j, v, ejv);        
    }
}

void chkvisit(int i, int j, Edge* eij)
{
    used[ color[i] ] = used[ color[j] ] = 1;
    //fprintf(stderr, "(%d -> %d)", i, j);
    eij->mark = 1;

    int v = -1;
    int mx = -1;
    Edge* ejv;

    nodecc ++;

    for (int p = 0; p < list[j].size(); p ++)
    {   
        int k = list[j][p]->u;
        if (clockdist(j, k) + clockdist(k, i) == clockdist(j, i) && k != i)
        {
            if (clockdist(j, k) > mx)
            {
                mx = clockdist(j, k);
                v = k;
                ejv = list[j][p];
            }
        }
    }

    if (! ejv->mark)
    {
        chkvisit(j, v, ejv);
    }
}


void run_check()
{
    for (int i = 0; i < top; i ++)
        memo[i].mark = 0;

    for (int i = 0; i < n; i ++)
    {
        for (int j = 0; j < list[i].size(); j ++)
            if (! list[i][j]->mark)
            {
                memset(used, 0, sizeof(used));
                chkvisit(i, list[i][j]->u, list[i][j]);
                //fprintf(stderr, "\n");
                for (int c = 0; c < ans; c ++)
                    if (! used[c])
                    {
                        puts("SHIT");
                        fprintf(stderr, "SHIT!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
                        while(1){}
                    }
            }
    }
}

void solve()
{
    //fprintf(stderr, "%d\n", clockdist(1,0));

    top = 0;

    for (int i = 0; i < n; i ++)
        list[i].clear();
    for (int i = 0; i < n; i ++)
        addEdge(i, (i + 1) % n, 1);
    for (int i = 0; i < m; i ++)
        addEdge(a[i], b[i], 0);

    for (int i = 0; i < top; i ++)
        memo[i].mark = 0;

    ans = n;
    Edge* ste;
    int sti, stj;
    

    for (int i = 0; i < n; i ++)
    {
        for (int j = 0; j < list[i].size(); j ++)
            if (! list[i][j]->mark)
            {
                nodecc = 0;
                visit(i, list[i][j]->u, list[i][j]);
                //fprintf(stderr, "\n");
                if (nodecc < ans)
                {
                    ans = nodecc;
                    sti = i;
                    stj = list[i][j]->u;
                    ste = list[i][j];
                }
            }
    }
    printf("%d\n", ans);

    for (int i = 0; i < top; i ++)
        memo[i].mark = 0;

    memset(color, 0xff, sizeof(color));
    memset(used, 0, sizeof(used));
 
    color[sti] = 0;
    color[stj] = 1;
    used[0] = used[1] = 1;
    usep = 2;

    head = 0; tail = -1;
    paint(sti, stj, ste);
    //fprintf(stderr, "\n");
    while (head <= tail)
    {
        memset(used, 0, sizeof(used));
        usep = 0;
        used[color[queue[head]->v]] = 1;
        used[color[queue[head]->u]] = 1;
        stcolor = color[queue[head]->v];
        paint(queue[head]->v, queue[head]->u, queue[head]);
        //fprintf(stderr, "\n");
        head ++;
    }

    for (int i = 0; i < n; i ++)
    {
        if (i) printf(" ");
        printf("%d", color[i] + 1);
    }
    printf("\n");

    run_check();
}

void clear()
{
    memset(a, 0, sizeof(a));
    memset(b, 0, sizeof(b));
    memset(memo, 0, sizeof(memo));
    memset(used, 0, sizeof(used));
}

int main()
{
    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("C-small-at1.out", "w", stdout);

    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    //freopen("in.txt", "r", stdin);

    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t ++)
    {
        clear();
        init();
        
        printf("Case #%d: " , t);
        fprintf(stderr, "Case #%d: " , t);

        solve();
    }

    return 0;
}