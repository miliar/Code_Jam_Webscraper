#include <stdio.h>
#include <string.h>
#include <map>

using namespace std;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int t, s, used[128], q, vec[1024], i, j, cnt, sol, test;
	map<char*, int> M;
	char engine[128][128], temp[128];

	scanf("%d", &t);

	for(test = 1; test <= t; ++test)
	{
		scanf("%d ", &s);
		for(i = 1; i <= s; ++i)
		{
			fgets(engine[i], 128, stdin);
			scanf(" ");
			M[engine[i]] = i;
		}
		scanf("%d ", &q);
		for(i = 1; i <= q; ++i)
		{
			fgets(temp, 128, stdin);
			for(j = 1; j <= s; ++j)
			{
				if(strcmp(engine[j], temp) == 0)
				{
					vec[i] = M[engine[j]];
					break;
				}
			}
		}

		cnt = 0;
		memset(used, 0, sizeof(used));
		sol = 0;
		for(i = q; i > 0; --i)
		{
			if(!used[vec[i]])
			{
				if(cnt == s - 1)
				{
					++sol;
					memset(used, 0, sizeof(used));
					used[vec[i]] = 1;
					cnt = 1;
				}
				else
				{
					used[vec[i]] = 1;
					++cnt;
				}
			}
		}
		printf("Case #%d: %d\n", test, sol);
		

		M.clear();
	}


	return 0;
}
