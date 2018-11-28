#include<iostream>

#define N 510

using namespace std;

char s1[N], s2[] = "welcome to code jam";
int rec[20];
int num;

void DFS(int pos)
{
	if (!s2[pos])
	{
		num++;
		return;
	}
	int i;
	pos == 0 ? i = 0 : i = rec[pos - 1] + 1;
	for ( ; s1[i]; i++)
	{
		if (s1[i] == s2[pos])
		{
			rec[pos] = i;
			DFS(pos + 1);
		}
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	gets(s1);
	int caseID = 1;
	while (caseID <= t)
	{
		gets(s1);
		num = 0;
		DFS(0);
		printf("Case #%d: %04d\n", caseID++, num);
	}
	return 0;
}