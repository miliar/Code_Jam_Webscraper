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

const int N = 100;
int a[N][N], b[N][N];

void print(int a[N][N])
{
	for (int i = 0; i < 6; ++i)
	{
		for (int j = 0; j < 6; ++j)
			printf("%d", a[i][j]);
		puts("");
	}
}

int main()
{
	freopen("B.in", "r", stdin); freopen("B.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int num = 1; num <= cas; ++num)
	{
		int m;
		scanf("%d", &m);
		memset(a, 0, sizeof(a));
		while (m--)
		{
			int X1, X2, Y1, Y2;
			scanf("%d %d %d %d", &Y1, &X1, &Y2, &X2);
			--X1, --X2, --Y1, --Y2;
			if (X1 > X2) swap(X1, X2);
			if (Y1 > Y2) swap(Y1, Y2);
			for (int i = X1; i <= X2; ++i)
				for (int j = Y1; j <= Y2; ++j)
					a[i][j] = 1;
		}
		int ret = 1;
		for (; ; ++ret)
		{
			int cnt = 0;
			for (int i = 0; i < N; ++i)
				for (int j = 0; j < N; ++j)
				{
					if (a[i][j] == 1)
					{
						if (!(i - 1 >= 0 && a[i - 1][j] > 0 || j - 1 >= 0 && a[i][j - 1] > 0))
							b[i][j] = 0;
						else b[i][j] = 1, ++cnt;
					}
					else
					{
						if (i - 1 >= 0 && a[i - 1][j] > 0 && j - 1 >= 0 && a[i][j - 1] > 0)
							b[i][j] = 1, ++cnt;
						else b[i][j] = 0;
					}
				}
			memcpy(a, b, sizeof(a));
			if (cnt == 0) break;
		}
		printf("Case #%d: %d\n", num, ret);
//		fprintf(stderr, "Case #%d: %d\n", num, ret);
	}
	return 0;
}
