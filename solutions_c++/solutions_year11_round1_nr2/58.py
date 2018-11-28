#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#define maxL 20
#define maxN 20000
#define maxC 30

using namespace std;

int N, M;
char list[maxC];
char word[maxN][maxL];
int len[maxN];
bool contain[maxN][256];
int r[maxN];
int cur[maxN];
bool flag[maxN];
int ans = 0, ansp;

bool cmp(int left, int right)
{
	return cur[left] < cur[right];
}

void dfs(int lev, int as, int left, int right)
{
//	cout << lev << " " << as << " " << left << " " << right << " " << list[lev];
//	for (int i = left; i <= right; i++)
//		cout << " " << word[r[i]];
//	cout << endl;
	if (left == right)
	{
		if (as > ans || (as == ans && r[left] < ansp))
		{
			ans = as;
			ansp = r[left];
		}
	}
	else
	{
		bool has = false;
		for (int i = left; i <= right; i++)
		{
			int w = r[i], t = cur[w];
			flag[w] = false;
			for (int j = 0; j < len[w]; j++)
				if (word[w][j] == list[lev])
				{
					flag[w] = true;
					has = true;
					cur[w] |= 1 << j;
				}
		}
		sort(&r[left], &r[right + 1], cmp);
		int j = left;
		for (int i = left + 1; i <= right + 1; i++)
			if (i == right + 1 || cur[r[i]] != cur[r[j]])
			{
//				cout << (flag[r[j]]? "true": "false") << " ";
				if (flag[r[j]] || !has)
					dfs(lev + 1, as, j, i - 1);
				else
					dfs(lev + 1, as + 1, j, i - 1);
				j = i;
			}
	}
}

int main()
{
	int T;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		cin >> N >> M;
		for (int i = 0; i < N; i++)
		{
			cin >> word[i];
			len[i] = strlen(word[i]);
		}
		printf("Case #%d:", z);
		for (int q = 0; q < M; q++)
		{
			ans = 0;
			cin >> list;
			for (int i = 0; i < N; i++)
			{
				cur[i] = 1 << len[i];
				r[i] = i;
			}
			sort(&r[0], &r[N], cmp);
			int j = 0;
			for (int i = 1; i <= N; i++)
				if (i == N || cur[r[i]] != cur[r[j]])
				{
					dfs(0, 0, j, i - 1);
					j = i;
				}
			printf(" %s", word[ansp]);
		}
		puts("");
	}
	return 0;
}
