#include <iostream>
#include <string>

using namespace std;
int TT;
int a[10];
int u[10];
int Q, P;
int mn;

void doP(int d)
{
	if (d > Q)
	{
		bool x[100];
		memset(x, false, sizeof (x));
		int ans = 0;
		for (int i = 0 ; i  < Q; i++)
		{
			x[a[u[i]-1]] = true;
			for (int j = a[u[i]-1] - 1; j >= 0; j--)
			{
				if (x[j]) break;
				ans++;
			}
			for (int j = a[u[i]-1] + 1; j < P; j++)
			{
				if (x[j]) break;
				ans++;
			}
		}
		mn = min(mn, ans);
	}
	else
	{
		for (int i = 0; i < Q; i++)
			if (u[i] == 0)
			{
				u[i] = d;
				doP(d + 1);
				u[i] = 0;
			}
	}
}
int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	cin >> TT;
	for (int I = 0 ; I < TT; I++)
	{
		mn = 2000000000;
		cin >> P >> Q;
		memset(u, 0, sizeof (u));
		for (int i = 0 ; i < Q; i++)
		{
			cin >> a[i];
			a[i]--;
		}
		doP(1);
		cout << "Case #" << I+1 << ": " << mn << endl;
	}

	return 0;
}