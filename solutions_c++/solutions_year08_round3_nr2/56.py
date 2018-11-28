#include <iostream>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

typedef long long T;

T values[100];
int L;

T dp[100][210];


T doit(int R)
{
   memset(dp,0,sizeof(dp));
   values[0]=0;
   dp[0][0]=1;
   for(int i=1;i<=L;i++) {
      T rem=0;
      T mul=1;
      for(int j=i;j>=1;j--) {
         rem=(rem+values[j]*mul)%R;
         for(int r=0;r<R;r++) {
            T nr = (r+rem)%R;
            dp[i][nr]+=dp[j-1][r];
            nr = (r-rem+R)%R;
            if(j>1)
            dp[i][nr]+=dp[j-1][r];

         }
         mul=(mul*10)%R;
      }
   }
   return dp[L][0];
}

T gcd(T a, T b)
{
   if(b==0) return a;
   return gcd(b,a%b);
}

T lcm(T a, T b)
{
   return (a*b)/gcd(a,b);
   
}
int getLen(int state)
{
      int ret=0;
      while(state) {
         ret+=state%2;
         state/=2;
      }   
      return ret;
}

T solve()
{
   vector<int> vt;vt.push_back(2);vt.push_back(3);vt.push_back(5);vt.push_back(7);
   
   
   T ret=0;
   for(int state=1;state<(1<<4);state++) {
      int len=getLen(state);
      T mul=-1;
      if(len%2)mul=1;
      T curLcm=1;
      for(int i=0;i<4;i++) {
         if(state&(1<<i)) {
            curLcm=lcm(curLcm,vt[i]);
         }
      }
      
      
      
      T cur=doit(curLcm)*mul;
      
      
      ret+=cur;        
   }
   
   return ret;
}

int main()
{
   freopen("C:\\Downloads\\B-large.in","r",stdin);
   freopen("test.out","w",stdout);
   int N;
   cin>>N;
   for(int tc=1;tc<=N;tc++) {
      
      string str;cin>>str;
      L=str.size();
      for(int i=0;i<L;i++) values[i+1]=str[i]-'0';
      
      cout<<"Case #"<<tc<<": ";
      T ret = solve();
      cout<<ret<<endl;
   }
   return 0;
}
