#include <stdio.h>
#include <string.h>

long long v[50];
int n, i, len, j;
char ss[50];
long long ans, tmp;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int kases=1, kase;
    scanf("%d", &kase);
    while(kase--) {
        memset(v, 0, sizeof(v));
        scanf("%d", &n);
        for (i=0; i<n; ++i) {
            scanf("%s", ss);
            tmp = 0;
            len = strlen(ss);
            for (j=len-1; j>=0; --j)
                tmp = (tmp<<1)+(ss[j]-'0');
            v[i] = tmp;

        }
        ans = 0;
        long long bak;
        tmp = 1;
        for (i=0; i<n; ++i) {
            for (j=i; j<n; ++j)
                if (v[j]<=tmp)
                    break;
            bak = v[j];
            while (j > i) {
                v[j] = v[j-1];
                ans++, j--;
            }
            v[i] = bak;
            tmp = (tmp<<1)+1;
        }
        printf("Case #%d: %lld\n", kases++, ans);
    }
    return 0;
}
