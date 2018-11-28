#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 10000;
const string ptn = "welcome to code jam";

vector<int> a, b;

int main()
{
	int n, cn, i, j, k, ans;
	string t;

	cin >> n;
	getline(cin, t);

	for (cn = 1; cn <= n; cn++)
	{
		getline(cin, t);

		a.assign(t.length(), 0);

		for (i = 0; i < t.length(); i++)
			if (t[i] == ptn[0])
				a[i]++;

		for (i = 1; i < ptn.length(); i++)
		{
			b.assign(t.length(), 0);

			for (j = 0; j < t.length(); j++)
				if (t[j] == ptn[i])
				{
					for (k = 0; k < j; k++)
						b[j] += a[k];
					b[j] %= MOD;
				}
			a = b;
		}

		ans = 0;
		for (i = 0; i < t.length(); i++)
			ans += a[i];

		printf("Case #%d: %04d\n", cn, ans % MOD);
	}

	return 0;
}
