#include <iostream>
#include <string>
#include <string.h>
using namespace std;

int x[64];
int v[64];
int n, k, b, t, tt;

void Solve()
{
	int cnt = 0;
	cin >> n >> k >> b >> t;
	for(int i = 0; i < n; i++)
		cin >> x[i];
	for(int i = 0; i < n; i++)
		cin >> v[i];
	if(k == 0)
	{
		cout << 0 << endl;
		return;
	}
	for(int i = 0; i < n; i++)
		for(int j = i + 1; j < n; j++)
			if(x[i] < x[j])
			{
				tt = x[i];
				x[i] = x[j];
				x[j] = tt;
				tt = v[i];
				v[i] = v[j];
				v[j] = tt;
			}
	int d = 0;
	int p = 0;
	for(int i = 0; i < k; i++)
	{
		while(p < n && x[p] + t * v[p] < b)
		{
			p++;
			d++;
		}
		if(p >= n)
		{
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		p++;
		cnt += d;
	}
	cout << cnt << endl;
}

int main()
{
	freopen("d:\\input.in", "r", stdin);
	freopen("d:\\output.out", "w", stdout);
	int T;
	cin >> T;
	for(int rr = 1; rr <= T; rr++)
	{
		cout << "Case #" << rr << ": ";
		Solve();
	}
	return 0;
}