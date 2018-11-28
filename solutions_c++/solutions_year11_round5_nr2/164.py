#include <iostream>
#include <algorithm>

using namespace std;

const int MAX = 1005;

int a[MAX], b[MAX][2];
int queue[MAX];

int main()
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		sort(a,a+n);
		int cnt = 0;
		for (int i = 0; i < n; i++)
		{
			if (i > 0 && (a[i] == a[i-1]))
			{
				b[cnt-1][1]++;
			}
			else
			{
				b[cnt][0] = a[i];
				b[cnt][1] = 1;
				cnt++;
			}
		}
		int ans = n;
		int qb, qe;
		for (int i = 0; i < cnt; i++)
		{
			if (i == 0 || (b[i][0] > b[i-1][0] + 1))
			{
				if (i > 0)
				{
					int cur = b[i-1][0] - queue[qe-1] + 1;
					if (ans > cur) ans = cur;
				}
				qb = 0;
				qe = b[i][1];
				for (int j = 0; j < qe; j++)
				{
					queue[j] = b[i][0];
				}
			}
			else
			{
				for (int j = b[i-1][1]; j < b[i][1]; j++)
				{
					queue[qe++] = b[i][0];
				}
				for (int j = b[i][1]; j < b[i-1][1]; j++)
				{
					//cerr << b[i-1][0] << ' ' << b[i-1][1] << ' ' << b[i][0] << ' ' << b[i][1] << endl;
					int cur = b[i-1][0] - queue[qb] + 1;
					if (ans > cur) ans = cur;
					qb++;
				}
			}
		}
		int cur = b[cnt-1][0] - queue[qe-1] + 1;
		if (ans > cur) ans = cur;
		cout << ans;
    cout << endl;
  }
  return 0;
}