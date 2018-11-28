#include <iostream>
#include <vector>
#include <string>

using namespace std;
typedef vector <int> vi;
int n, ans;
vi a;

bool _swap()
{
	int i = 0;
	while (i != a.size())
	{
		if (a[i] > i)
			break;
		i++;
	}

	if (i == a.size())
		return false;

	int j = i + 1;
	while (j != a.size())
	{
		if (a[j] <= i)
			break;
		j++;
	}

	vi b = a;
	b[i] = a[j];
	b[i+1] = a[i];
	for (int t = i + 2; t <= j; t++)
		b[t] = a[t-1];

	a.swap(b);

	ans += j - i;

	return true;
}

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int K;
	cin >> K;

	for (int k = 0; k < K; k++)
	{
		ans = 0;
		a.clear();

		cin >> n;

		for (int j = 0; j < n; j++)
		{
			int y = 0;
			string s;
			cin >> s;

			for (int i = 0; i < n; i++)
				if (s[i] == '1')
					y = i;

			a.push_back(y);
		}

		while (_swap());

		cout << "Case #" << k + 1 << ": " << ans << endl;
	}
	return 0;
}