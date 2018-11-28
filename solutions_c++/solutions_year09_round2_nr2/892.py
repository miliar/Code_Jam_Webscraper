#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <stack>
#include <queue>
using namespace std; 

#define ALL(v) (v).begin(), (v).end()
#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,n) for(LET(i,a);i!=n;i++)
#define REP(i,n) FOR(i,0,n)
#define sz size()
#define pb(x) push_back(x)
#define DEBUG(x) {REP(i,x.sz) cout<<x[i]<<" "; cout <<endl;}
#define VI vector<int>
const int INF = int(1e8);

VI convertToNumber(string t){
  VI ret;
  REP(i,t.sz) ret.pb(t[i]-'0');
  
  return ret;
}

string convertToString(VI a){
  string ret="";
  REP(i,a.sz) ret+=a[i] + '0';
  return ret;
}
int main(){
  int n;
  cin >> n ;
  REP(i,n){
    string t; cin >> t;
    VI a = convertToNumber(t);
    VI _a = a;
    next_permutation(a.begin(),a.end());
    string temp = convertToString(a);
    if(temp<=t) {
	 a = _a;
	 reverse(a.begin(),a.end());
	 a.pb(0);
	 reverse(a.begin(),a.end());
	 next_permutation(a.begin(),a.end());
	 
    }
    cout<< "Case #" << i+1 << ": ";
    REP(i,a.sz) cout<<a[i];
    cout<<endl;
  }
}
