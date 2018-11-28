#include <iostream>
#include <cassert>
#include <cstdio>
using namespace std;

int triarea(int x0,int y0,int x1,int y1,int x2,int y2)
{
	return (x0 * y1 + x1 * y2 + x2 * y0) - (x1 * y0 + x2 * y1 + x0 * y2);
}

int main()
{
	int	C,cs;
	int	N,M,A;
	int	x0,y0,x1,y1,x2,y2;
	bool	found;

	scanf("%d",&C);

	for(cs = 1; cs <= C; cs++)
	{
		scanf("%d %d %d",&N,&M,&A);

		x0 = 0;

		found = false;

		for(y0 = 0; y0 <= M; y0++)
		{
			y1 = 0;

			for(x1 = 0; x1 <= N; x1++)
			{
				for(x2 = 0; x2 <= N; x2++)
				{
					for(y2 = 0; y2 <= M; y2++)
					{
						int area = triarea(x0,y0,x1,y1,x2,y2);			
						if(area < 0) area = -area;

						if(area == A)
						{
							found = true;
							break;
						}
					}

					if(found) break;
				}

				if(found) break;
			}

			if(found) break;
		}

		if(found)	
			printf("Case #%d: %d %d %d %d %d %d\n",cs,x0,y0,x1,y1,x2,y2);
		else
			printf("Case #%d: IMPOSSIBLE\n",cs);
	}

	return 0;
}
