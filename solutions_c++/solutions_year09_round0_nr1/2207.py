#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int l, d, n;
string s[10000];
string t;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> l >> d >> n;

	for (int i = 0; i < d; i++)
		cin >> s[i];

	for (int i = 0; i < n; i++)
	{
		cin >> t;
		int k = t.size();
		int res = 0;

		for (int j = 0; j < d; j++)
		{
			int uk1 = 0;
			bool q = true;
			int sost = 0;
			int uk2 = 0;

			while (uk1 < k)
			{
				if (t[uk1] == '(')
				{
					uk1++;
					bool q1 = false;
					while (t[uk1] != ')')
					{
						if (t[uk1] == s[j][uk2])
							q1 = true;

						uk1++;
					}
					if (!q1)
					{
						q = false;
						break;
					}
				}
				else
				{
					if (t[uk1] != s[j][uk2])
					{
						q = false;
						break;
					}
				}
				uk1++;
				uk2++;
			}

			if (q)
				res++;
		}

		cout << "Case #" << (i+1) << ": " << res << endl;
	}

	return 0;
}