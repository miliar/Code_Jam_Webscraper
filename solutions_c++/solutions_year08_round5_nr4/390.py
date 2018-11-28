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
int H, W, R;
int r[100], c[100];
int a[101][101];
bool bad(int rw, int cl)
{
	FOR(i,0,R) if (r[i]==rw && c[i]==cl) return true;
	return false;
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
		scanf("%d%d%d", &H, &W, &R);
		FOR(i,0,R)
		{
			scanf("%d%d", &r[i], &c[i]);
		}
		fill(a,0);
		a[1][1] = 1;
		FOR(row,1,H+1)
			FOR(col,1,W+1)
		{
			if (bad(row, col)) continue;
			if (row-2>=1 && col-1>=1) a[row][col] += a[row-2][col-1];
			if (row-1>=1 && col-2>=1) a[row][col] += a[row-1][col-2];
			a[row][col] %= 10007;
		}
		printf("%d\n", a[H][W]);
	}

#ifdef SHOW_TIME
	clock_t endTime = clock();
	printf("\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
#endif
	return 0;
} 
