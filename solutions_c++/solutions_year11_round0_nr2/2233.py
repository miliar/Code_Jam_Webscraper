#include<iostream>
#include<vector>
#include<cstdio>
#include<cstring>

#define Max 105
#define cMax 127

using namespace std;

vector<char> q;
char str[Max];

int ct[cMax];

char tab[cMax][cMax];
char bong[Max][2];


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int z, zi, n, i, j, m;
	int ca, cb, cc, tc;

	scanf("%d", &z);

	for(zi=1;zi<=z;zi++)
	{
		memset(tab, 0, sizeof(tab));
		q.clear();
		memset(ct, 0, sizeof(ct));

		scanf("%d", &n);

		while(n--)
		{
			scanf("%s", str);
			ca = str[0], cb = str[1], cc = str[2];

			tab[ca][cb] = tab[cb][ca] = cc;
		}

		scanf("%d", &m);

		for(i=0;i<m;i++)
			scanf("%s", bong[i]);

		scanf("%d %s", &n, str);


		for(i=0;i<n;i++)
		{
			tc = str[i];

			while(!q.empty())
			{
				cb = q.back();

				if(!tab[cb][tc])
					break;

				tc = tab[cb][tc];

				ct[cb]--;
				q.pop_back();
			}

			ct[tc]++;
			q.push_back(tc);

			for(j=0;j<m;j++)
			{
				ca = bong[j][0];
				cb = bong[j][1];

				if(ct[ca] && ct[cb])
				{
					memset(ct, 0, sizeof(ct));
					q.clear();
				}
			}
		}


		printf("Case #%d: [", zi);

		for(i=0;i<q.size();i++)
		{
			if(i)
				printf(", ");

			printf("%c", q[i]);
		}

		printf("]\n");

	}
}
