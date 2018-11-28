#include <iostream>

using namespace std;

const int nn = 64;

int test;

char s[nn][nn];
int b[nn];

void solve()
{
	int ans = 0;
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> (s[i]+1);
		b[i] = 0;
		for (int j = 1; j <= n; j++) if (s[i][j] == '1') b[i] = j;
	}
	for (int i = 1; i <= n; i++) cerr << b[i] << ' ';
	cerr << endl;

	for (int i = 1; i <= n; i++)
	{
		if (b[i] > i)
		{
			int k = i + 1;
			while (b[k] > i) k++;
			for (int j = k-1; j >= i; j--)
			{
				ans++;
				swap(b[j], b[j+1]);
			}
		}
	}

	for (int i = 1; i <= n; i++) cerr << b[i] << ' ';
	cerr << endl << endl;

	cout << "Case #" << ++test << ": " << ans << endl;
	cerr << "Case #" << test << ": " << ans << endl;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	cin >> t;
	while (t--)
	solve();
	fclose(stdout);
	return 0;
}