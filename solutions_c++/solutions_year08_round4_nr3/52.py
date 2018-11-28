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

int x[11111], y[11111], z[11111], p[11111];
const double eps=1e-7;
bool ok(int i, int j, double m)
{
	return (abs(x[i]-x[j])+abs(y[i]-y[j]) + abs(z[i]-z[j]) < (p[i]+p[j])*m + eps);
}
bool can(double m)
{
	FOR(i,0,N)
		FOR(j,i+1,N)
	{
		if (!ok(i,j,m))
			return false;
	}
	return true;
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif 
	int Q;
	scanf("%d", &Q);
	FOR(q,0,Q)
	{
		scanf("%d", &N);
		FOR(i,0,N) scanf("%d%d%d%d", &x[i], &y[i], &z[i], &p[i]);

		double l=0, r = 30000000;
		const double eps = 1e-8;
		while (fabs(l-r) > eps)
		{
			double m=(l+r)/2.0;

			if (can(m))
			{
				r = m;
			}
			else
			{
				l = m;
			}
		}
		printf("Case #%d: %.6lf\n", q+1, (l+r)/2.0);
	}
	return 0;
} 
