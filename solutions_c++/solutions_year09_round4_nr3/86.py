#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <string>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <bitset>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;
#define dbg(x) {cerr << #x << " " << x << endl;}
#define dbgv(x) {cout << "{ "; for(int i = 0; i < (x).size(); ++i) cout << " " << (x)[i]; cout << " }\n";}
const double eps = 1e-9;
const LD pi = 3.1415926535897932384626433832795;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define iss istringstream
#define oss ostringstream


LL vect(LL ax, LL ay, LL bx, LL by, LL cx, LL cy)
{
	return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
}

bool intersect(int ax, int ay, int bx, int by, int cx, int cy, int dx, int dy)
{
	LL v11 = vect(ax, ay, bx, by, cx, cy);
	LL v12 = vect(ax, ay, bx, by, dx, dy);
	LL v21 = vect(cx, cy, dx, dy, ax, ay);
	LL v22 = vect(cx, cy, dx, dy, bx, by);
	if((v11|v12|v21|v22) == 0)
	{
		if(ax > bx) swap(ax, bx);
		if(ay > by) swap(ay, by);
		if(cx > dx) swap(cx, dx);
		if(cy > dy) swap(cy, dy);
		return bx >= cx && dx >= ax && by >= cy && dy >= ay;
	}
	
	return ((v11 <= 0 && v12 >= 0) || (v11 >= 0 && v12 <= 0)) &&
		((v21 <= 0 && v22 >= 0) || (v21 >= 0 && v22 <= 0));
}
/*
bool ok(vector<int> &a, vector<int> &b, int k)
{
	bool fl = false;
	for(int i = 0; i + 1 < k; ++i)
		for(int j = 0; j + 1 < k; ++j)

}
*/
int cc[1<<16];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cc[0] = 0;
	for(int i = 1; i < (1 << 16); ++i)
		cc[i] = cc[i >> 1] + (i & 1);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int n, k; scanf("%d%d", &n, &k);
		vector< vector<int> > p(n, vector<int>(k, 0));
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < k; ++j)
				scanf("%d", &p[i][j]);
		vector< vector<int> > g(n, vector<int>(n, 0));
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < n; ++j) if(i != j)
			{
				bool fl = false;
				for(int w1 = 0; w1 + 1 < k; ++w1)
					for(int w2 = 0; w2 + 1 < k; ++w2)
						fl |= intersect(w1, p[i][w1], w1 + 1, p[i][w1 + 1], w2, p[j][w2], w2 + 1, p[j][w2 + 1]);
				if(fl)
					g[i][j] = 0;
				else
					g[i][j] = 1;
			
					
			}
		vector<bool> d(1 << n, 0);
		d[0] = true;
		for(int i = 1; i < (1 << n); ++i)
		{
			int p = 0;
			for(int j = 0; j < n; ++j)
				if(i & (1 << j))
					p = j;
			int ni = i ^ (1 << p);
			if(!d[ni]) continue;
			bool fl = true;
			for(int j = 0; j < n; ++j)
				if(ni & (1 << j))
					if(!g[p][j])
					{
						fl = false;
						break;
					}
			d[i] = fl;
		}
		vector<int> dp(1 << n, n);
		dp[0] = 0;
		for(int i = 1; i < (1 << n); ++i)
		{
			if(cc[i] == 1)
			{
				dp[i] = 1;
				continue;
			}
			for(int j = i; j > 0; j = (j - 1) & i)
			{
				int r1, r2;
				if(d[i ^ j]) r1 = (i^j)!=0; else r1 = dp[i ^ j];
				if(d[j]) r2 = j!=0; else r2 = dp[j];
				
				dp[i] = min(dp[i], r1 + r2);
			}
		}
		cout << "Case #" << z + 1 << ": " << dp.back() << endl;
	}

	return 0;
}
