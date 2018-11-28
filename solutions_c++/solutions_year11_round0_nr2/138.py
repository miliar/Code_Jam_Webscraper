#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>
#include <cassert>
using namespace std;
static const double EPS = 1e-10;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> PI;
#define rep(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define SZ(a) (int(a.size()))
#define F first
#define S second
const double pi=acos(-1);
int dx[]={0,1,0,-1},dy[]={1,0,-1,0};

main(){
  int T;
  cin>>T;
  rep(ca,T){
    cout<<"Case #"<<ca+1<<": ";
    int c,d;
    map<pair<char,char>,string> com;
    cin>>c;
    while(c--){
      string in;
      cin>>in;
      com[mp(min(in[0],in[1]),max(in[0],in[1]))]=in.substr(2);
    }
    cin>>d;
    set<pair<char,char> > opp;
    while(d--){
      char a,b;
      cin>>a>>b;
      opp.insert(mp(min(a,b),max(a,b)));
    }
    int n;
    cin>>n;
    string in;
    cin>>in;

    for(int i=1;i<SZ(in);i++){
      char a=min(in[i-1],in[i]),b=max(in[i-1],in[i]);
      if(com.count(mp(a,b))){
        in.erase(i-1,2);
        in.insert(i-1,com[mp(a,b)]);
        i=0;
      }else{
        for(int j=i-1;j>=0;--j){
          char a=min(in[j],in[i]),b=max(in[j],in[i]);
          if(opp.count(mp(a,b))){
            in.erase(0,i+1);
            i=0;
            break;
          }
        }
      }
    }
    cout<<'[';
    rep(i,SZ(in)){
      if(i)cout<<", ";
      cout<<in[i];
    }
    cout<<']'<<endl;
  }
}
