#include <iostream>
#include <iomanip>

using namespace std;

#define maxN (100 + 10)

int n;
char a[maxN][maxN];
double wp[maxN], owp[maxN], oowp[maxN], swp[maxN][maxN];

void solve ()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int sum = 0, t = 0;
		for (int j = 0; j < n; j++)
		{
			cin >> a[i][j];
			sum += (a[i][j] == '1');
			t += (a[i][j] == '1' || a[i][j] == '0');
		}
		wp[i] = double (sum) / double (t);
		for (int j = 0; j < n; j++)
		{
			if (a[i][j] == '1')
				swp[i][j] = double (sum - 1) / double (t - 1);
			if (a[i][j] == '0')
				swp[i][j] = double (sum) / double (t - 1);
		}
	}

	for (int i = 0; i < n; i++)
	{
		double sum = 0; int t = 0;
		for (int j = 0; j < n; j++)
		{
			if (a[i][j] == '1' || a[i][j] == '0')
				sum += swp[j][i];
			t += (a[i][j] == '1' || a[i][j] == '0');
		}
		owp[i] = sum / (double) t;
	}
	for (int i = 0; i < n; i++)
	{
		double sum = 0; int t = 0;
		for (int j = 0; j < n; j++)
		{
			if (a[i][j] == '1' || a[i][j] == '0')
				sum += owp[j];
			t += (a[i][j] == '1' || a[i][j] == '0');
		}
		oowp[i] = sum / (double) t;
	}

	for (int i = 0; i < n; i++)
		cerr << wp[i] << ' ' << owp[i] << ' ' << oowp[i] << endl;
	for (int i = 0; i < n; i++)
		cout << fixed << setprecision (6) << (wp[i] + 2 * owp[i] + oowp[i]) / 4.0 << endl;
}

int main()
{
	int t; cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ":" << endl;
		solve();
	}

	return 0;
}
