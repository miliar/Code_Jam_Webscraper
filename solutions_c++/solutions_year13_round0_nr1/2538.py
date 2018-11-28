#pragma comment(linker, "/STACK:16777216")
#pragma warning(default :4)
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <string.h>
#include <utility>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <ctime>
#include <queue>
#include <cmath>
#include <deque>
#include <list>
#include <sstream>
#include <bitset>
#include <complex>
#include <functional>
#include <numeric>
//#include <unordered_set>
//#include <unordered_map>
#include <cassert>
#include <iomanip>
#define mp make_pair
#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define CL(x) memset(x, 0, sizeof(x))
#define SINF(x) memset(x, 0x3F, sizeof(x))
#define SVAL(x, y) memset(x, y, sizeof(x))
#define CP(t, f) memcpy(t, f, sizeof(f));
#define CPS(t, f, s) memcpy(t, f, s*sizeof(f[0]))
#define FIN freopen("in.txt", "r", stdin);
#define FINOUT freopen("in.txt", "w", stdout);
#define FOUT freopen("out.txt", "w", stdout);
#define y1 ____y1
using namespace std;
typedef const int CI;
typedef long long ll;
typedef unsigned long long ull;
//typedef __float128 ld;
//typedef long double ld;
typedef double ld;
typedef vector<int> VINT;
typedef vector<ld> VLD;
typedef vector<ll> VLL;
typedef vector<vector<int> > VVINT;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef pair<ld, ld> PDD;
typedef pair<ld, ld> ptp;
typedef complex<ld> Cn;
typedef vector<PII> VPII;
typedef unsigned int uint;
const ld eps = 1e-9;
//const int INF = 1000000001;
const int oo = 0x3F3F3F3F;
const ll ooLL = 0x3F3F3F3F3F3F3F3FLL;
const int MOD = 1000000007;
void deb() { std::cerr << '\n'; }
template<typename T> T sqr(T x) { return x*x; }
template<typename T1> void deb(T1 x1) { std::cerr << x1 << '\n'; }
template<typename T1, typename T2> void deb(T1 x1, T2 x2) { std::cerr << x1 << " " << x2 << '\n'; }
template<typename T1, typename T2, typename T3> void deb(T1 x1, T2 x2, T3 x3) { std::cerr << x1 << " " << x2 << " " << x3 << '\n'; }
const ld PI=acos(-1.);
ll Round(double x) { return x<0 ? x-.5 : x+.5; }

int n=4;
char s[7][7];
bool gt(char c)
{
	bool z1=1, z2=2;
	REP(i, n)
	{
		bool o=1; REP(j, n) o&=s[i][j]==c || s[i][j]=='T'; if (o) return 1;
		o=1; REP(j, n) o&=s[j][i]==c || s[j][i]=='T'; if (o) return 1;
		z1&=s[i][i]==c || s[i][i]=='T';
		z2&=s[i][n-i-1]==c || s[i][n-i-1]=='T';
	}
	return z1 || z2;
}
int main()
{
	int t;
	scanf("%d", &t);
	REP(it, t)
	{
		printf("Case #%d: ", it+1);
		gets(s[0]);
		REP(i, n) gets(s[i]);
		
		if (gt('X')) puts("X won");
		else if (gt('O')) puts("O won");
		else
		{
			int c=0; REP(i, n) REP(j, n) c+=s[i][j]=='.';
			puts(c?"Game has not completed":"Draw");
		}
	}
	return 0;
}
