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
typedef ostringstream oss;
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define sz(a) ((int)a.size()) 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define pb push_back 
#define all(a) a.begin(),a.end()
#define mp make_pair 
#define inf 1000000000 
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }

int N, M;
int m[111][1011];
char engines[111][200];
int q[1111];
char qu[256];

int rec(int e, int quer)
{
	int &r = m[e][quer];
	if (r != -1) return r;
	r = inf;
	int p;
	for (p=quer; p<M; ++p)
	{
		if (q[p] == e)
		{
			for (int ee=0; ee<N; ++ee)
			{
				if (e == ee)
					continue;
				r = min(r, 1+rec(ee, p));
			}
			break;
		}
	}
	if (r == inf) r = 0;
	return r;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int C;
	scanf("%d\n", &C);
	FOR(c,0,C)
	{
		gets(qu);
		sscanf(qu, "%d", &N);
		FOR(i,0,N)
			gets(engines[i]);
		gets(qu);
		sscanf(qu, "%d", &M);
		FOR(i,0,M)
		{
			gets(qu);
			FOR(j,0,N)
			{
				if (strcmp(qu, engines[j]) == 0)
				{
					q[i] = j;
					break;
				}
			}
		}

		fill(m, -1);
		int mn=inf;
		FOR(i,0,N)
		{
			int t = rec(i, 0);
			if (t < mn)
				mn = t;
		}
		printf("Case #%d: %d\n", c+1, mn);
	}
	return 0;
} 
