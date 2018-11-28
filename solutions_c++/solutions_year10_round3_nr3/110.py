#include<iostream>
#include<cmath>
#include<string>
using namespace std;
const int Maxn=600;
int T,N,M,Map[Maxn][Maxn],dp[Maxn][Maxn];
int now;
int Ans[Maxn];
char ch[Maxn];
void work(int x){
     for (int i=0;i<M/4;i++){
         int now=ch[i]-'0';
         if (now<0 || now > 9)
         now=ch[i]-'A'+10;
         for (int j=4;j>0;j--){
             Map[x][i*4+j]=now & 1;
             now=now>>1;
         }
     }
}
int min(int a,int b,int c){
    if (a>b) a=b;
    if (a>c) a=c;
    return a;
}
void solve(){
     int Max=0;
     int ii,jj;
     for (int i=0;i<=N+1;i++)
     for (int j=0;j<=M+1;j++)
     dp[i][j]=0;
     for (int i=1;i<=N;i++)
     for (int j=1;j<=M;j++){
         if (Map[i][j]==-1){
            dp[i][j]=0;
            continue;
         }
         if (Map[i][j]==Map[i-1][j-1] && Map[i][j]+Map[i-1][j]==1 && Map[i][j]+Map[i][j-1]==1)
         dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1;else
         dp[i][j]=1;
         if (dp[i][j]>Max){
            Max=dp[i][j];
            ii=i;
            jj=j;
         }
     }
//     cout<<ii<<" "<<jj<<endl;
     Ans[Max]++;
     if (Ans[Max]==1) Ans[0]++;
     for (int i=ii-Max+1;i<=ii;i++)
     for (int j=jj-Max+1;j<=jj;j++)
     Map[i][j]=-1;
     now-=Max*Max;
}
int main(){
freopen("C.in","r",stdin);
freopen("C.out","w",stdout);
    scanf("%d", &T);
    int t=0;
    while (T--){
          for (int i=0;i<Maxn;i++) Ans[i]=0;
          scanf("%d%d\n", &N, &M);
          for (int i=1;i<=N;i++){
              gets(ch);
              work(i);
          }/*
          for (int i=1;i<=N;i++){
              for (int j=1;j<=M;j++){
                  cout<<Map[i][j];
              }
              cout<<endl;
          }*/
          now=N*M;
          while (now){
                
                solve();
/*                
                for (int i=1;i<=N;i++){
                    for (int j=1;j<=M;j++){
                        cout<<Map[i][j];
                    }     
                    cout<<endl;
                }
                */
          }
          printf("Case #%d: %d\n",++t,Ans[0]);
          for (int i=N;i>0;i--)
          if (Ans[i]>0) printf("%d %d\n",i,Ans[i]);
    }
    return 0;
}
