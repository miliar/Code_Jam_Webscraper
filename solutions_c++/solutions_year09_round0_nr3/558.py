#include <cstdio>
#include <cstring>

#define  MAX 501
int f[MAX][20];
int main()
{
    int n;
    char s[MAX],t[]="welcome to code jam";
    memset(f,0,sizeof(f));
    for(int i = 0; i<MAX;i++){
        f[i][0] = 1;
    }
    scanf("%d\n",&n);
    for(int T=1;T<=n;T++){
        gets(s);
        int len = strlen(s);
        for(int i=1;i<=len;i++){
            for(int j=1;j<=19;j++){
                if(s[i-1] == t[j-1]){
                    f[i][j] = (f[i-1][j-1] + f[i-1][j])%10000;
                }
                else {
                    f[i][j] = f[i-1][j];
                }
            }
        }
        printf("Case #%d: %04d\n",T,f[len][19]);
    }
}