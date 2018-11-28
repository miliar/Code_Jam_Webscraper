#include <stdio.h>
#include <string>

using namespace std;

char s1[600];
string s2;
int T, C, i, j, k, l1, l2, ans;
int a[510][30];

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.ans", "w", stdout);
    s2 = "welcome to code jam"; l2 = 19;
    scanf("%d ", &T);
    for (C=1; C<=T; C++)
    {
        gets(s1); l1 = strlen(s1); ans = 0;
        for (i=0; i<l1; i++) for (j=0; j<l2; j++) if (s1[i]!=s2[j]) a[i][j] = 0; else
        {
            if (j==0) { a[i][j] = 1; continue; }
            a[i][j] = 0;
            for (k=0; k<i; k++) a[i][j] += a[k][j - 1];
            a[i][j] %= 10000;
            if (j==l2-1) ans = (ans + a[i][j]) % 10000;
        }
        printf("Case #%d: %04d\n", C, ans);
    }
}

