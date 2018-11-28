#include <stdio.h>
#include <string.h>

#define FOR(i, n) for(int i = 0; i < n; i++)

struct Servers
{
	bool v;
	char arr[101];
};

Servers servers[100];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n, s, q;
	char query[101];
	scanf("%d", &n);
	FOR(i, n)
	{
		int ans = 0;
		scanf("%d\n", &s);
		FOR(j, s)
		{
			gets(servers[j].arr);
			servers[j].v = false;
		}
		scanf("%d\n", &q);
		FOR(j, q)
		{
			gets(query);
			FOR(k, s)
				if(strcmp(query, servers[k].arr) == 0)
					servers[k].v = true;
			bool flag = false;
			FOR(k, s)
				if(servers[k].v == false)
					flag = true;
			if(!flag)
			{
				FOR(k, s)
					if(strcmp(query, servers[k].arr) != 0)
						servers[k].v = false;
				ans++;
			}
		}
		printf("Case #%d: %d\n",i+1, ans);
	}
	return 0;
}