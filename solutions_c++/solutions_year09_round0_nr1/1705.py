#include<iostream>

#define N 5010

using namespace std;

int l, d, n;
char dic[N][20], str[N];
bool flag[30][30];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d %d %d", &l, &d, &n);
	int i, j;
	for (i = 0; i < d; i++)
		scanf("%s", dic[i]);
	int caseID = 1;
	while (caseID <= n)
	{
		memset(flag, 0, sizeof(flag));
		scanf("%s", str);
		int pos = 0;
		for (i = 0; str[i]; i++)
		{
			if (str[i] >= 'a' && str[i] <= 'z') flag[pos][str[i] - 'a'] = 1;
			else if (str[i] == '(')
			{
				for (j = i + 1; str[j] != ')'; j++)
					flag[pos][str[j] - 'a'] = 1;
				i = j;
			}
			pos++;
		}
		int num = 0;
		for (i = 0; i < d; i++)
		{
			bool exist = 1;
			for (j = 0; j < l; j++)
				if (!flag[j][dic[i][j] - 'a'])
				{
					exist = 0;
					break;
				}
			if (exist) num++;
		}
		printf("Case #%d: ", caseID++);
		printf("%d\n", num);
	}
	return 0;
}