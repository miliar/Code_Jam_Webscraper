#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:16777216")
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
#include <cstdarg>
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
void print(const char *fmt, ...)  { va_list args; va_start(args, fmt); vprintf(fmt, args); vfprintf(stderr, fmt, args); va_end(args); }

int N, M, K;
int X, S, R, t;

#define MAX 111111
pair<pii, int> a[MAX];

double save(int x, int y, int w)
{
	double dx = y - x;
	double t1 = min<double>(t, dx / (w + R));
	double t2 = (dx - t1*(w+R)) / (w + S);

	double t3 = dx / (w+S);
	return t3 - (t1 + t2);
}

int main()
{
	freopen("inA.txt", "r", stdin);
	freopen("outA.txt", "w", stdout);
	clock_t startTime = clock();

	int Cases;
	scanf("%d", &Cases);
	FOR(Case,0,Cases)
	{
		print("Case #%d: ", Case+1);

		scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
		FOR(i,0,N)
		{
			int a1, a2, w;
			scanf("%d%d%d", &a1, &a2, &w);
			a[i] = mp(mp(a1,a2), w);
		}

		sort(a, a+N);

		vector<pair<pair<double,int>, pii>> v;
		int curX=0;
		FOR(i,0,N)
		{
			int dx;
			double s;
			if (a[i].X.X > curX)
			{
				dx = a[i].X.X-curX;
				//s = dx / (0.0 + S);
				s = -S;
				v.pb(mp(mp(-s, 0), mp(curX, a[i].X.X)));
			}
			dx = a[i].X.Y - a[i].X.X;
			//s = dx/(0.0 + a[i].Y + S);
			s = -(a[i].Y + S);
			v.pb(mp(mp(-s, -a[i].Y), a[i].X));
			curX = a[i].X.Y;
		}
		if (X > curX)
		{
			int dx = X - curX;
			//double s = dx/(0.0 + S);
			double s = -S;
			v.pb(mp(mp(-s, 0), mp(curX, X)));
		}

		sort(all(v));

		int n = sz(v);

		double res = 0.0;
		double maxT = t;
		FOR(i,0,n)
		{
			int dx = v[i].Y.Y - v[i].Y.X;
			double w = -v[i].X.Y;
			double t1 = min(maxT, dx / (w + R));
			double t2 = (dx - t1*(w+R)) / (w + S);
			maxT -= t1;
			res += t1 + t2;
		}

		print("%.10lf\n", res);
	}

	clock_t endTime = clock();
	fprintf(stderr, "\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
	return 0;
} 
