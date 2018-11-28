#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int a[150], b[150];
int m, T, len;
long long n, two[64];
bool q;
char s[150];

void dfs(int k, long long n)
{
     long long t = (int)sqrt(n);
     if (t * t == n)
     {
           q = true;
           return;
     }
     for (int i = k; i < m; i++)
     {
         b[a[i]] = 1;
         dfs(i + 1, n + two[len - 1 - a[i]]);
         if (q) return;
         b[a[i]] = 0;
     }
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    scanf("%d\n", &T);
    two[0] = 1;
    for (int i = 1; i < 64; i++)
        two[i] = two[i - 1] * 2;
    for (int cas = 1; cas <= T; cas++)
    {
        printf("Case #%d: ", cas);
        gets(s);
        len = strlen(s);
        m = n = 0;
        for (int i = 0; i < len; i++)
        {
            b[i] = 0;
            if (s[i] == '1') b[i] = 1;
            else if (s[i] == '?') a[m++] = i;
            n = (n << 1) + b[i];
        }
        q = false;
        dfs(0, n);
        for (int i = 0; i < len; i++)
            printf("%d", b[i]);
        printf("\n");
    }
    return 0;
}
