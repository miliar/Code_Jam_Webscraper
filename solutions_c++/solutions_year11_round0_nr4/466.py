#include<iostream>
using namespace std;

int main(){
  int t;
  cin>>t;
  double f[1001],res[1001];
  f[0]=1;
  for(int i=1;i<=1000;i++)
    f[i]=f[i-1]/i;
  res[0]=res[1]=0;
  for(int i=2;i<=1000;i++){
    res[i]=0;
    double p=0;
    int sig=-1;
    for(int j=2;j<i;j++)
      res[i]+=res[j]*f[i-j]*(p+=f[j]*(sig=-sig));
    res[i]+=1;
    res[i]/=(1-p-f[i]*-sig);
  }
  cout.setf(ios_base::fixed);
  cout.precision(6);
  for(int i=1;i<=t;i++){
    int n;
    cin>>n;
    int s[1001];
    for(int j=1;j<=n;j++)
      cin>>s[j];
    double ans=0;
    for(int j=1;j<=n;j++)
      if(s[j]){
        int c=0;
        for(int a,b=j;(a=s[b]),(s[b]=0),(b=a);c++);
        ans+=res[c];
      }
    cout<<"Case #"<<i<<": "<<ans<<endl;
  }
}
