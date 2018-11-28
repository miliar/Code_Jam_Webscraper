#include <iostream>
#include <fstream>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <cstring>

#define all(x) (x).begin(),(x).end()

using namespace std;

const int nmax = 1e5;

int n, D;
int d[nmax];
int l[nmax];
int H[nmax];
bool upd[nmax];


void solve(int t)
{
	printf("Case #%d: ", t);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> d[i] >> l[i];
		H[i] = 0;
		upd[i] = 0;
	}
	cin >> D;
	queue<int> q;
	H[0] = d[0];
	q.push(0);
	while (q.size() > 0)
	{
		int v = q.front();
		q.pop();
		if (upd[v]) continue;
		upd[v] = 1;
		if (d[v] + H[v] >= D)
		{
			cout << "YES" << endl;
			return;
		}
		int x = v;
		while (x < n && d[x] - d[v] <= H[v])
		{
			int nh = min(d[x] - d[v], l[x]);
			if (nh > H[x])
			{
				H[x] = nh;
				q.push(x);
				upd[x] = 0;
			}
			x ++;
		}
		while (x > 0 && d[v] - d[x] <= H[v])
		{
			int nh = min(d[v] - d[x], l[x]);
			if (nh > H[x])
			{
				H[x] = nh;
				q.push(x);
				upd[x] = 0;
			}
			x --;
		}
	}
	cout << "NO" << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i ++)
		solve(i + 1);
	return 0;
};
