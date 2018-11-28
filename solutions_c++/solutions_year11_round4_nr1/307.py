#include <iostream>
#include <algorithm>

using namespace std;

const int MAX = 1005;

int w[MAX], p[MAX], len[MAX], ind[MAX];

bool cmp(int a, int b)
{
	return p[a] < p[b];
}

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
		int x, s, r, n;
		double maxt;
		cin >> x >> s >> r >> maxt >> n;
		double ans = 0;
		int l = x;
		for (int i = 0; i < n; i++)
		{
			int b, e;
			cin >> b >> e >> w[i];
			len[i] = e - b;
			l -= len[i];
			p[i] = w[i] + s;
			ans += (double) len[i] / p[i];
			ind[i] = i;
		}
		p[n] = s;
		len[n] = l;
		ind[n] = n;
		ans += (double) l / p[n];
		sort(ind,ind+n+1,cmp);
		double zans = 0;
		for (int i = 0; i <= n; i++)
		{
			double curt = min(maxt,(double)len[ind[i]] / (p[ind[i]] + r - s));
			maxt -= curt;
			zans += curt / p[ind[i]];
		}
		ans -= zans * (r-s);
		cout.setf(ios::fixed, ios::floatfield);
		cout << ans;
    cout << endl;
  }
  return 0;
}