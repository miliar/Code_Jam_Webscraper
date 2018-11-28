#include <cstdio>
#include <cstring>

struct tree {
    double val;
    bool flag;
    char fea[12];
    tree *l, *r;
};

tree *h;
int m, Case = 1;
int n, k;
char name[12], nfea[110][12];
    
void get(tree *&s)
{
    char ch, tmp[12];
    s = new tree;
    for (ch = getchar(); ch != '('; ch = getchar());
    scanf ("%lf", &s -> val);
    //printf ("Go : %lf\n", s -> val);
    for (ch = getchar(); ch == ' '; ch = getchar());
    if (ch == ')') {
        s -> flag = false;
        s -> l = s -> r = NULL;
        return ;
    }
    int cnt = 0;
    s -> fea[cnt++] = ch;
    while (ch = getchar()) {
        if (ch == ' ' || ch == '\n')
            break;
        s -> fea[cnt++] = ch;
    }
    s -> fea[cnt] = '\0';
    //printf ("s -> fea : %s\n", s -> fea);
    s -> flag = true;
    get(s -> l);
    get(s -> r);
    for (ch = getchar(); ch != ')'; ch = getchar());
}

void free(tree *&s)
{
    if (s == NULL)
        return ;
    if (s -> flag) {
        free(s -> l);
        free(s -> r);
    }
    delete s;
}

double cal(tree *s)
{
    if (s == NULL)
        return 1.0;
    double res = s -> val;
    //printf ("--%lf\n", res);
    if (!s -> flag)
        return res;
    for (int i = 0; i < k; ++i) {
        //printf ("%s %s\n", s -> fea, nfea[i]);
        if (strcmp(s -> fea, nfea[i]) == 0)
            return res * cal(s -> l);
    }
    return res * cal(s -> r);
}

void init()
{
    scanf ("%d", &m);
    getchar();
    get(h);
}

void solve()
{
    scanf ("%d", &n);
    printf ("Case #%d:\n", Case++);
    
    while (n--) {
        scanf ("%s", name);
        scanf ("%d", &k);
        for (int i = 0; i < k; ++i)
            scanf ("%s", nfea[i]);
        printf ("%.7lf\n", cal(h));
    }
}

int main()
{
    int t;
    freopen ("A-large.in", "r", stdin);
    freopen ("out.txt", "w", stdout);
    
    scanf ("%d", &t);
    while (t--) {
        init();
        solve();
        free(h);
    }
    
    //while (1);
    
    return 0;
}
