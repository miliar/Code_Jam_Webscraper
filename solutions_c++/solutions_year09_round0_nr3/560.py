#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
using namespace std;
const string s0="welcome to code jam";
const int LIMIT=10000;
int t;
long i,j,k,h,sum;
string s;
long f[550],f2[550];
main(){
  freopen("welcome.in","r",stdin);
  freopen("welcome.out","w",stdout);
  getline(cin,s);
  t=atoi(s.c_str());
  for(i=1;i<=t;++i){ //BEGIN A TEST CASE
    getline(cin,s);
    memset(f,0,sizeof(f));
    memset(f2,0,sizeof(f2));
    for(j=0;j<s.length();++j) {
      if(s[j]=='w') f2[j]=1; else f2[j]=0;
    }
    for(j=1;j<s0.length();++j){
      sum=0;
      for(k=0;k<s.length();++k){
        if (s[k]==s0[j]) f[k]=sum;
        else f[k]=0;
        sum+=f2[k];
        if (sum>LIMIT) sum%=10000;
      }
      for(k=0;k<s.length();++k){
        f2[k]=f[k];
      }
    }
    sum=0;
    for(k=0;k<s.length();++k) sum+=f[k];
    sum%=10000;
    cout<<"Case #"<<i<<": "<<setw(4)<<setfill('0')<<sum<<endl;    
  }
}
