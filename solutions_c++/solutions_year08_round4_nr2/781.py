
#include <iostream>
using namespace std;

int fab(int a)
{
	return a>-a?a:-a;
}
int main()
{
	int i,j,n,m,A,minx,maxx,miny,maxy,T,t;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d", &T);
	for(t = 1; t <= T; t ++)
	{
		scanf("%d %d %d",&n,&m,&A);
		printf("Case #%d:", t);
		for (minx = 0; minx <= n; minx ++)
		{
			for (maxx = 0; maxx <= n; maxx ++)
			{
				for (miny = 0; miny <= m; miny ++)
				{
					for (maxy = 0; maxy <= m; maxy ++)
					{
						if (fab(minx * maxy - maxx * miny) == A)
						{
							printf(" 0 0 %d %d %d %d\n", minx, miny, maxx, maxy);
							goto end;
						}
					}
				}
			}
		}
		printf(" IMPOSSIBLE\n");
end:	;
	}
	return 0;
}