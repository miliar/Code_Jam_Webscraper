#include <iostream>
#include <string>
using namespace std;

int area(int x1,int y1,int x2,int y2)
{
	int r=x1*y2-x2*y1;
	if(r<0) r=-r;
	return r;
}
int main()
{
	int T,Ti=0;;
	scanf("%d",&T);
	while(T--)
	{
		Ti++;
		int n,m,a;

		scanf("%d%d%d",&n,&m,&a);

		for(int x1=0;x1<=n;x1++)
		{
			for(int y1=0;y1<=m;y1++)
			{
				for(int x2=0;x2<=n;x2++)
				{
					for(int y2=0;y2<=m;y2++)
					{
						int r=area(x1,y1,x2,y2);
						if(r==a)
						{
							printf("Case #%d: 0 0 %d %d %d %d\n",Ti,x1,y1,x2,y2);
							goto scat;
						}
					}
				}
			}
		}
		printf("Case #%d: IMPOSSIBLE\n",Ti);
scat:;

	}
}