#include <iostream>
#include <queue>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <iomanip>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef pair<int,int> P2;
typedef pair<int,P2> P;

P v[1000001];
int B[1000001];
int E[1000001];
int W[1000001];

int main(){

  string ln;
  int T;

  getline(cin,ln);
  istringstream(ln)>>T;

  for(int test=1;test<=T;test++){

    double res=0,s,t,X,x=0,d,d2;
    int N,R,S;

    getline(cin,ln);
    istringstream(ln)>>X>>S>>R>>t>>N;

    LL e0=0;
    LL dist=0;

    for(int i=0;i<N;i++){
      int b,e,w;
      getline(cin,ln);
      istringstream(ln)>>b>>e>>w;
      v[i]=P(w,P2(b,e));

      dist+=b-e0;
      e0=e;
    }

    dist+=X-e0;

    d=dist;
    s=d/R;

    if(t>=s){
      res+=s;
      t-=s;
    }else{
      d2=t*R;
      res+=t;
      t=0;

      d=dist-d2;
      s=d/S;

      res+=s;
    }

    sort(v,v+N);

    for(int i=0;i<N;i++){

      int b=v[i].second.first;
      int e=v[i].second.second;
      int w=v[i].first;

      d=min(X-b,(double)(e-b));
      s=d/(w+R);

      if(t>=s){
        res+=s;
        t-=s;
      }else{
        d2=t*(w+R);
        res+=t;
        t=0;

        d=min(X-(b+d2),(double)(e-(b+d2)));
        s=d/(w+S);

        res+=s;
      }
    }

    cout<<"Case #"<<test<<": "<<fixed<<setprecision(10)<<res<<endl;

  }

  return 0;
}
