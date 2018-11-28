#include<iostream>
#include<string>
#include<vector>
#include<string>
#include<map>
using namespace std;
#define CLR(x,y) memset(x,y,sizeof(x))
#define INF 100000000
int dp[1001][110];
int s,q;
map< string,int > mp;
int que[1001];
int main()
{
    int i,j,k,t,cases;
    string st;
    freopen("A-large.in","r",stdin);
    FILE* fs=fopen("A-large.out","w+");
    while(scanf("%d",&t)!=EOF)
    {
          cases=1;
          while(t--)
          {
               scanf("%d\n",&s);
               mp.clear();
               for(i=0;i<s;i++)
               {
                   getline(cin,st); 
                   mp.insert(make_pair(st,i));
               }
               scanf("%d\n",&q);
               for(i=0;i<q;i++)
               {
                   getline(cin,st);
                   que[i]=(mp.find(st))->second;                
               }
               CLR(dp,0);
               dp[0][que[0]]=INF;
               for(i=1;i<q;i++)
               {
                   for(j=0;j<s;j++)
                   {    
                       dp[i][j]=INF;
                       if(que[i]==j) continue;
                       dp[i][j]=min(dp[i][j],dp[i-1][j]);
                   }
                   for(k=0;k<s;k++)
                       {
                           if(que[i]==k) continue;
                           else dp[i][k]=min(dp[i][k],dp[i-1][que[i]]+1);
                       }
               }
               int res=INF;
               for(i=0;i<s;i++)
                   if(res>dp[q-1][i]) res=dp[q-1][i];
               fprintf(fs,"Case #%d: %d\n",cases++,res);
          }                          
    }
    system("pause");
    return 0;
}
