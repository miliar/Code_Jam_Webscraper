#include <iostream>
#include <queue>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long LL;

LL A[1001];
LL B[1000001];

int main(){

  string ln;
  int T;

  getline(cin,ln);
  istringstream(ln)>>T;

  for(int test=1;test<=T;test++){

    LL L,t,N,C;

    getline(cin,ln);
    istringstream in(ln);
    in>>L>>t>>N>>C;

    for(int i=0;i<C;i++){
      in>>A[i];
    }

    for(int i=0;i*C<N;i++){
      for(int k=0;k<C;k++){
        B[i*C+k]=A[k];
      }
    }

    LL k=N;
    LL res1=0;
    LL res2=0;
    LL time=0;

    for(int i=0;i<N;i++){
      if(k==N && time+2*B[i]>t){
        k=i+1;
        if(L>0) res2-=((time+2*B[i])-t)/2;
      }
      time+=2*B[i];
    }

    sort(B+k,B+N);

    res1+=time;
    for(int i=0;i<L && N-(i+1)>=k;i++){
      res1-=B[N-(i+1)];
    }

    res2+=time;
    for(int i=0;i<L-1 && N-(i+1)>=k;i++){
      res2-=B[N-(i+1)];
    }

    cout<<"Case #"<<test<<": "<<min(res1,res2)<<endl;
  }

  return 0;
}
