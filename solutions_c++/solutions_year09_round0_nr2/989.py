#define _CRT_SECURE_NO_DEPRECATE 
#ifndef ONLINE_JUDGE 
#include <ctime> 
#endif 
#include <iostream> 
#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <functional> 
#include <algorithm> 
#include <sstream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 

using namespace std; 

#define FOR(i, a, b) for(int i = a; i < b; ++i) 
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i) 
#define REP(i, N) for(int i = 0; i < N; ++i) 
#define RREP(i, N) for(int i = N - 1; i >= 0; --i) 

#define ABS(N) (((N) < 0) ? (-(N)) : (N)) 
#define MIN(A, B) (((A) < (B)) ? (A) : (B)) 
#define MAX(A, B) (((A) > (B)) ? (A) : (B)) 
#define EPS 1e-7 
#define ALL(V) V.begin(), V.end() 
#define pb push_back 
#define mp make_pair 
#define Pi 3.14159265358979323846 
#define SIZE(V) V.size() 


typedef vector <int> VI; 
typedef pair <int, int> PI; 
typedef long long Long; 
typedef unsigned int Uint; 
typedef unsigned long long ULong; 
typedef unsigned char Uchar; 

#define sz(a) ((int)a.size()) 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define all(a) a.begin(),a.end() 
#define inf 1000000000 
#define X first 
#define Y second 
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = 
b%a, b = t; return a+b; } 
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if 
(p&1) r = r*a; a = a*a; p >>= 1; } return r; } 
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, 
y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - 
a/b*y1; return g; } 
template<class T> inline T Floor(T a, T b) { if (b<0) a=-a, b=-b; if 
(a<0) return (a-b+1)/b; return a/b; } 
template<class T> inline T Ceil(T a, T b) { if (b<0) a=-a, b=-b; if 
(a<0) return a/b; return (a+b-1)/b; } 

typedef vector<int> vi; 
typedef vector<string> vs; 
typedef pair<int,int> pii; 
typedef long long ll; 

#define SZ 110

int T;
int n;
int m;

int a[SZ][SZ];

char res[SZ][SZ];

int Q[SZ*SZ][2];
int h1;
int h2;

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};


bool flow(int x, int y, int x1, int y1)
{
	int A = 1000000;
	int x2;
	int y2;
	REP(k, 4)
	{
		x2 = x + dx[k];
		y2 = y + dy[k];
		if(x2 < 0 || x2 >= n)
			continue;
		if(y2 < 0 || y2 >= m)
			continue;
		if(A > a[x2][y2])
			A = a[x2][y2];
	}
	if(A >= a[x][y])
		return 0;
	REP(k, 4)
	{
		x2 = x + dx[k];
		y2 = y + dy[k];
		if(x2 < 0 || x2 >= n)
			continue;
		if(y2 < 0 || y2 >= m)
			continue;
		if(A == a[x2][y2])
			return x2 == x1 && y2 == y1;
	}
	return 0;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &T);
	REP(I, T)
	{
		scanf("%d%d", &n, &m);
		REP(i, n)
			REP(j, m)
				scanf("%d", &a[i][j]);

		memset(res, 0, sizeof(res));
		char ch = 'a';
		REP(i, n)
			REP(j, m)
				if(!res[i][j])
				{
					res[i][j] = ch;
					Q[0][0] = i;
					Q[0][1] = j;
					h1 = 0;
					h2 = 1;
					int x;
					int y;
					int x1;
					int y1;
					while(h1 ^ h2)
					{
						x = Q[h1][0];
						y = Q[h1][1];
						++h1;
						REP(k, 4)
						{
							x1 = x + dx[k];
							y1 = y + dy[k];
							if(x1 < 0 || x1 >= n)
								continue;
							if(y1 < 0 || y1 >= m)
								continue;
							if(res[x1][y1] == 0 && (flow(x, y, x1, y1) || flow(x1, y1, x, y)))
							{
								res[x1][y1] = ch;
								Q[h2][0] = x1;
								Q[h2][1] = y1;
								++h2;
							}
						}
					}
					++ch;
				}
		printf("Case #%d:\n", I + 1);
		REP(i, n)
			REP(j, m)
				printf("%c%c", res[i][j], j == m - 1 ? '\n' : ' ');
	}

	return 0;
}