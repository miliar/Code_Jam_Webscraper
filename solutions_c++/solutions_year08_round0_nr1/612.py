#include <iostream>
#include <string>

#define REP(i,n) for (int i=1,_n=(n);i<=_n;i++)

using namespace std;

const int maxn=1000+10; const int maxm=10000+10; const int maxint=2100000000;

int F[maxn][maxm];

string S[maxn];

string T[maxm];

int n,m;

int K;

inline void Init()
{
       scanf("%d",&n);
       getline(cin,S[0]);
       REP(i,n)
       {
          getline(cin,S[i]);
       }
       scanf("%d",&m);
       getline(cin,T[0]);
       REP(i,m)
       {
          getline(cin,T[i]);
       }
       
}

inline void work()
{
       memset(F,-1,sizeof(F));
       memset(F[0],0,sizeof(F[0]));
       for (int i=1;i<=m;i++)
           for (int j=1;j<=n;j++)
           {
               //if (T[i]==S[j]) {F[i][j]=-1; continue;}
               if (T[i]!=S[j] && F[i-1][j]!=-1 && (F[i][j]==-1 || F[i][j]>F[i-1][j]))
               {
                  F[i][j]=F[i-1][j];
               }
               REP(k,n)
               if (k!=j)
               {
                   if (F[i-1][k]!=-1 && (F[i][j]==-1 || F[i][j]>F[i-1][k]+1))
                   {
                      F[i][j]=F[i-1][k]+1;
                   }
               }
           }
           
      int mini=maxint;
      REP(i,n) if (F[m][i]!=-1) {mini=min(mini,F[m][i]);}
      printf("Case #%d: %d\n",K,mini);
}

int main()
{
    freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
    int t; scanf("%d",&t);
    for (K=1;K<=t;K++)
    {
        Init();
        work();
    }
    return 0;
}
