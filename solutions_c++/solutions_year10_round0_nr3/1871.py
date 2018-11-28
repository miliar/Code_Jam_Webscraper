#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#define file "c"
#define ldb long double
#define LL long long
const ldb eps = 1e-9;
const int INF = 1 << 30;
const LL LINF = 1ll << 60;
const ldb LDINF = 1e+70;
using namespace std;


int R, k, n, g[1010];
LL res[2010];
int was[2010];


void Load()
{
	cin >> R >> k >> n;
	int i;
	for (i = 0; i < n; i++)
	{
		cin >> g[i];	
	}
}

void Solve(int Test)
{
	cout << "Case #" << Test << ": ";
	int i, j;
	for (i = 0; i < n; i++) was[i] = 0;
	int cur = 0;
	LL sum = 0;
	res[0] = 0;
	for (i = 1; i <= R; i++)
	{
		sum = 0ll;
		for (j = 0; j < n; j++)
		{
			sum += (LL) g[(cur + j) % n];
			if (sum > k)
			{
				sum -= (LL) g[(cur + j) % n];
				break;
			}
		}   
		
		res[i] = res[i-1] + sum;		 
		if (was[cur] != 0) break;
		else was[cur] = i;
		//cerr << cur << " "; //<< res[i] << " _ " << was[cur] << " j = " << j << " ";
		cur += j;
		cur %= n;
	}
//	cerr << "\n";
	if (i > R)
	{
		cout << res[R] << "\n";
	}
	else
	{
		int prev = was[cur];
		int cycle = i - was[cur];
		//cout << "  pred = " << prev << " cycle = " << cycle << " i = " << i << " was[" << cur << "] = " << was[cur] << " ";
		cout << ((LL)R - prev) / (LL)cycle * (res[i] - res[prev]) + res[((R - prev) % cycle) + prev] << "\n";
	}
}

int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	int i;
	for (i = 1; i <= T; i++)
	{
		Load();
		Solve(i);
	}
	return 0;
}