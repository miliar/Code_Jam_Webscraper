#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <sstream>

using namespace std;

#define iter(c) __typeof((c).begin())

#define rep(i,n) for(int i=0; i<(int)(n); i++)
#define repd(i,n) for(int i=(int)(n); i-->0;)
#define repi(i,a,b) for(int i=(int)(a); i<=(int)(b); i++)
#define times(n) for(int __times=(n); __times-->0;)
#define each(i, c) for (iter(c) i = (c).begin(); i != (c).end(); ++i)

#define all(a) (a).begin(),(a).end()
#define elem(e, c) (find(all(c), (e)) != (c).end())
#define pb push_back
#define mp make_pair
#define fst first
#define snd second

#define INF 1001001001
#define INFTY (INF<<32LL|INF)
#define EPS 1e-9
#define PI 3.141592653589793

typedef long long ll;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<double> vd;
typedef vector<string> vs;

template <class T>
void debug(vector<T> v){ each(i,v.size()) cout<<*i<<" "; cout<<endl; }

int nextInt(){ int t; scanf("%d", &t); return t; }
string next(){ string t; cin>>t; return t; }

bool isSq(ll a){
  ll b = sqrt(a);
  if((b-1)*(b-1)==a || (b)*(b)==a || (b+1)*(b+1)==a) return true;
  else return false;
}

string solve(string s){
  int N= s.size();
  int cntQ = 0;
  rep(i,N) if(s[i]=='?') cntQ++;
  rep(flags,1<<cntQ){
    ll x=0;
    int j=0;
    rep(i,N){
      switch(s[i]){
	case '0': x*=2;break;
	case '1': x*=2;x++; break;
	case '?': x*=2;x+=(flags>>j)&1;
		  j++; break;
	default: cerr<<"orz"<<endl;
      }
    }
    //cout<<x<<endl;
    j=0;
    if(isSq(x)){
      rep(i,N){
	switch(s[i]){
	  case '0': break;
	  case '1': break;
	  case '?': s[i]='0'+((flags>>j)&1);
		    j++; break;
	  default: cerr<<"orz"<<endl;
	}
      }
      return s;
    }
  }
  cerr<<"err"<<endl;
  return s;
}

int main(){
  int T=nextInt();
  repi(cases,1,T){
    string s=next();
    string ans=solve(s);
    cout<<"Case #"<<cases<<": ";
    cout<<ans;
    cout<<endl;
  }
  return 0;
}
