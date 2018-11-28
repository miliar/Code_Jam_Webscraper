#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

int a[30000];
int r[110][110];

void step(int lef, int rig)
{
	if (lef > rig)
		return;
	if (r[lef][rig])
		return;
	if (rig == lef)
	{
		//r[lef][rig] = a[rig + 1] - a[lef - 1] - 2;
		r[lef][rig] = a[rig + 1] - a[lef - 1] - 2;
		return;
	}
	int i;
	int res = 2000000000;
	for (i = lef; i <= rig; i++)
	{
		step(lef, i - 1);
		step(i + 1, rig);
		int var = r[lef][i - 1] + r[i + 1][rig];
		res = min(res, var);
	}
	r[lef][rig] = res + a[rig + 1] - a[lef - 1] - 2;
}

void solve(void)
{
	int len, n;
	cin >> len >> n;
	int i;
	for (i = 1; i <= n; i++)
	{
		cin >> a[i];
	}
	a[0] = 0;
	a[n + 1] = len + 1;
	memset(r, 0, sizeof(r));
	step(1, n);
	cout << r[1][n];
}

int main (void) 
{
	//freopen("input3.txt", "r", stdin);
	//freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("output3.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}