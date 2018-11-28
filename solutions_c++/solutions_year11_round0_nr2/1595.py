#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

string ans;
char com[100][5],opp[100][5];
char str[200];
int c, d, n;
void init()
{
	scanf("%d", &c);
	for(int i = 0; i < c; i++)
		scanf("%s", com[i]);

	scanf("%d", &d);
	for(int i = 0; i < d; i++)
		scanf("%s", opp[i]);
	scanf("%d", &n);
	scanf("%s", str);
}

void process()
{
	ans = "";
	int flag;
	for (int k = 0; k < n; k++)
	{
		ans += str[k];
		flag = 0;
		int i;
		for (i = 0; i < c; i++)
			if (ans.length() >= 2)
				if (((ans[ans.length() - 1] == com[i][0]) && (ans[ans.length() - 2] == com[i][1])) ||
					((ans[ans.length() - 1] == com[i][1]) && (ans[ans.length() - 2] == com[i][0])))
				{
					flag = 1;
					break;
				}

		if(flag)
		{
			ans = ans.substr(0, ans.length() - 2) + com[i][2];
			continue;
		}

		flag = 0;
		for (int i = 0; i < ans.length() - 1; i++)
		{
			for (int j = 0; j < d; j++)
				if (ans.length() >= 2)
					if (((ans[ans.length() - 1] == opp[j][0]) && (ans[i] == opp[j][1])) ||
						((ans[ans.length() - 1] == opp[j][1]) && (ans[i] == opp[j][0])))
					{
						flag = 1;
						break;
					}
			if (flag)
				break;
		}

		if (flag)
		{
			ans = "";
			continue;
		}
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int testCase = 0; testCase < t; testCase++)
	{
		init();
		process();
		printf("Case #%d: [", testCase + 1);
		for (int i = 0; i < ans.length(); i++)
			if(i == 0)
				printf("%c", ans[i]);
			else
				printf(", %c", ans[i]);
		printf("]\n");
	}
	return 0;
}