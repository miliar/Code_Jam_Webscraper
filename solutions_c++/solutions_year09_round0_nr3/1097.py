#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#define MAXN 510
#define MOD 10000
#define L 19
using namespace std;
int f[MAXN][L];
int ntest;
char tam[MAXN];
string p;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.ou","w",stdout);
    
    scanf("%d\n",&ntest);
    p="welcome to code jam";
    reverse(p.begin(),p.end());
    for (int test=1; test<=ntest; test++)
    {
        gets(tam);
        int lim=strlen(tam);
        memset(f,0,sizeof(f));
        f[lim][0]=1;
        for (int i=lim-1; i>=0; i--)
        {
            f[i][0]=1;
            for (int j=1; j<=L; j++)
            {
                f[i][j]=f[i+1][j];
                if (tam[i]==p[j-1])
                {
                   f[i][j]+=f[i+1][j-1];
                   if (f[i][j]>=MOD)
                      f[i][j]-=MOD;
                }
            }
        }
        printf("Case #%d: ",test);
        if (f[0][L]==0)
           printf("0000\n");
        else 
        {
            for (int i=1; i<=3-int(log10(f[0][L])); i++)
                printf("0");
            printf("%d\n",f[0][L]);
        }
    }
    
    return 0;
}
