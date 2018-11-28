#include <cstdio>

#define N 100001
#define L 100000

int n, m, l, nodes, cnt;
int child[N][26] = {0};
int f[N] = {0};
char str[L];
int a[30];
char s[30][26];

void insert(char s[])
{
    int i, k, now = 1;
    for (i = 0; s[i]; ++i)
    {
        k = s[i] - 'a';
        if (child[now][k] == 0)
            child[now][k] = ++nodes;
        now = child[now][k];
    }
    ++f[now];
}

void query(int k, int now)
{
    if (k == l)
    {
        cnt += f[now];
        return;
    }
    int i, j;
    for (i = 0; i < a[k]; ++i)
    {
        j = s[k][i] - 'a';
        if (child[now][j])
            query(k + 1, child[now][j]);
    }
}

void work(int no)
{
    int i, len = 0, k;
    for (i = 0; str[i]; ++i)
    {
        if (str[i] == '(')
        {
            for (++i, k = 0; str[i] != ')'; ++i, ++k)
                s[len][k] = str[i];
            a[len] = k;
            ++len;
        }
        else
        {
            s[len][0] = str[i];
            a[len] = 1;
            ++len;
        }
    }
    cnt = 0;
    query(0, 1);
    printf("Case #%d: %d\n", no, cnt);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int i;
    scanf("%d %d %d", &l, &n, &m);
    nodes = 1;
    while (n--)
    {
        scanf("%s", str);
        insert(str);
    }
    for (i = 1; i <= m; ++i)
    {
        scanf("%s", str);
        work(i);
    }
    return 0;
}
