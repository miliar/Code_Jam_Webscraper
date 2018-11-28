#include <iostream>
#include <algorithm>

using namespace std;

int o[105];
int b[105];
char seq[105];

int sgn(int x)
{
	return (x == 0)
		? 0
		: ((x > 0) ? 1 : -1);
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
    int n;
    cin >> n;
    int io = 0, ib = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> seq[i];
			if (seq[i] == 'O')
				cin >> o[io++];
			else
				cin >> b[ib++];
		}
		o[io] = io ? o[io-1] : 1;
		b[ib] = ib ? b[ib-1] : 1;
		io = 0;
		ib = 0;
		int po = 1, pb = 1;
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			int m = min(abs(po - o[io]), abs(pb - b[ib]));
			ans += m;
			po += m * sgn(o[io] - po);
			pb += m * sgn(b[ib] - pb);
			if (seq[i] == 'O')
			{
				ans += abs(po - o[io]) + 1;
				po = o[io];
				pb += sgn(b[ib] - pb);
				io++;
			}
			else
			{
				ans += abs(pb - b[ib]) + 1;
				pb = b[ib];
				po += sgn(o[io] - po);
				ib++;
			}
		}
		cout << ans;
    cout << endl;
  }
  return 0;
}