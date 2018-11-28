#include<sstream>
#include<vector>
#include<list>
#include<limits>
#include<iostream>
#include<set>
#include<string>
#include<map>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<iomanip>
#include<cmath>
#include<queue>
#include<gmpxx.h>

using namespace std;

typedef long long LL;

LL A[1000];
LL B[1001];

int main(){

  string ln;
  getline(cin,ln);
  LL T,R,k,N;
  string t;
  istringstream(ln)>>T;
  for(int t=1;t<=T;t++){
    getline(cin,ln);
    istringstream(ln)>>R>>k>>N;
    vector<LL> g(N);
    getline(cin,ln);
    istringstream in(ln);
    for(int i=0;i<N;i++){
      in>>g[i];
    }
    memset(A,-1,sizeof(A));
    B[0]=0;
    LL res=0;
    for(LL i=0,j=0;i<=R;i++){
      if(A[j]!=-1){
        res+=B[i];
        res+=(B[i]-B[A[j]])*((R-i)/(i-A[j]));
        res+=B[A[j]+((R-i)%(i-A[j]))]-B[A[j]];
        break;
      }
      if(i==R){
        res+=B[i];
        break;
      }
      A[j]=i;
      LL n=0;
      for(LL m=0;m<N;m++){
        if(n+g[j]>k){
          break;
        }
        n+=g[j];
        j=(j+1)%N;
      }
      B[i+1]=B[i]+n;
    }
    cout<<"Case #"<<t<<": "<<res<<endl;
  }

  return 0;
}



