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
    int ncase, icase;
    scanf("%d", &ncase);
    for (icase=0; icase<ncase; ++icase) {
        memset(v, 0, sizeof(v));
        scanf("%d", &n);
        for (i=0; i<n; ++i) {
            scanf("%s", ss);
            tmp = 0;
            len = strlen(ss);
            for (j=len-1; j>=0; --j)
                tmp = (tmp<<1)+(ss[j]-'0');
            v[i] = tmp;
            //printf("get value:%lld \n", v[i]);
        }    
        
        //long long ans = msort(v, 0, n-1);
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
            /*
            printf("after swap:\n");
            for (j=0; j<n; ++j)
                printf("%lld ", v[j]);
            printf("\n"); */
            tmp = (tmp<<1)+1;
        }    
        printf("Case #%d: %lld\n", icase+1, ans);
    }    
   // system("pause");
    return 0;
}    
/*
2
10
11
3
001
100
010
4
1110
1100
1100
1000
*/
