#include <iostream>
#include <string>

using namespace std;

string w = "welcome to code jam";

char buf[65536];
int f[600][25];

int solve(string& s)
{
	int n = s.size();
	int m = w.size();
	memset(f, 0, sizeof(f));

	for (int i=0;i<n;i++)
	{
		for (int j=1;j<m;j++)
		{
			if (i > 0)	f[i][j] = f[i-1][j];
			if (s[i] == w[j])
			{
				f[i][j] += f[i-1][j-1];
				if (f[i][j] > 10000) f[i][j] -= 10000;
			}
		}
		if (i > 0) f[i][0] = f[i-1][0];
		if (s[i] == w[0])
		{
			f[i][0] += 1;
			if (f[i][0] > 10000) f[i][0] -= 10000;
		}
	}
	return f[n-1][m-1];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	cin.getline(buf, sizeof(buf), '\n');
	for (int i=0;i<n;i++)
	{
		cin.getline(buf, sizeof(buf), '\n');
		string s(buf);
		int ans = solve(s);
		cout << "Case #" << (i+1) << ": ";
		if (ans == 0)
		{
			cout << "0000" << endl;
		} else
		{
			int q = ans;
			while (q < 1000)
			{	
				q*=10;
				cout << '0';
			};
			cout << ans << endl;
		}
	}
	fclose(stdout);
	return 0;
}