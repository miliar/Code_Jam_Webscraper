#include <cstdio>
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;



int m[10000][20];

char s[10000];

string ww="welcome to code jam";


int main()
{
	const char *w = ww.c_str();

	freopen("c:\\c2.txt", "r", stdin);
	freopen("c:\\c2sol.txt", "w", stdout);

	int n;
	scanf("%d\n", &n);

	for (int t = 1; t <= n; t++)
	{

	memset(m, 0, sizeof(m));

	int len = 0;
	do
	{
		scanf("%c", &s[len++]);
	}
	while (s[len-1] != 10);

	s[len-1]='\0';
	len--;

	for (int i = 0; i < 19; i++)
	{
		m[len][i] = 0;
	}

	for (int k = len-1; k>=0; k--)
	{
		for (int i = 0; i < 19; i++)
		{
			if (s[k] == w[i])
			{
				if (i == 18)
				{
					m[k][i] = (m[k+1][i] + 1) % 10000;
				}
				else
				{
					m[k][i] = (m[k+1][i+1] + m[k+1][i]) % 10000;
				}
			}
			else
			{
				m[k][i] = m[k+1][i];
			}
		}

	}

	printf("Case #%d: %04d\n", t, m[0][0]);


	}





	return 0;
}
