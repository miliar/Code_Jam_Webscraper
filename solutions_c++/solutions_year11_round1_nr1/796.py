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
#include<cstdlib>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)      REP(i,0,n)
#define pb push_back 
#define mp make_pair
#define ALL(C)   (C).begin(),(C).end()
template<class T> void vp(T &a,int p){rep(i,p)cout << a[i]<<" ";cout << endl;} 

typedef complex<double>P;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;

ll gcd(ll a,ll b){
  return b==0?a:gcd(b,a%b);
}

bool solve(ll n,int pd,int pg){
  if (pd == 100 && pg == 100)return true;
  if (pd < 100 && pg == 100)return false;
  if (pd == 0 && pg == 0)return true;
  if (0 < pd && pg == 0)return false;
  ll tmp=gcd(100,pd);
  return 100/tmp <= n;
}

main(){
  int te;
  cin>>te;
  rep(tc,te){
    ll n;
    int pd,pg;
    cin>>n>>pd>>pg;
    cout << n << " " << pd <<" " << pg << endl;
    cout <<"Case #" << tc+1  << ":";
    if (solve(n,pd,pg))cout <<" Possible" <<endl;
    else cout <<" Broken" << endl;
  }
  return false;
}
