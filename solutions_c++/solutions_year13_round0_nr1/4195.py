#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<list>
#include<algorithm>

using namespace std;

char s[4][5];


int main()
{
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t, i, j, c, n;
	bool foun;
	n = 0;
	scanf("%d", &t);
	while(t--)
	{
		++n;
		foun = false;
		scanf("%s", s[0]);
		scanf("%s", s[1]);
		scanf("%s", s[2]);
		scanf("%s", s[3]);

		for(i=0; i<4; ++i)
		{
			c = 0;
			for(j=0; j<4; ++j)
			{
				if(s[i][j] == '.')
				{
					c = 0;
					break;
				}
				if(s[i][j] == 'X')
				{
					++c;
				}
				else if(s[i][j] == 'O')
				{
					--c;
				}
			}
			if(c >= 3)
			{
				printf("Case #%d: X won\n", n);
				foun = true;
				break;
			}
			else if(c <= -3)
			{
				printf("Case #%d: O won\n", n);
				foun = true;
				break;
			}
		}
		if(foun)
		{
			continue;
		}
		for(i=0; i<4; ++i)
		{
			c = 0;
			for(j=0; j<4; ++j)
			{
				if(s[j][i] == '.')
				{
					c = 0;
					break;
				}
				if(s[j][i] == 'X')
				{
					++c;
				}
				else if(s[j][i] == 'O')
				{
					--c;
				}
			}
			if(c >= 3)
			{
				printf("Case #%d: X won\n", n);
				foun = true;
				break;
			}
			else if(c <= -3)
			{
				printf("Case #%d: O won\n", n);
				foun = true;
				break;
			}
		}
		if(foun)
		{
			continue;
		}
		c = 0;
		for(i=0; i<4; ++i)
		{
			if(s[i][i] == '.')
			{
				c = 0;
				break;
			}
			if(s[i][i] == 'X')
			{
				++c;
			}
			else if(s[i][i] == 'O')
			{
				--c;
			}
		}
		if(c >= 3)
		{
			printf("Case #%d: X won\n", n);
			foun = true;
			continue;
		}
		else if(c <= -3)
		{
			printf("Case #%d: O won\n", n);
			foun = true;
			continue;
		}
		c = 0;
		for(i=0; i<4; ++i)
		{
			if(s[i][3 - i] == '.')
			{
				c = 0;
				break;
			}
			if(s[i][3-i] == 'X')
			{
				++c;
			}
			else if(s[i][3-i] == 'O')
			{
				--c;
			}
		}
		if(c >= 3)
		{
			printf("Case #%d: X won\n", n);
			foun = true;
			continue;
		}
		else if(c <= -3)
		{
			printf("Case #%d: O won\n", n);
			foun = true;
			continue;
		}
		c = 0;
		for(i=0; i<4; ++i)
		{
			for(j=0; j<4; ++j)
			{
				if(s[i][j] == '.')
				{
					++c;
				}
			}
		}
		if(c == 0)
		{
			printf("Case #%d: Draw\n", n);
		}
		else
		{
			printf("Case #%d: Game has not completed\n", n);
		}
	}
	return 0;
}
