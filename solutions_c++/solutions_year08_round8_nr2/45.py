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
#define infL (1LL<<62)
#define X first
#define Y second
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }
template<class T> inline T Floor(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return (a-b+1)/b; return a/b; }
template<class T> inline T Ceil(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return a/b; return (a+b-1)/b; }
int N, M, K;

struct Item
{
	int a, b;
	int ind;
	bool operator<(const Item& it) const
	{
		if (a == it.a) return b<it.b;
		return a < it.a;
	}
};
#define MAXN 305
short m[MAXN][MAXN][MAXN];
Item items[MAXN];
map<string,int> Map;
inline short min(short a, short b) { return (a<b)?a:b; }
short rec(int last, int c1, int c2)
{
	short &r=m[last][c1][c2];
	if (r != -1) return r;
	if (items[last].b == 10000)
		return r = 0;
	r = 500;

	int c;
	FOR(i,last+1,N)
	{
		c = items[i].ind;
		if (items[i].a <= items[last].b+1)
		{
			if (c == items[last].ind)
				r = min(r, 1+rec(i, c1, c2));
			else if (c == c1 || c1 == N)
				r = min(r, 1+rec(i, items[last].ind, c2));
			else if (c == c2 || c2 == N)
				r = min(r, 1+rec(i, c1, items[last].ind));
		}
	}
	return r;
}
int gcnt=0;
int getInd(const string& s)
{
	if (Map.count(s)) return Map[s];
	Map[s] = gcnt++;
	return gcnt-1;
}
char buf[256];
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
//#define SHOW_TIME
#ifdef SHOW_TIME
	clock_t startTime = clock();
#endif
	int Q;
	scanf("%d", &Q);
	FOR(q,0,Q)
	{
		printf("Case #%d: ", q+1);
		fflush(stdout);
		Map.clear();
		gcnt = 0;
		scanf("%d\n", &N);
		FOR(i,0,N)
		{
			int a, b;
			scanf("%s%d%d\n", buf, &a, &b);
			int ind = getInd(buf);
			items[i].a = a;
			items[i].b = b;
			items[i].ind = ind;
		}
		sort(items, items+N);
		fill(m, -1);
		int bst = 500;
		FOR(i,0,N)
		{
			if (items[i].a == 1)
			{
				bst = min(bst, 1+rec(i,N,N));
			}
			else break;
		}
		
		if (bst >= 500)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", (int)bst);
		fflush(stdout);
	}

#ifdef SHOW_TIME
	clock_t endTime = clock();
	printf("\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
#endif
	return 0;
} 
