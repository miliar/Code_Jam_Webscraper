#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <memory>
#include <string>
#include <set>
#include <map>
#include <queue>
using namespace std;
int main(void)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,q,n,m;
	char c;
	scanf("%d",&t);
	for (q = 1; q <= t; q++)
	{
		scanf("%d%d",&n,&m);
		scanf("%c",&c);
		char a[100][100];
		memset(a,'.',sizeof(a));
		for (int i = 0 ; i < n; i++)
		{
			for (int j = 0; j < m; j++)
				scanf("%c",&a[i][j]);
			scanf("%c",&c);
		}
		bool b[100][100];
		char c[100][100];
		memset(c,'.',sizeof(c));
		memset(b,false,sizeof(b));
		bool ok = true;
		for (int i = 0 ; i < n; i++)
		{
			for (int j = 0 ; j < m; j++)
				if ((a[i][j] == '#') && (!b[i][j]))
				{
					c[i][j] = '/';
					b[i][j] = true;
					if (a[i][j+1] == '#')
					{
						c[i][j+1] = '\\';
						b[i][j+1] = true;
					} else
					{
						ok = false;
						break;
					}
					if (a[i+1][j] == '#')
					{
						c[i+1][j] = '\\';
						b[i+1][j] = true;
					} else
					{
						ok = false;
						break;
					}
					if (a[i+1][j+1] == '#')
					{
						c[i+1][j+1] = '/';
						b[i+1][j+1] = true;
					} else
					{
						ok = false;
						break;
					}
				}
		}
		printf("Case #%d:\n",q);
		if (ok)
		for (int i = 0 ; i < n; i++)
		{
			for (int j =0 ; j < m; j++)
				printf("%c",c[i][j]);
			printf("\n");
		} else
			printf("Impossible\n");
	}
	return 0;
}