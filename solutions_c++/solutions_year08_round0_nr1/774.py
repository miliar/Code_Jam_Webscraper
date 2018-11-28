#include<iostream>

using namespace std;

char name[110][110];
int query[1100];
bool flag[110];
int n, s, q;

int findID(char str[])
{
	int i;
	for (i = 0; i < s; i++)
		if (strcmp(name[i], str) == 0) break;
	return i;
}

int main()
{
	//freopen("a.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	char temp[110];
	scanf("%d", &n);
	int caseID = 1;
	while (caseID <= n)
	{
		printf("Case #%d: ", caseID++);
		scanf("%d", &s);
		gets(temp);
		int i;
		for (i = 0; i < s; i++)
			gets(name[i]);
		scanf("%d", &q);
		gets(temp);
		for (i = 0; i < q; i++)
		{
			gets(temp);
			query[i] = findID(temp);
		}
		int num = 0, cnt = 0;
		memset(flag, 0, sizeof(flag));
		for (i = 0; i < q; i++)
		{
			if (cnt == s)
			{
				num++;
				memset(flag, 0, sizeof(flag));
				flag[query[i - 1]] = 1;
				cnt = 1;
			}
			if (flag[query[i]] == 0)
			{
				flag[query[i]] = 1;
				cnt++;
			}	
		}
		if (cnt == s) num++;
		printf("%d\n", num);
	}
	return 0;
}