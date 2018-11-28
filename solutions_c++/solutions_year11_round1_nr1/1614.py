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
static const double EPS = 1e-10;
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

int output(string n){
	static int a = 1;
	cout << "Case #" << a++ << ": " << n << endl;
}

int check(int N,int PD,int PG){
		for(int D=1;D<=N;D++){
			for(int G=0;G<=1000;G++){
				if( (D*PD) % 100 == 0){
					int w = (D*PD) / 100;
					for(int y = 0;y<=G;y++){
						if( 100.0*(w+y) / (D+G) == PG){
							//cout << ">" << D << " " << G << " " << w << " " << y << endl;
							return D;
						}
					}
				}
			}
		}
		return -1;
}
int main(){
	int n;
	cin >> n;
	while(n--){
		int N;
		int PD,PG;
		cin >> N >> PD >> PG;
		bool f = false;
		int e = check(N,PD,PG);
		if(e != -1 && e)f = true; 
		output(f?"Possible":"Broken");
	}
}