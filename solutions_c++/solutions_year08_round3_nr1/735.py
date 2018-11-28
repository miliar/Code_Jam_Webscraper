#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1000000000

string doit(){
  int p,k,l;
  int i,j,t;

  cin>>p>>k>>l;
  if(p*k<l)return "Impossible";

  vector<pair<int,int> > f(l);
  for(i=0;i<l;i++){
    cin>>t;
    f[i]=make_pair(t,i);
  }
  sort(f.begin(), f.end(), greater<pair<int,int> >());

  vector<int> pt(l);
  t=0;
  for(i=0;i<p&&t<l;i++)for(j=0;j<k&&t<l;j++){
    pt[f[t++].second]=i+1;
  }

  LL r=0;
  for(i=0;i<l;i++)
    r+=f[i].first*pt[f[i].second];
  return i2s(r);
}

int main(){
  int T;
  cin>>T;
  for(int C=1; C<=T; C++) {
    string r=doit();
    cout << "Case #"<<C<<": "<<r<<endl;
  }
}
