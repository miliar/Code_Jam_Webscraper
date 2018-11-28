#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;
ifstream cin("A.in");
ofstream cout("A.out");
char ordR[110];
int N,ordnum[110],M;
int dp[110][110][110];
vector<int> O,B;
int exc(int ord,int Opos,int Bpos)
{
    if(ord==N)return 0;
    if(Bpos>M||Opos>M||Bpos<=0||Opos<=0)return 1<<30;
    if(dp[ord][Opos][Bpos]!=-1)return dp[ord][Opos][Bpos];
    if(ordR[ord]=='O')
    {
         if(ordnum[ord]==Opos)
         {
             int x1,x2,x3;
             x1=exc(ord+1,Opos,Bpos)+1;
             x2=exc(ord+1,Opos,Bpos+1)+1;
             x3=exc(ord+1,Opos,Bpos-1)+1;
             return dp[ord][Opos][Bpos]=min(min(x1,x2),x3);
         }
         if(Opos<ordnum[ord])
         {
             int x1,x2,x3;
             x1=exc(ord,Opos+1,Bpos)+1;
             x2=exc(ord,Opos+1,Bpos+1)+1;
             x3=exc(ord,Opos+1,Bpos-1)+1;
             return dp[ord][Opos][Bpos]=min(min(x1,x2),x3);
         }
         if(Opos>ordnum[ord])
         {
             int x1,x2,x3;
             x1=exc(ord,Opos-1,Bpos)+1;
             x2=exc(ord,Opos-1,Bpos+1)+1;
             x3=exc(ord,Opos-1,Bpos-1)+1;
             return dp[ord][Opos][Bpos]=min(min(x1,x2),x3);
         }
    }
    if(ordR[ord]=='B')
    {
         if(ordnum[ord]==Bpos)
         {
             int x1,x2,x3;
             x1=exc(ord+1,Opos,Bpos)+1;
             x2=exc(ord+1,Opos+1,Bpos)+1;
             x3=exc(ord+1,Opos-1,Bpos)+1;
             return dp[ord][Opos][Bpos]=min(min(x1,x2),x3);
         }
         if(Bpos<ordnum[ord])
         {
             int x1,x2,x3;
             x1=exc(ord,Opos,Bpos+1)+1;
             x2=exc(ord,Opos+1,Bpos+1)+1;
             x3=exc(ord,Opos-1,Bpos+1)+1;
             return dp[ord][Opos][Bpos]=min(min(x1,x2),x3);
         }
         if(Bpos>ordnum[ord])
         {
             int x1,x2,x3;
             x1=exc(ord,Opos,Bpos-1)+1;
             x2=exc(ord,Opos+1,Bpos-1)+1;
             x3=exc(ord,Opos-1,Bpos-1)+1;
             return dp[ord][Opos][Bpos]=min(min(x1,x2),x3);
         }
    }
}
int main()
{
    int T;
    cin>>T;
    for(int k=1;k<=T;k++)
    {
       cin>>N;
       M=0;
       for(int i=0;i<N;i++)
       {
           cin>>ordR[i];
           cin>>ordnum[i];
           M=max(M,ordnum[i]);
           if(ordR[i]=='O')O.push_back(ordnum[i]);
           if(ordR[i]=='B')B.push_back(ordnum[i]);
       }
       memset(dp,-1,sizeof(dp));
       cout<<"Case #"<<k<<": "<<exc(0,1,1)<<endl;
    }
    return 0;
}
