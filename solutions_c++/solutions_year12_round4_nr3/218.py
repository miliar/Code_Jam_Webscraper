#include <iostream>

using namespace std;

int x[5000];
int h[5000];
bool ok;

void seth(int l, int r, int he, int k)
{
	if (!ok) return;
	h[r] = he;
	int st = l;
	for (int i = l; i < r; i++)
	{
		if (x[i] > r)
		{
			ok = false;
			return;
		}
		if (x[i] == r)
		{
			seth(st,i,he + (r-i) * k - 1, k - 1);
			st = i+1;
		}
	}
}

int main()
{
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ":";
		int n;
		cin >> n;
		ok = true;
		for (int i = 1; i < n; i++)
		{
			cin >> x[i];
		}
		seth(1, n, 0, n);
		if (!ok)
			cout << " Impossible";
		else
		{
			for (int i = 1; i <= n; i++)
				cout << " " << h[i];
		}
    cout << endl;
  }
  return 0;
}