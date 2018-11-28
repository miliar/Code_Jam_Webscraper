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

#define SZ 510

int res[SZ][20];

char buf[SZ];

char words[] = "welcome to code jam";

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	gets(buf);
	int n;
	sscanf(buf, "%d", &n);

	REP(i, n)
	{
		gets(buf);
		memset(res, 0, sizeof(res));
		int len = strlen(buf);
		REP(j, len)
		{
			if(buf[j] == 'w')
				res[j][0] = 1;
		}
		int num = strlen(words);
		FOR(j, 1, num)
		{
			int sum = 0;
			REP(k, len)
			{
				if(sum >= 10000)
					sum -= 10000;
				if(buf[k] == words[j])
					res[k][j] = sum;
				sum += res[k][j - 1];
			}
		}
		int r = 0;
		REP(j, len)
			r += res[j][num - 1];
		r %= 10000;
		printf("Case #%d: %04d\n", i + 1, r);
	}
	
	return 0;
}
