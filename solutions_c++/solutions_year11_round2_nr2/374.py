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
using namespace std;
static const long double EPS = 1e-10;
typedef long long ll;
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n-1;i>=0;i--)
#define all(a) a.begin(),a.end()
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define SS stringstream
#define DBG1(a) rep(_X,sz(a)){printf("%d ",a[_X]);}puts("");
#define DBG2(a) rep(_X,sz(a)){rep(_Y,sz(a[_X]))printf("%d ",a[_X][_Y]);puts("");}
#define bitcount(b) __builtin_popcount(b)
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)

#define delete(a,n) a.erase(remove(all(a),n),a.end())
template<typename T, typename S> vector<T>& operator<<(vector<T>& a, S b) { a.push_back(b); return a; }
template<typename T> void operator>>(vector<T>& a, int b) {while(b--)if(!a.empty())a.pop_back();}
bool isprime(int n){ if(n<2)return false;  for(int i=2;i*i<=n;i++)if(n%i==0)return false;  return true;} 
ll b_pow(ll x,ll n){return n ? n==1 ? x: b_pow(x,n>>1)*b_pow(x,(n>>1)+(n&1)) : 1;}
string itos(int n){stringstream ss;ss << n;return ss.str();}

int output(long double n){
	static int a = 1;
	cout << "Case #" << a++ << ": ";
	printf("%.6Lf\n",n);
}

long double pos[200];
long double num[200];

int C,D;

bool simulate(long double time){
	long double le = -time + D * (num[0]-1);
	if(le > time) return false;
	
	for(int i=1;i<C;i++){
		long double p = le + D;
		if( pos[i]+time < le+D ){
			return false; // ちゅうい
		}else{
			p = max(le+D,pos[i] - time);
		}
		le = p + D * (num[i]-1);
		if(le-pos[i] > time) return false;
	}
	return true;
}
int main(){
	int T;
	cin >> T;
	while(T--){
		cin >> C >> D;
		long double m = (1ll<<62)-1;
		rep(i,C){
			long double a,b;
			cin >> a >> b;
			pos[i] = a , num[i] = b;
			m = min(m,a);
		}
		rep(i,C) pos[i] -= m;
		long double l = 0 , r = 1e20;
		rep(X,1000){
			long double m = (l+r) / 2;
			if( simulate(m) ){
				r = m;
			}else{
				l = m;
			}
		}
		output(l);
	}
}