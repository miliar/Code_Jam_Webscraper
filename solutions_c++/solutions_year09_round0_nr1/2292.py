#include <cstdio>
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;


char word[5050][20];
char s[10000];

int main()
{
	freopen("c:\\a2.txt", "r", stdin);
	freopen("c:\\a2sol.txt", "w", stdout);

	int l,d,n;

	scanf("%d %d %d", &l, &d, &n);

	for (int i = 0; i < d; i++)
	{
		scanf("%s", &word[i]);
	}



	for (int i = 1; i <= n; i++)
	{
		scanf("%s", &s);

		int tot = 0;

		for (int j = 0; j < d; j++)
		{
			int cur = 0;

			bool good = true;
			for (int k = 0; k < l && good; k++)
			{
				// word[j][k]
				if (s[cur] == '(')
				{
					cur++;
					bool found = false;
					while (s[cur] != ')')
					{
						if (s[cur] == word[j][k])
						{
							found = true;
						}
						cur++;
					}
					cur++;
					good = found;
						
				}
				else if (s[cur] == word[j][k])
				{
					// ok
					cur++;
				}
				else
				{
					// bad
					good = false;
				}
			}

			tot += good;
		}

		printf("Case #%d: %d\n", i, tot);
	}





	return 0;
}