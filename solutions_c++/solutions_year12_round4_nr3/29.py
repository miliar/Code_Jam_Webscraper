#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);
const int size = 100 * 1000;
const int inf = 1000 * 1000 * 1000;
const double eps = 1e-8;

int ans[size];
int h[size];
bool flag;

bool check(int s, int f)
{
	for (int i = s; i < f; i++)
		if (ans[i] > f)
			return false;
	return true;
}

bool under(int f, int s, int ps, int x)
{
	double hg = h[f] + (h[s] - h[f]) * 1.0 / (s - f) * (ps - f);
	return (x + eps < hg);
}

int getmaxunder(int f, int s, int ps)
{
	if (!flag)
		return 0;
	int l = 0, r = inf;
	if (!under(f, s, ps, l))
	{
		flag = false;
		return 0;
	}
	while (l < r)
	{
		int mid = (l + r + 1) / 2;
		if (under(f, s, ps, mid))
			l = mid;
		else
			r = mid - 1;
	}
	return l;
}

int main() {
	freopen("problem_c2.in", "r", stdin);
	freopen("problem_c2.out", "w", stdout);
	
	int tc;
	cin >> tc;
	for (int t = 0; t < tc; t++)
	{
		int n;
		flag = true;
		cin >> n;
		for (int i = 0; i < n - 1; i++)
		{
			h[i] = n;
			cin >> ans[i];
			ans[i]--;
		}
		for (int i = 0; i < n - 1; i++)
			if (!check(i, ans[i]))
				flag = false;
		if (!flag)
		{
			cout << "Case #" << t + 1 << ": Impossible" << endl;
			continue;
		}
		h[n - 1] = inf;
		h[n] = inf;
		ans[n - 1] = n;
		for (int i = n - 1; i > 0; i--)
		{
			int f = i;
			int s = ans[i];
			for (int j = 0; j < i; j++)
				if (ans[j] == i)
				{
					h[j] = getmaxunder(f, s, j);
					s = i;
					f = j;
				}
		}
		if (flag)
		{
			cout << "Case #" << t + 1 << ":";
			for (int i = 0; i < n; i++)
				cout << " " << h[i];
			cout << endl;
		}
		else
			cout << "Case #" << t + 1 << ": Impossible" << endl;
	}

	return 0;
}