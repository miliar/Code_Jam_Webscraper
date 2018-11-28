#include <stdio.h>
#include <string>
#include <string.h>
#include <map>
using namespace std;

int main(void)
{
	int t, n, m, i, len, cnt, ans, p, test = 0;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d", &t);
	char a[120], b[120];
	int c[102];
	map<string, int> mymap;
	while(t --)
	{
		scanf("%d %d", &n, &m);
		while(n --)
		{
			scanf("%s", a);
			len = strlen(a);
			a[len] = '/';
			cnt = 0;
			for(i = 1;i <= len;i ++)
			{
				if(a[i] == '/')
				{
					b[cnt] = '\0';
					mymap[b] = 1;
				}
				else
					b[cnt ++] = a[i];
			}
		}
		ans = 0;
		while(m --)
		{
			scanf("%s", a);
			len = strlen(a);
			a[len] = '/';
			cnt = 0;
			p = 0;
			for(i = 1;i <= len;i ++)
			{
				if(a[i] == '/')
					c[p ++] = cnt;
				else
					b[cnt ++] = a[i];
			}
			for(i = p - 1;i >= 0;i --)
			{
				b[c[i]] = '\0';
				if(mymap[b])
					break;
				else
				{
					ans ++;
					mymap[b] = 1;
				}
			}
		}
		printf("Case #%d: %d\n", ++ test, ans);
		mymap.clear();
	}
	return 0;
}

