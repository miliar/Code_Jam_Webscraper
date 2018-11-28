#include <iostream>
#include <cstdio>

using namespace std;

bool can[10009]; //!!!!!!!

int main()
{
	int tot=0;

	freopen("c:\\2.txt", "r", stdin);
	freopen("c:\\2out.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int te = 1; te <= t; te++)
	{
		int xx,yy,a;
		scanf("%d %d %d", &xx, &yy, &a);

		bool bad=false;

		int x1=-1,x2=-1,y1=-1,y2=-1;


		if (a>xx*yy)
		{bad=true;
		}
		else
		{

		memset(can,false,sizeof(can));


		for (int x = 0; x <= xx; x++)
		{
			for (int y = 0; y <= yy; y++)
			{
				int p=x*y;
				can[p]=true;
			}
		}
		
		int i = a;
		bool ok=false;

		while (!ok)
		{
			if (can[i] && can[i-a])
			{
				ok=true;

				for (int x = 0; x <= xx; x++)
				{
					for (int y = 0; y <= yy; y++)
					{
						int p=x*y;
						if (p==i)
						{
							x1=x;
							y2=y;
						}
						if (p==i-a)
						{
							x2=x;
							y1=y;
						}
					}
				}

			}
			i++;
			if (!ok && i>xx*yy)
			{
				ok=true;
				bad=true;
			}
		}

		}

	
		if (bad)
		{
			tot++;
			printf("Case #%d: IMPOSSIBLE\n", te);
		}
		else
		{
			printf("Case #%d: 0 0 %d %d %d %d\n", te, x1, y1, x2, y2);
			//printf("%d\n",abs(x1*y2-x2*y1));
			//if (abs(x1*y2-x2*y1)!=a) printf("badddddddddd\n");
		}
	}

	//printf("%d\n",tot);
	return 0;
}
