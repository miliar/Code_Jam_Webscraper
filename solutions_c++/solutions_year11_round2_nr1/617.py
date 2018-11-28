#include <iostream>
#include <string>
#include <vector>

using namespace std;

double wp(const string &s, const int ex)
{
	int a = 0, b = 0;
	for (int i = 0; i < s.length(); i++)
	{
		if (i == ex)
			continue;
		if (s[i] == '1')
			a++;
		if (s[i] == '0')
			b++;
	}

	return (double)a / (a + b);
}

int main()
{
	int t, tn = 1;

	cout.setf(ios::fixed);
	cin >> t;

	while (tn <= t)
	{
		int n;
		vector<string> inp;
		vector<double> rwp, owp;
		double tm, ans = 0;

		cin >> n;
		inp.resize(n);
		rwp.resize(n);
		owp.resize(n);

		for (int i = 0; i < n; i++)
		{
			cin >> inp[i];
			rwp[i] = wp(inp[i], -1);
		}

		cout << "Case #" << tn << ":\n";

		int k;
		for (int i = 0; i < n; i++)
		{
			k = 0;
			for (int j = 0; j < n; j++)
			{
				if (inp[i][j] == '.')
					continue;
				k++;
				owp[i] += wp(inp[j], i);
			}
			owp[i] /= k;
		}
		
		for (int i = 0; i < n; i++)
		{
			ans = 0.25 * rwp[i] + 0.5 * owp[i];
			tm = 0;
			k = 0;
			for (int j = 0; j < n; j++)
			{
				if (inp[i][j] == '.')
					continue;
				tm += owp[j];
				k++;
			}
			ans += 0.25 * tm / k;

			cout << ans << endl;
		}

		tn++;
	}

	return 0;
}
