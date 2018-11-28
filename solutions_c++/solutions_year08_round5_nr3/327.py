#define _CRT_SECURE_NO_DEPRECATE
#include <ctime>
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
template<class T> inline T Floor(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return (a-b+1)/b; return a/b; }
template<class T> inline T Ceil(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return a/b; return (a+b-1)/b; }
//#define SHOW_TIME
int N, M, K;
char a[15][15];
ll m[15][15][180000];
//int transfMask(int msk)
//{
//	int r=0;
//	FOR(i,0,M)
//	{
//		if (msk & (1<<i))
//		{
//			if (i-1>=0) r |= (1<<(i-1));
//			if (i+1<M) r |= (1<<(i+1));
//		}
//	}
//	return r;
//}
int createMask(int r[])
{
	int res=0;
	for (int i=M-1; i>=0; --i) res = res*3 + r[i];
	return res;
}
int newMask(int p[])
{
	int r[11];
	fill(r,0);
	FOR(i,0,M)
	{
		if (p[i] == 1)
		{
			if (i-1>=0) r[i-1] = 2;
			if (i+1<M) r[i+1] = 2;
		}
	}
	return createMask(r);
}
ll rec(int rw, int c, int msk)
{
	ll &r = m[rw][c][msk];
	if (r!=-1) return r;
	if (rw == N) return r = 0;
	int ok[11];
	int tmsk=msk;
	FOR(i,0,M)
	{
		ok[i] = tmsk%3;
		tmsk/=3;
	}

	int nmsk = newMask(ok);
	r = rec(rw+1, 0, nmsk);
	FOR(i,c,M)
	{
		if (a[rw][i]=='x' || ok[i]==2) continue;

		int tmp=ok[i];
		ok[i] = 1;
		nmsk = createMask(ok);
		r = max(r, 1+rec(rw, i+2, nmsk));
		ok[i] = tmp;

	}
	return r;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#ifdef SHOW_TIME
	clock_t startTime = clock();
#endif

	int Q;
	scanf("%d", &Q);
	FOR(q,0,Q)
	{
		printf("Case #%d: ", q+1);
		scanf("%d%d\n", &N, &M);
		FOR(i,0,N)
		{
			FOR(j,0,M)
			{
				a[i][j] = getchar();
			}
			getchar();
		}
		fill(m,-1);
		ll res = rec(0, 0, 0);
		printf("%lld\n", res);
	}

#ifdef SHOW_TIME
	clock_t endTime = clock();
	printf("\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
#endif
	return 0;
} 
