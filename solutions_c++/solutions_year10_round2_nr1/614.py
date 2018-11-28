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
  int T,N,M;
  istringstream(ln)>>T;
  for(int t=1;t<=T;t++){
    set<string> S;
    getline(cin,ln);
    istringstream(ln)>>N>>M;
    for(int i=0;i<N;i++){
      getline(cin,ln);
      for(int k=1;k<ln.size();k++){
        if(ln[k]=='/'){
          string d=ln.substr(0,k);
          S.insert(d);
        }
      }
      S.insert(ln);
    }
    LL res=0;
    for(int i=0;i<M;i++){
      getline(cin,ln);
      for(int k=1;k<ln.size();k++){
        if(ln[k]=='/'){
          string d=ln.substr(0,k);
          if(!S.count(d)){
            S.insert(d);
            res++;
          }
        }
      }
      if(!S.count(ln)){
        S.insert(ln);
        res++;
      }
    }
    cout<<"Case #"<<t<<": "<<res<<endl;
  }

  return 0;
}
