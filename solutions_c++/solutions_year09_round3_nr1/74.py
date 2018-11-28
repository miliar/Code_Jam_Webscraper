#include <stdio.h>
#include <string>

char s[100];
int T, C, p, i, j, k;
int a[100], b[300];
long long ans;

int main()
{
    freopen("a_in.txt", "r", stdin);
    freopen("a_out.txt", "w", stdout);
    scanf("%d ", &T);
    for (C=1; C<=T; C++)
    {
        scanf("%s", s);
        memset(a, 0, sizeof(a));
        for (i=0; s[i]!='\0'; i++) if (s[i]<='9') a[s[i] - '0'] ++; else a[s[i] - 'a' + 10] ++;
        p = 0;
        for (i=0; i<36; i++) if (a[i]) p ++;
        if (p<2) p = 2;
        memset(b, 0, sizeof(b));
        ans = 0;
        for (i=0; s[i]!='\0'; i++) if (b[s[i]]) ans = ans * p + b[s[i]] - 1; else
        {
            for (j=0; j<p; j++) if (a[j]>=0 && (i || j))
            {
                b[s[i]] = j + 1; a[j] = -1;
                ans = ans * p + j;
                break;
            }
        }
        printf("Case #%d: %I64d\n", C, ans);
    }
}

