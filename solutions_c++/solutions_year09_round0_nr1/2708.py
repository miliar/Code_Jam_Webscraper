#include <iostream>
#include <string>

using namespace std;

int L, D, N;
string strs[5000];

int solve(string p)
{
	int a[15][40];
	memset(a, 0, sizeof (a));
	int j = 0;
	bool st = false;
	for( int i = 0 ; i < p.size(); i++)
	{
		if (p[i] == ')')
		{
			st = false;
			j++;
			continue;
		}
		if (p[i] == '(')
		{
			st = true;
			continue;
		}
		a[j][p[i] - 'a'] = 1;
		if (!st) j++;
	}

	int ans = 0;
	for (int i = 0 ; i < D; i++)
	{
		bool ok = true;
		for (int j = 0 ; j < L; j++)
			if (a[j][strs[i][j] - 'a'] == 0)
			{
				ok = false;
				break;
			}
		if (ok) ans++;
	}
	return ans;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> L >> D >> N;
	cin.get();
	char cc[1000];
	for (int i = 0 ; i < D; i ++)
	{
		cin.getline(cc, 500);
		strs[i] = cc;
	}
	for (int i = 0 ; i < N; i ++)
	{
		cin.getline(cc, 500);
		string str = cc;
		cout << "Case #" << i+1 << ": " << solve(str) << endl;
	}
}