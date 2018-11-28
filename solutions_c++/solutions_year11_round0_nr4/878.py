#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <cstring>
#include <iomanip>

using namespace std;

double A[1001];
double dp[1001];
int vis[1001];
int B[1001];

double f(int n){
  if(n<=1) return 0;

  double e=1;
  double& res=dp[n];
  if(res!=-1) return res;

  res=0;

  for(int i=1;i<n;i++){
    e += (i>1?1:0) + f(i) + f(n-i);
//cout<<"c"<<i<<","<<n<<": "<<(i>1?1:0) + f(i) + f(n-i)<<endl;
  }

  res = e/(n-1);

  return res;
}

int main()
{
  string ln;
  int T,N;

  A[0]=1;
  for(int i=1;i<=1000;i++)
    A[i]=A[i-1]/i;

  getline(cin,ln);
  istringstream(ln)>>T;

  for(int test=1;test<=T;test++){

    for(int i=0;i<=1000;i++)
      for(int k=0;k<=1;k++)
        dp[i]=-1;

    bzero(vis,sizeof(vis));

    getline(cin,ln);
    istringstream(ln)>>N;

    getline(cin,ln);
    istringstream in(ln);

    for(int i=1;i<=N;i++)
      in>>B[i];

    double res=0;

    for(int i=1;i<=N;i++){
      if(vis[i]) continue;
      int n=1;
      for(int k=B[i];k!=i;k=B[k]){
        vis[k]=1;
        n+=1;
      }
      if(n>1) res+=1+f(n);
    }

    cout<<"Case #"<<test<<": "<<fixed<<setprecision(10)<<res<<endl;

  }

  return 0;
}
