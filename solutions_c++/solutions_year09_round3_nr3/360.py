#include<fstream>
#include<algorithm>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<stdio.h>
using namespace std;
ifstream fin("C.in");
ofstream fout("C.out");
ofstream f2out("C2.out");
int dp[10010][10010],P,Q,val[110];
int brib(int st,int en)
{
    if(dp[st][en]!=-1)return dp[st][en];
    int res=9999999,done=0;
    for(int i=0;i<Q;i++)
    {
         if(val[i]>=st&&val[i]<=en)
         {
             res=min(res,brib(st,val[i]-1)+brib(val[i]+1,en)+(val[i]-st)+(en-val[i]));
             done=1;
         }
    }
    if(!done)
    return dp[st][en]=0;
    return dp[st][en]=res;
}
int main()
{
    int T;
    fin>>T;
    memset(dp,-1,sizeof(dp));
    for(int k=0;k<T;k++)
    {
       fin>>P>>Q;
       f2out<<"Case #"<<k+1<<": "<<P<<" "<<Q<<endl;
       for(int i=0;i<Q;i++)
       fin>>val[i];
       fout<<"Case #"<<k+1<<": "<<brib(1,P)<<endl;
       for(int i=0;i<=P;i++)
       for(int j=0;j<=P;j++)
       dp[i][j]=-1;
    }
    return 0;
}
