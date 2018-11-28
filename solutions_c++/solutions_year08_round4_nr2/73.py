#define _CRT_SECURE_NO_DEPRECATE 
#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 
using namespace std; 
typedef vector<int> vi; 
typedef vector<string> vs; 
typedef pair<int,int> pii; 
typedef long long ll; 
typedef istringstream iss;
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define sz(a) ((int)a.size()) 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define pb push_back 
#define all(a) a.begin(),a.end()
#define mp make_pair 
#define inf 1000000000 
#define X first
#define Y second
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }

int N, M, K;

ll area(ll x1, ll y1, ll x2, ll y2)
{
	ll r = (x1*y2-x2*y1);
	if (r <0) return -r; else return r;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif 
	int Q;
	scanf("%d", &Q);
	FOR(q,0,Q)
	{
		ll A;
		scanf("%d%d%lld", &N, &M, &A);
		bool ok=false;
		FOR(x1,0,N+1) FOR(y1,0,M+1)
		FOR(x2,0,N+1) FOR(y2,0,M+1)
		{
			if (area(x1,y1,x2,y2) == A)
			{
				ok = true;
				printf("Case #%d: 0 0 %d %d %d %d\n", q+1, x1, y1, x2, y2);
				goto end;
			}
		}
end:
		if (!ok)
			printf("Case #%d: IMPOSSIBLE\n", q+1);
	}

	return 0;
} 
