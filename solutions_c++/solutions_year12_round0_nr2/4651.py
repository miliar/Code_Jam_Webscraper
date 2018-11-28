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

int dat[MAXN];
int dp[MAXN][MAXN];
int judge1(int val, int p)
{
	int temp;
	if (val < p)
		return 0;
	temp = val / 3;
	if (val % 3 == 0)
	{
		if (temp >= p)
			return 1;
		else
			return 0;
	}
	else
	{
		if (temp + 1 >= p)
			return 1;
		else
			return 0;
	}
}
int judge2(int val, int p)
{
	int temp;
	if (p == 0)
	{
		if (val >= 2)
			return 1;
		else
			return 0;
	}
	else
	{
		if (val < p)
			return 0;
		else if ((val - 2) % 3 == 0)
			temp = (val - 2) / 3;
		else if ((val - 3) % 3 == 0)
			temp = (val - 3) / 3;
		else if ((val - 4) % 3 == 0)
			temp = (val - 4) / 3;
		if (temp + 2 >= p && temp >= 0)
			return 1;
		else
			return 0;
	}
}
void solve()
{
	//freopen("C://in.txt", "r", stdin);
	//freopen("C://out.txt", "w", stdout);
	int T;
	int N, S, p;
	int ans;
	scanf("%d", &T);
	forab (cas, 1, T)
	{
		scanf("%d%d%d", &N, &S, &p);
		forab (i, 1, S)
		{
			forab (j, 1, N)
				dp[i][j] = -oo;
		}
		forab (i, 1, N)
			scanf("%d", &dat[i]);
		dp[0][0] = 0;
		forab (i, 1, N)
			dp[0][i] = dp[0][i - 1] + judge1(dat[i], p);
		if (judge2(dat[1], p))
			dp[1][1] = 1;
		forab (i, 2, N)
		{
			forab (j, 1, Min(i, S))
			{
				forba (k, i - 1, 1)
				{
					dp[j][i] = Max(dp[j][i], dp[j - 1][k] + judge2(dat[i], p));
					dp[j][i] = Max(dp[j][i], dp[j][k] + judge1(dat[i], p));
				}
			}
		}
		ans = 0;
		forab (i, 0, S)
		{
			forab (j, 1, N)
				ans = Max(ans, dp[i][j]);
		}
		printf("Case #%d: %d\n", cas, ans);
	}
}
int main()
{
	solve();
	return 0;
}