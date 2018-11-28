#define _USE_MATH_DEFINES  
#define _CRT_SECURE_NO_DEPRECATE  
  
#include <algorithm>  
#include <bitset>  
#include <cassert>  
#include <cmath>  
#include <cstdio>  
#include <cstdlib>  
#include <cstring>   
#include <deque>  
#include <functional>  
#include <iomanip>  
#include <iostream>  
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
  
#pragma comment(linker, "/STACK:64000000")  
  
#define problem "Khaustov"  

typedef long long int64;  
typedef unsigned long long ull;
typedef unsigned char byte;  
typedef pair<int, int> pii;
typedef pair<int64, int64> pii64;
typedef pair<pii64, int64> piii;
typedef pair<int, piii> piiii;
typedef pair<pii, pii> edge;
typedef pair<int64, pii64> shit;
typedef pair<pii64, int> piii64;
typedef pair<double, int> pdi;
typedef pair<pdi, int> pdii;
typedef pair<int, string> pis;
typedef vector<int> vi;  
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<pii> vpii;  
typedef vector<vpii> vvpii;  
typedef vector<string> vs;  
typedef vector<vs> vvs;  
typedef list<int> li;   
  
#define y1 _dsfdsfkn
#define left _dsfdsf
#define right _dfjdsj
#define link _tsu_sux
#define prime 1103
#define eps 1e-7
#define inf 123456789
#define toMod 1000000007LL

int n, m, d, nt;
int res;
string s;
int64 a[1 << 10][1 << 10];
int64 f[1 << 10][1 << 10];
int64 fx[1 << 10][1 << 10];
int64 fy[1 << 10][1 << 10];

inline int64 value(int64 x, int64 val)
{
	return ((2 * x + 1LL) * val);
}

inline int64 getsum(int x1, int y1, int x2, int y2)
{
	int64 res = f[x2][y2];
	if (y1) res -= f[x2][y1 - 1];
	if (x1) res -= f[x1 - 1][y2];
	if (x1 && y1) res += f[x1 - 1][y1 - 1];
	return res;
}

inline int64 getsumx(int x1, int y1, int x2, int y2)
{
	int64 res = fx[x2][y2];
	if (y1) res -= fx[x2][y1 - 1];
	if (x1) res -= fx[x1 - 1][y2];
	if (x1 && y1) res += fx[x1 - 1][y1 - 1];
	return res;
}

inline int64 getsumy(int x1, int y1, int x2, int y2)
{
	int64 res = fy[x2][y2];
	if (y1) res -= fy[x2][y1 - 1];
	if (x1) res -= fy[x1 - 1][y2];
	if (x1 && y1) res += fy[x1 - 1][y1 - 1];
	return res;
}

inline int check(int x1, int y1, int x2, int y2)
{
	int64 sumx = 0;
	int64 sumy = 0;
	int64 mx = (x2 + x1 + 1);
	int64 my = (y2 + y1 + 1);
	sumx = getsumx(x1, y1, x2, y2) - value(x1, a[x1][y2]) - value(x1, a[x1][y1]) - value(x2, a[x2][y2]) - value(x2, a[x2][y1]);
	sumy = getsumy(x1, y1, x2, y2) - value(y2, a[x1][y2]) - value(y1, a[x1][y1]) - value(y2, a[x2][y2]) - value(y1, a[x2][y1]);
	int64 dif = getsum(x1, y1, x2, y2) - a[x1][y1] - a[x2][y1] - a[x1][y2] - a[x2][y2];
	sumx -= mx * dif;
	sumy -= my * dif;
	return (sumx == 0) && (sumy == 0);
}

int main()
{  
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	cin >> nt;
	for (int tn = 1; tn <= nt; ++tn)
	{
		cin >> n >> m >> d;
		for (int i = 0; i < n; ++i)
		{
			cin >> s;
			for (int j = 0; j < m; ++j)
			{
				a[i][j] = (int64)(s[j] - '0') + (int64)d;
			}
		}

		f[0][0] = a[0][0];
		for (int i = 1; i < m; ++i)
			f[0][i] = f[0][i - 1] + a[0][i];
		for (int i = 1; i < n; ++i)
		{
			f[i][0] = f[i - 1][0] + a[i][0];
			for (int j = 1; j < m; ++j)
			{
				f[i][j] = getsum(0, 0, i - 1, j);
				f[i][j] += getsum(i, 0, i, j - 1);
				f[i][j] += a[i][j];
			}
		}

		fx[0][0] = value(0, a[0][0]);
		for (int i = 1; i < m; ++i)
			fx[0][i] = fx[0][i - 1] + value(0, a[0][i]);
		for (int i = 1; i < n; ++i)
		{
			fx[i][0] = fx[i - 1][0] + value(i, a[i][0]);
			for (int j = 1; j < m; ++j)
			{
				fx[i][j] = getsumx(0, 0, i - 1, j);
				fx[i][j] += getsumx(i, 0, i, j - 1);
				fx[i][j] += value(i, a[i][j]);
			}
		}

		fy[0][0] = value(0, a[0][0]);
		for (int i = 1; i < m; ++i)
			fy[0][i] = fy[0][i - 1] + value(i, a[0][i]);
		for (int i = 1; i < n; ++i)
		{
			fy[i][0] = fy[i - 1][0] + value(0, a[i][0]);
			for (int j = 1; j < m; ++j)
			{
				fy[i][j] = getsumy(0, 0, i - 1, j);
				fy[i][j] += getsumy(i, 0, i, j - 1);
				fy[i][j] += value(j, a[i][j]);
			}
		}

		int res = -1;
		for (int K = min(n, m); K > 2; --K)
		{
			for (int i = 0; i + K - 1 < n; ++i)
			{
				if (res != -1) break;
				for (int j = 0; j + K - 1 < m; ++j)
				{
					if (!check(i, j, i + K - 1, j + K - 1)) continue;
					res = K;
					break;
				}
			}
			if (res != -1) break;
		}

		cout << "Case #" << tn << ": ";
		if (res == -1) cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}

    return 0;  
}