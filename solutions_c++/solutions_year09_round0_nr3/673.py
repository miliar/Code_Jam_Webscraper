#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

const string l = "welcome to code jam";

int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int n, test, sz, c[19][501], s[19][501], i, j;
	string text;

	scanf("%d ", &n);

	for(test = 1; test <= n; ++test)
	{
		memset(c, 0, sizeof(c));
		memset(s, 0, sizeof(s));
		char line[512];
		fgets(line, 512, stdin);
		text = line;
		sz = text.length();
		for(i = 0; i < 19; ++i)
		{
			for(j = 0; j < sz; ++j)
			{
				if(l[i] == text[j])
				{
					if(j != 0 && i != 0)
					{
						c[i][j] = s[i - 1][j - 1];
					}
					else
					{
						if(i == 0)
							c[i][j] = 1;
					}
				}
				if(j != 0)
				{
					s[i][j] = (s[i][j - 1] + c[i][j]) % 10000;
				}
				else
				{
					s[i][j] = c[i][j] % 10000;
				}
			}
		}
		printf("Case #%d: %04d\n", test, s[18][sz - 1]);
	}

	return 0;
}
