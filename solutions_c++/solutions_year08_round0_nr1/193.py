#include <string>
#include <iostream>

using namespace std;

int a[1200][120];
string s[120];
int q[1200];

int main(void)
{
	int N;
	cin >> N;

	for (int Case = 0; Case < N; Case++)
	{
		int S, Q;
		std::string x;
		cin >> S;
		getline(cin, x);
		for (int i = 0; i < S; i++)
			getline(cin, s[i]);
		cin >> Q;
		getline(cin, x);
		for (int i = 0; i < Q; i++)
		{
			getline(cin, x);
			for (int j = 0; j < S; j++)
				if (x == s[j])
				{
					q[i] = j;
					break;
				}
		}

		if (Q == 0)
		{
			cout << "Case #" << Case + 1 << ": 0" << endl;
			continue;
		}

		for (int j = 0; j < S; j++)
			a[0][j] = (j == q[0]);
		for (int i = 1; i < Q; i++)
			for (int j = 0; j < S; j++)
			{
				int m = 9999;
				for (int k = 0; k < S; k++)
				{
					int c;
					if (k == j)
						c = a[i - 1][k] + 2 * (j == q[i]);
					else
						c = a[i - 1][k] + 1;
					if (c < m)
						m = c;
				}
				a[i][j] = m;
			}

		int ans = 9999;
		for (int j = 0; j < S; j++)
		{
			int c = a[Q - 1][j];
			if (c < ans)
				ans = c;
		}
		
		cout << "Case #" << Case + 1 << ": " << ans << endl;
	}

	return 0;
}
