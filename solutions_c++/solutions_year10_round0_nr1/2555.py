#include<iostream>
#include<fstream>
#define cin fin
#define cout fout
using namespace std;
int main()
{
   ifstream fin("A-large.in");
   ofstream fout("A-large-out.out");
   int t;
   cin>>t;
   int dp[40];
   dp[1]=1;
   for(int i=2;i<=30;i++)
      dp[i]=2*dp[i-1]+1;     
   for(int count=1;count<=t;count++)
   {
      int n,k;
      cin>>n>>k;
      cout<<"Case #"<<count<<": ";
      if(k%(dp[n]+1)==dp[n])cout<<"ON"<<endl;
      else cout<<"OFF"<<endl;
   }
   system("pause");
   return 0;
}
      
