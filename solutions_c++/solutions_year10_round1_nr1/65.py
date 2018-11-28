#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const double EPS = 1e-10;
const double PI = acos(-1.0);
typedef long long int64;
#define MP(x, y) make_pair(x, y)
#define SZ(x) ((int)(x).size())
#define sqr(x) ((x) * (x))
template<class T> T gcd(T a, T b) { for (T c; b; c = a, a = b, b = c % b); return a; }
template<class T> void out(const vector<T> &a) { for (int i = 0; i < SZ(a); ++i) cout << a[i] << " "; cout << endl; }
int countbit(int n) { return n == 0 ? 0 : 1 + countbit(n & (n - 1)); }
const int d4[8][2] = {{0, 1}, {1, 1}, {1, 0}, {1, -1}};
typedef complex<double> point;
inline int dcmp(double x) { return (x > EPS) - (x < -EPS); }
inline double cross(const point &a, const point &b) { return (conj(a) * b).imag(); }
inline double dot(const point &a, const point &b) { return (conj(a) * b).real(); }

const int N = 60;
char a[N][N], b[N][N];

bool valid(int n, int x, int y)
{
	return x >= 0 && x < n && y >= 0 && y < n;
}

int main()
{
	freopen("A-large.in", "r", stdin); freopen("A.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int num = 1; num <= cas; ++num)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%s", a[i]);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				b[j][n - 1 - i] = a[i][j];
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				a[i][j] = '.';
		for (int j = 0; j < n; ++j)
		{
			int k = n - 1;
			for (int i = n - 1; i >= 0; --i)
				if (b[i][j] != '.')
					a[k--][j] = b[i][j];
		}
		bool flagR = false, flagB = false;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
			{
				if (a[i][j] == '.') continue;
				for (int k = 0; k < 4; ++k)
				{
					if (!valid(n, (m - 1) * d4[k][0] + i, (m - 1) * d4[k][1] + j)) continue;
					int u;
					for (u = 1; u < m; ++u)
						if (a[u * d4[k][0] + i][u * d4[k][1] + j] != a[i][j]) break;
					if (u == m)
					{
						if (a[i][j] == 'R') flagR = true;
						else flagB = true;
					}
				}
			}
		printf("Case #%d: ", num);
		if (flagR)
		{
			if (flagB) puts("Both");
			else puts("Red");
		}
		else
		{
			if (flagB) puts("Blue");
			else puts("Neither");
		}
	}
	return 0;
}
