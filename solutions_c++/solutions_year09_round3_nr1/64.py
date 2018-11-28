#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <iostream>

using namespace std;

int ans[300];
int ans_len;

void mul(int[], int);
void add(int[], int);

int main()
{

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);


	int testcases;
	scanf("%d", &testcases);

	for (int cases = 1; cases <= testcases; cases++)
	{
		char inp[100];
		scanf("%s", inp);

		int app[100];
		int num = 0;

		memset(app, 255, sizeof app);

		for (int i = 0; i < strlen(inp); i++)
		{
			char c = inp[i];
			int tmp;

			if (c >= 'a' && c <= 'z') tmp = c - 'a';
			if (c >= '0' && c <= '9') tmp = 26 + c - '0';

			if (app[tmp] == -1) app[tmp] = num++;
		}

		if (num == 1) num = 2;

		memset(ans, 0, sizeof ans);
		ans_len = 1;

		for (int i = 0; i < strlen(inp); i++)
		{
			mul(ans, num);

			char c = inp[i];
			int tmp;

			if (c >= 'a' && c <= 'z') tmp = c - 'a';
			if (c >= '0' && c <= '9') tmp = 26 + c - '0';

			if (app[tmp] == 0) 
			{
				add(ans, 1);
			}
			else if (app[tmp] > 1)
			{
				add(ans, app[tmp]);
			}
		}

		printf("Case #%d: ", cases);

		for (int i = ans_len - 1; i >= 0; i--)
		{
			printf("%d", ans[i]);
		}
		printf("\n");

	}

	return 0;
}

void mul(int ans[], int num)
{
	for (int i = 0; i < ans_len; i++) ans[i] = ans[i] * num;

	for (int i = 0; i < ans_len - 1; i++)
	{
		ans[i + 1] += ans[i] / 10;
		ans[i] = ans[i] % 10;
	}

	while (ans[ans_len - 1] >= 10)
	{
		ans[ans_len] = ans[ans_len - 1] / 10;
		ans[ans_len - 1] %= 10;
		++ans_len;
	}
}

void add(int ans[], int num)
{
	ans[0] += num;

	for (int i = 0; i < ans_len - 1; i++)
	{
		ans[i + 1] += ans[i] / 10;
		ans[i] = ans[i] % 10;
	}

	while (ans[ans_len - 1] >= 10)
	{
		ans[ans_len] = ans[ans_len - 1] / 10;
		ans[ans_len - 1] %= 10;
		++ans_len;
	}
}
