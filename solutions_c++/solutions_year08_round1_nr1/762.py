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
#include <functional>

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
#define maxn 1100
#define maxp 1100000

int doit(){
  int n;
  cin>>n;
  vector<int> a(n), b(n);
  for(int i=0;i<n;i++)cin>>a[i];
  for(int i=0;i<n;i++)cin>>b[i];
  sort(a.begin(),a.end());
  sort(b.begin(),b.end(),greater<int>());
  int p=0;
  for(int i=0;i<n;i++)p+=a[i]*b[i];
  return p;
}

int main(){
  int T;
  cin>>T;
  for(int C=1; C<=T; C++) {
    int p=doit();
    cout << "Case #"<<C<<": "<<p<<endl;
  }
}
