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
int output(){
	static int a = 1;
	cout << "Case #" << a++ << ": ";
}
pair<long double,long double> calc(long double dist , long double rT , long double S , long double R){
		long double use = min(rT,dist/R);
		long double move = use * R;
		return make_pair(use + (dist-move) / S , use);
}


long double X,S,R,t,N;

class IT{
public:
	double dist , acc;
	IT(double a,double b){dist = a , acc = b;}
};
bool operator < (const IT &a , const IT& b){
	return (S+b.acc+R) > (S+a.acc+R);
}

int main(){
	int Te;
	cin >> Te;
	while(Te--){
		cin >> X >> S >> R >> t >> N;
		int cur = 0;
		
		vector<IT> get;
		
		int B,E=0,W;
		for(int i=0;i<N;i++){
			cin >> B >> E >> W;
			get.push_back(IT(B-cur,0));
			get.push_back(IT(E-B,W));
			cur = E;
		}
		get.push_back(IT(X-cur,0));
		sort(all(get));
		
		long double ans = 0;
		long double rT = t;
		
		

		for(int i=0;i<get.size();i++){
			
			long double dist,w;
			dist = get[i].dist , w = get[i].acc;
			
			long double two = calc(dist,rT,S+w,R+w).first;
			rT -= calc(dist,rT,S+w,R+w).second;
			ans += two;
		}
		
		
		output();
		printf("%.9f\n",(double)ans);
	}
}