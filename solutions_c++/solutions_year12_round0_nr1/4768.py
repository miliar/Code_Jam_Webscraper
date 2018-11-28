//#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

template<typename T> T GCD(T a, T b) {return (b == 0) ? abs(a) : GCD(b, a % b);}
template<typename T> inline T LCM(T a, T b) {return a / GCD(a, b) * b;}
template<typename T> inline T MOD(T a, T b) {return (a % b + b) % b;}
template<typename T> inline T SQR(T x) {return x * x;}
template<typename T> inline string tostring(const T& x) {ostringstream os;os << x;return os.str();}

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forba(i, b, a) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define memoset(a , b) memset(a, b, sizeof(a))
#define pb push_back
#define mp make_pair
#define se(x) cout<<#x<<" = "<<x<<endl
#define oo 0x3f3f3f3f
#define PI acos(-1.0)
#define eps 1e-8
#define MAXN 150
#define MOD 100000
#define Max(x, y) ((x) >= (y) ? (x) : (y))
#define Min(x, y) ((x) <= (y) ? (x) : (y))
#define Abs(x) ((x) >= 0 ? (x) : (-(x)))
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define Bug puts("here!!!") 

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

char str[MAXN];
map<char, char> hash;
void Init()
{
	hash['a'] = 'y'; hash['b'] = 'h'; hash['c'] = 'e'; hash['d'] = 's';
	hash['e'] = 'o'; hash['f'] = 'c'; hash['g'] = 'v'; hash['h'] = 'x';
	hash['i'] = 'd'; hash['j'] = 'u'; hash['k'] = 'i'; hash['l'] = 'g';
	hash['m'] = 'l'; hash['n'] = 'b'; hash['o'] = 'k'; hash['p'] = 'r';
	hash['q'] = 'z'; hash['r'] = 't'; hash['s'] = 'n'; hash['t'] = 'w';
	hash['u'] = 'j'; hash['v'] = 'p'; hash['w'] = 'f'; hash['x'] = 'm';
	hash['y'] = 'a'; hash['z'] = 'q';
}
void solve()
{
	freopen("C://in.txt", "r", stdin);
	freopen("C://out.txt", "w", stdout);
	int T;
	int i, cas;
	Init();
	scanf("%d", &T);
	getchar();
	for (cas = 1; cas <= T; cas++)
	{
		gets(str);
		for (i = 0; str[i] != 0; i++)
		{
			if (str[i] != ' ')
				str[i] = hash[str[i]];
		}
		printf("Case #%d: %s\n", cas, str);
	}
}
int main()
{
	solve();
	return 0;
}