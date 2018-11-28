#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

char ms[101][105];
string ss[101];

char mq[105];
string sq;

int u[105];


int main()
{
	freopen("c:\\a2.txt", "r", stdin);
	freopen("c:\\a2_out.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int te = 1; te <= t; te++)
	{
		int s, q;

		scanf("%d\n", &s);
		for (int i = 0; i < s; i++)
		{
			int j = 0;
			char c;
			do
			{
				scanf("%c", &c);
				ms[i][j++] = c;
			}
			while (c != 10);
			ms[i][j-1] = 0;
			ss[i] = ms[i];
			//printf("%s\n", ms[i]);
		}

		memset(u,0,sizeof(u));

		int tot = 1;
		int tused = 0;

		scanf("%d\n", &q);
		for (int i = 0; i < q; i++)
		{
			int j = 0;
			char c;
			do
			{
				scanf("%c", &c);
				mq[j++] = c;
			}
			while (c != 10);
			mq[j-1] = 0;
			sq = mq;

			int k = 0;
			while (k < s && sq != ss[k]) k++;
			if (k < s)
			{
				if (u[k] != tot)
				{
					u[k] = tot;
					tused++;
					if (tused == s)
					{
						tused = 1;
						tot++;
						u[k] = tot;

					}
				}
			}

		}

		printf("Case #%d: %d\n", te, tot-1);
	}




	return 0;
}