#include <stdio.h>
#include <string.h>

int n, len, i, j, k;
char ss[600];
char line[] = "welcome to code jam";
int d[600][600];

int main()
{
    int nline = strlen(line);
    
    freopen("C-2.in", "r", stdin);
    freopen("C-2.out", "w", stdout);  
    
    scanf("%d", &n);
    gets(ss);
    for (int icase=0; icase<n; ++icase) {
        gets(ss);
        len = strlen(ss);
        // deal
        memset(d, 0, sizeof(d));
        // init
        for (i=0; i<len; ++i)
            if (ss[i] == line[0]) 
                d[i][0] = 1;
        for (i=1; i<nline; ++i) {
            for (j=0; j<len; ++j) 
                if (ss[j] == line[i]) {
                    int cnt = 0;
                    for (k=0; k<j; ++k) 
                        cnt += d[k][i-1];
                    cnt %= 10000;
                    d[j][i] = cnt;
                }    
        }   
        int ans = 0;      
        for (i=0; i<len; ++i) {
            ans += d[i][nline-1];
            ans %= 10000;
        }    
        printf("Case #%d: %04d\n", icase+1, ans);
    
    }        
    
    return 0;
}    

