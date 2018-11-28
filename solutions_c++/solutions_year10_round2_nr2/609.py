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
typedef pair<int,int> P;

int main(){

  string ln;
  getline(cin,ln);
  LL C;
  istringstream(ln)>>C;
  for(LL c=1;c<=C;c++){
    getline(cin,ln);
    LL N,K,B,T,X[100],V[100];
    istringstream(ln)>>N>>K>>B>>T;
    getline(cin,ln);
    istringstream in(ln);
    getline(cin,ln);
    istringstream in2(ln);
    for(LL i=0;i<N;i++){
      in>>X[i];
      in2>>V[i];
    }
    LL bad=0;
    LL good=0;
    LL res=0;
    for(int i=N-1;i>=0;i--){
      if(((double)B-X[i])/V[i]>T){
        bad++;
      }else{
        good++;
        res+=bad;
        if(good==K){
          break;
        }
      }
    }
    if(good==K)
          cout<<"Case #"<<c<<": "<<res<<endl;
    else
      cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
  }

  return 0;
}
