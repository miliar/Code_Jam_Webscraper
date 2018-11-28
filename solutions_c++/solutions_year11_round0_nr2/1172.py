#include <iostream>

using namespace std;

#define MAX 128

char cmd[5];
char s[MAX];

int main()
{
	freopen("B-small-attempt4.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int t;
	cin >> t;
	int c, d;
	for (int ti = 1; ti <= t; ++ti)
	{
		cin >> c;
		if (c == 1)
		{
			cin >> cmd[0] >> cmd[1] >> cmd[2];
		}
		cin >> d;
		if (d == 1)
		{
			cin >> cmd[3] >> cmd[4];
		}
		int n;
		cin >> n;
		for (int i = 1; i <= n; ++i)
		{
			cin >> s[i];
		}
		char sta[MAX];
		int top = 0;
		for (int i = 1; i <= n; ++i)
		{
			if (top > 0)
			{
				if ((s[i] == cmd[0] && sta[top] == cmd[1])||(s[i] == cmd[1] && sta[top] == cmd[0]))
				{
					sta[top] = cmd[2];
				}
				else if (s[i] == cmd[3])
				{
					bool flag = false;
					for (int j = top; j >= 1; --j)
					{
						if (sta[j] == cmd[4]) 
						{
							top = j-1;
							flag = true;
							break;
						}
					}
					if (!flag) sta[++top] = s[i]; 
					else top = 0;
				}
				else if (s[i] == cmd[4])
				{
					bool flag = false;
					for (int j = top; j >= 1; --j)
					{
						if (sta[j] == cmd[3]) 
						{
							top = j-1;
							flag = true;
							break;
						}
					}
					if (!flag) sta[++top] = s[i];
					else top = 0; 
				}
				else
				{
					sta[++top] = s[i];
				}
			}
			else
			{
				sta[++top] = s[i];
			}
		}
		printf("Case #%d: [", ti);
		for (int i = 1; i <= top; ++i)
		{
			if (i == 1) printf("%c", sta[i]);
			else printf(", %c", sta[i]);
		}
		printf("]\n");
	}
	return 0;
}

