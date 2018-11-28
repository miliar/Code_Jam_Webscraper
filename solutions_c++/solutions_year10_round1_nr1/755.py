#include <iostream>
#include <cstring>
using namespace std;

const int MAXN = 100;

char s[MAXN][MAXN];
char t[MAXN][MAXN];


bool Find(char s[MAXN][MAXN], int n, int k, char c)
{
	int ans, I, J;
	for (int i = 0; i < n; ++ i)
		for (int j = 0; j < n; ++ j)
		{
			ans = 0;
			I = i;
			J = j;
			while (s[I][J] == c)
			{
				ans ++;
				++ J;
			}

			if (ans >= k)
				return true;

			ans = 0;
			I = i;
			J = j;
			while (s[I][J] == c)
			{
				ans ++;
				++ J;
				++ I;
			}

			if (ans >= k)
				return true;

			ans = 0;
			I = i;
			J = j;
			
			while (s[I][J] == c)
			{
				ans ++;
				-- J;
				++ I;
			}

			if (ans >= k)
				return true;

			ans = 0;
			I = i;
			J = j;

			while (s[I][J] == c)
			{
				ans ++;
				++ I;
			}
			

			if (ans >= k)
				return true;
		}

	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;


	for (int tt = 1; tt <= T; ++ tt)
	{
		int n,k;
		cin >> n >> k;

		for (int i = 0; i < n; ++ i)
		{
			scanf("%s", s[i]);
		}

		memset(t, '.', sizeof(t));

		for (int i = 0; i < n; ++ i)
		{
			for (int j = 0; j < n; ++ j)
				t[i][j] = s[n - j - 1][i];
		}
		for (int kof = 0; kof < n + 10; ++ kof)
			for (int i = n - 1; i > 0; -- i)
				for (int j = 0; j < n ; ++ j)
					if (t[i][j] == '.')
					{
						t[i][j] = t[i - 1][j];
						t[i - 1][j] = '.';
					}

	

		bool R = Find(t, n, k, 'R');
		bool B = Find(t, n, k, 'B');

		cout << "Case #" << tt << ": ";


		if (R && B)
			cout << "Both\n";
		else if (R)
			cout << "Red\n";
		else if (B)
			cout << "Blue\n";
		else
			cout << "Neither\n";

	}

	return 0;
}