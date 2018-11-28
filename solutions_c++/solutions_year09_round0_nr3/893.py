#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
const int MOD=10000;
char S[550];
int L;
const char T[21]=" welcome to code jam";
int F[501][20];
void Solve()
{
     for (int i=0;i<=L;i++) F[i][0]=1;
     for (int i=1;i<=L;i++)
     {
         for (int j=1;j<=19;j++)
         {
             if (S[i]==T[j])
                F[i][j]=(F[i-1][j]+F[i-1][j-1])%MOD;
             else
                 F[i][j]=F[i-1][j];
            // printf("%d ",F[i][j]);
         }
         //printf("\n");
     }
}
int main()
{
    //freopen("a.txt","r",stdin);
    //freopen("b.txt","w",stdout);
    int N;
    scanf("%d",&N);
    gets(S+1);
    for (int i=1;i<=N;i++)
    {
        gets(S+1);
        L=strlen(S+1);
        Solve();
        printf("Case #%d: %.4d\n",i,F[L][19]);
    }
    return 0;
}
