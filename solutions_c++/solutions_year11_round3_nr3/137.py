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

LL A[10001]; 

int main(){

  string ln;
  int T;

  getline(cin,ln);
  istringstream(ln)>>T;

  for(int test=1;test<=T;test++){

    LL N,L,H;

    getline(cin,ln);
    istringstream(ln)>>N>>L>>H;

    getline(cin,ln);
    istringstream in(ln);

    for(int i=0;i<N;i++){
      in>>A[i];
    }

    LL res=0;

    for(LL n=L;n<=H;n++){
      bool ok=1;

      for(int i=0;i<N;i++){
        if(A[i]<n){
          if((n%A[i])!=0) { ok=0; break; }
        }

        if(A[i]>n){
          if((A[i]%n)!=0) { ok=0; break; }
        }
      }

      if(ok) { res=n; break; }
    }

    if(!res) cout<<"Case #"<<test<<": NO"<<endl;
    else cout<<"Case #"<<test<<": "<<res<<endl;
  }

  return 0;
}
