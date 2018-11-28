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

int output(vector<long double> n){
	static int a = 1;
	cout << "Case #" << a++ << ":" << endl;
	rep(i,n.size())printf("%.16Lf\n",n[i]);
}
vector<long double> wp , owp , oowp;
vector<string> data;

long double calc(int n,int c){
	long double ans = 0;
	int d = 0;
	for(int i=0;i<data.size();i++){
		if(i == c) continue;
		if(data[n][i] != '.'){
			ans += data[n][i] == '1';
			d++;
		}
	}
	return ans / d;
}

long double rec(int n,int depth,bool f,int prev){
	long double ans = 0;
	int c = 0;
	if(!depth){
		return f ? calc(n,prev) : owp[n];
	}else{
		rep(i,data.size()){
			if(data[n][i] != '.') ans += rec(i,depth-1,f,n),c++;
		}
	}
	if(c)ans/=c;
	return ans;
}

int main(){
	int T;
	cin >> T;
	while(T--){
		int n;
		cin >> n;
		wp.resize(n);
		owp.resize(n);
		oowp.resize(n);
		data.resize(n);
		rep(i,n)cin >> data[i];
	
		vector<long double> ans(n);
		rep(i,n) wp[i] = calc(i,-1);
		rep(i,n) owp[i] = rec(i,1,1,-1);
		rep(i,n) oowp[i] = rec(i,1,0,-1);
		
		rep(i,n)ans[i] = wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25;
		output(ans);
		
	}
}