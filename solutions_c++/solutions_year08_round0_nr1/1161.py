#include <stdio.h>
#include <memory.h>
#include <string>
#include <map>

using namespace std;

int dynamic[1001][101];
int ans;
int S, Q;
int data[1001];

map<string, int> mapping;

int main()
{
	int t;
	scanf("%d", &t);
	int ti, i, j, k;
	char buf[101];
	for (ti = 1;ti <= t;ti++)
	{
		mapping.clear();
		memset(dynamic, 0x7F, sizeof(dynamic));
		scanf("%d\n", &S);
		for (i = 0;i < S;i++)
		{
			gets(buf);
			string q(buf);
			if (mapping.find(q) == mapping.end())
				mapping.insert(make_pair(q, mapping.size()));
		}
		scanf("%d\n", &Q);
		for (i = 0;i < Q;i++)
		{
			gets(buf);
			string q(buf);
			if (mapping.find(q) == mapping.end())
				data[i] = -1;
			else
				data[i] = mapping[q];
		}

		for (i = 0;i < S;i++)
			dynamic[0][i] = 0;

		for (i = 0;i < Q;i++)
		{
			for (j = 0;j < S;j++)
			{
				for (k = 0;k < S;k++)
				{
					if (k == data[i])
						continue;
					if (dynamic[i + 1][k] > dynamic[i][j] + (j != k))
						dynamic[i + 1][k] = dynamic[i][j] + (j != k);
				}
			}
		}

		ans = 0x7F7F7F7F;
		for (i = 0;i < S;i++)
			if (ans > dynamic[Q][i])
				ans = dynamic[Q][i];

		printf("Case #%d: %d\n", ti, ans);
	}
}