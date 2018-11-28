#include<algorithm>
#include<iostream>
#include<iomanip>
#include<string>
#include<vector>
#include<cmath>
using namespace std;

struct poly
{
    int a , b , f;
    poly(){a = 0 , b = 0 , f = 0 , pair = 0;}
    poly(int _a , int _b , int _f){a = _a , b = _b , pair = 0 , f = _f;}
    poly* pair;
}P[10001];

int z , zf , root;
int s[10001]; // father , size
int n , m , nodeA[10001] , nodeB[10001];
vector <int> from[10001];
vector <int> edge[10001];
vector <int> node[10001];
int color[10001];
bool v[10001];
int ans;

int d(int a , int b)
{
    if(b > a)
        return b - a;
    b += n;
    return b - a;
}

int getf(int w)
{
    if(P[w].f == w)
        return w;
    P[w].f = getf(P[w].f);
    return P[w].f;
}

void Union(int a , int b)
{
    int fa = getf(a);
    int fb = getf(b);
    if(fa != fb)
        P[fa].f = fb;
}

int other(int c1 , int c2)
{
    int c = 0;
    while(c == c1 || c == c2)
        c ++;
    return c;
}

void dfs(int cur)
{
    v[cur] = true;
    int from = node[cur][0];
    int used1 = -1 , used2 = -1;
    for(int i = 0 ; i < node[cur].size() ; i++)
    {
        int w = node[cur][i];
        if(color[w] >= 0)
        {
            if(used1 == -1)
                used1 = color[w];
            else
                used2 = color[w];
        }
    }
    int want = 0;
    for(int i = 0 ; i < node[cur].size() ; i++)
        if(color[node[cur][i]] == -1)
        {
            want = want + 1;
            want %= ans;
            while(want == used1 || want == used2)
                want = (want + 1) % ans;
            color[node[cur][i]] = want;
        }

    for(int i = 0 ; i < node[cur].size() - 1 ; i++)
    if(color[node[cur][i]] == color[node[cur][i+1]])
    {
        
        int another;
        if(i == 0)
            another = color[node[cur][node[cur].size() - 1]];
        else
            another = color[node[cur][i-1]];
            color[node[cur][i]] = other(color[node[cur][i]] , another);
    }
    if(color[node[cur][0]] == color[node[cur][node[cur].size() - 1]])
    {
        color[node[cur][0]] = other(color[node[cur][node[cur].size() - 1]] , color[node[cur][1]]);
    }
    
    
    for(int i = 0 ; i < edge[cur].size() ; i++)
    {
        int to = edge[cur][i];
        if(!v[to])
            dfs(to);
    }
}

int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    ios :: sync_with_stdio(false);
    int TestCase;
    cin >> TestCase;
    
    for(int CaseID = 1 ; CaseID <= TestCase ; CaseID ++)
    {
        int minsize = 1000000;
        z = 0 , zf = 0;
        cin >> n >> m;
        for(int i = 1 ; i < n ; i++)
            P[++z] = poly(i , i + 1 , ++zf);
        P[++z] = poly(n , 1 , ++zf);
        for(int i = 1 ; i <= m ; i++)
            cin >> nodeA[i];
        for(int i = 1 ; i <= m ; i++)
            cin >> nodeB[i];
        for(int i = 1 ; i <= m ; i++)
        {
            P[++z] = poly(nodeA[i] , nodeB[i] , ++zf);
            P[++z] = poly(nodeB[i] , nodeA[i] , ++zf);
            P[z].pair = &P[z-1];
            P[z-1].pair = &P[z];
        }
        for(int i = 1 ; i <= n ; i++)
            from[i].clear();
        for(int i = 1 ; i <= z ; i++)
            from[P[i].a].push_back(i);
        for(int i = 1 ; i <= z ; i++)
            P[i].f = i;
        for(int i = 1 ; i <= z ; i++)
        {
            int which = 0 , maxd = 0;
            for(int j = 0 ; j < from[P[i].b].size() ; j++)
            {
                int e = from[P[i].b][j];
                int to = P[e].b;
                if(to == P[i].a)
                    continue;
                int dist1 = d(P[i].a , P[i].b);
                int dist2 = d(P[i].a , to);
                if(dist1 < dist2)
                {
                    if(dist2 > maxd)
                    {
                        maxd = dist2;
                        which = e;
                    }
                }
            }
            Union(i , which);
        }
        for(int i = 1 ; i <= z ; i++)
            edge[i].clear() , node[i].clear();
        for(int i = 1 ; i <= z ; i++)
            if(P[i].f == i)
            {
                int size = 0;
                for(int j = 1 ; j <= z ; j++)
                    if(P[j].f == i)
                    {
                        size ++;
                        if(P[j].pair)
                        edge[i].push_back((P[j].pair)->f);
                        node[i].push_back(P[j].a);
                    }
                if(size < minsize)
                    minsize = size , root = i;
                sort(node[i].begin() , node[i].end());
            }
        ans = minsize;
        memset(color , 0xff , sizeof(color));
        memset(v , 0 , sizeof(v));
        dfs(root);
        cout << "Case #" << CaseID << ": " << ans << endl ;
        for(int i = 1 ; i <= n ; i++)
        {
            cout << color[i] + 1;
            if(i == n)
                cout << endl;
            else
                cout << " ";
        }
    }
    return 0;
}
