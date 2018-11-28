#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
using namespace std;
ifstream fin("C.in");
ofstream fout("C.out");
string base="welcome to code jam",txt;
int dp[25][515];
int rec(int ind,int txi)
{
   if(ind==base.size())return 1;
   if(txi==txt.size())return 0;
   if(dp[ind][txi]!=-1)return dp[ind][txi];
   int n=0;
   for(int i=txi;i<txt.size();i++)
   {
      if(txt[i]==base[ind])
      n+=rec(ind+1,i+1);
   }
   return dp[ind][txi]=n;
}
int main()
{
    int N;
    fin>>N;
    getline(fin,txt);
    for(int k=0;k<N;k++)
    {
       fout<<"Case #"<<k+1<<": ";
       memset(dp,-1,sizeof(dp));
       txt="";
       getline(fin,txt);
       int res=0;
       res=rec(0,0);
       if(res<1000)fout<<0;
       if(res<100)fout<<0;
       if(res<10)fout<<0;
       fout<<res<<endl;
    }
}
