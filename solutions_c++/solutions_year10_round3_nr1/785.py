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

using namespace std;

typedef long long LL;

int main(){

  string ln;
  getline(cin,ln);
  LL T;
  istringstream(ln)>>T;
  for(LL t=1;t<=T;t++){
    getline(cin,ln);
    LL N,A[1000],B[1000];
    istringstream(ln)>>N;
    for(LL i=0;i<N;i++){
      getline(cin,ln);
      istringstream(ln)>>A[i]>>B[i];
    }
    LL res=0;
    for(int i=0;i<N;i++){
      for(int k=i+1;k<N;k++){
        if(A[i]<A[k]){
          if(B[i]>B[k]){
            res++;
          }
        }else{
          if(B[i]<B[k]){
            res++;
          }
        }
      }
    }
    cout<<"Case #"<<t<<": "<<res<<endl;
  }

  return 0;
}
