#include <map> 
#include <set> 
#include <cmath> 
#include <queue> 
#include <vector> 
#include <string> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <cassert> 
#include <numeric> 
#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <ctime>
#include <math.h>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
int NN;
LL A[5000001];
LL C[5000001];
#define MOD 1000000007
int main(){
  string in;
  getline(cin,in);
  istringstream(in)>>NN;
  for(int II=1;II<=NN;++II){
    LL n,m,X,Y,Z;
    getline(cin,in);
    istringstream(in)>>n>>m>>X>>Y>>Z;
    for(int i=0;i<m;++i){
      getline(cin,in);
      istringstream(in)>>A[i];
    }
    map<LL,LL>B;
    LL res=0;
    for(int i=0;i<n;++i){
      LL a=A[i%m];
      LL b=1;
      for(typeof(B.begin())k=B.begin();k!=B.end();++k){
       if(k->first>=a)break;
       b=(b+k->second)%MOD;
      }
      B[a]+=b;
      res=(res+b)%MOD;
      A[i%m] = (X*A[i%m] + Y * (i + 1)) % Z;
    }

    cout<<"Case #"<<II<<": "<<res<<endl;
  }
  return 0;
}
