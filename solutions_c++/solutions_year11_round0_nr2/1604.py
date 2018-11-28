#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;


char cmd[5];
int form[26][26];
bool oppose[26][26];
char input[110];
char list[110];



int main()
{
	int t;
	int n, pos;
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &t);
	for (int test = 1; test <= t; ++test)
	{
		for (int i = 0; i < 26; ++i)
			for (int j = 0; j < 26; ++j)
			{
				form[i][j] = -1;
				oppose[i][j] = false;
			}

		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%s", cmd);
			form[cmd[0] - 'A'][cmd[1] - 'A'] = cmd[2] - 'A';
			form[cmd[1] - 'A'][cmd[0] - 'A'] = cmd[2] - 'A';		
		}
		
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%s", cmd);
			oppose[cmd[0] - 'A'][cmd[1] - 'A'] = true;
			oppose[cmd[1] - 'A'][cmd[0] - 'A'] = true;		
		}

		scanf("%d", &n);
		scanf("%s", input);

		int len = 0;
		
		for (int i = 0; i <n; ++i)
		{
			list[len++] = input[i];
			if (len > 1 && form[list[len - 1] - 'A'][list[len - 2] - 'A'] != -1)
			{
				list[len - 2] = form[list[len - 1] - 'A'][list[len - 2] - 'A'] + 'A';
				--len;
			}

			for (int j = 0; j < len - 1; ++j)
				if (oppose[list[j] - 'A'][list[len - 1] - 'A'])
					len = 0;
		}


		printf("Case #%d: [", test);
		for (int i = 0; i < len - 1; ++i)
			printf("%c, ", list[i]);
		if (len - 1 >= 0)
			printf("%c", list[len - 1]);
		printf("]\n");
	}
	return 0;
}