#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int area(int x1, int y1, int x2, int y2, int x3, int y3)
{
	return x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2);
}

int main()
{
	int x1, y1, x2, y2, x3, y3;
	int c, C;
	int N, M, A;
	bool find;

	scanf("%d", &C);

	for(c=1;c<=C;c++)
	{
		scanf("%d %d %d", &N, &M, &A);

		find = false;
		/*for(x1=0;x1<=N;x1++)
		{
			for(y1=0;y1<=M;y1++)
			{*/
				for(x2=0;x2<=N;x2++)
				{
					for(y2=0;y2<=M;y2++)
					{
						for(x3=0;x3<=N;x3++)
						{
							for(y3=0;y3<=M;y3++)
							{
								if( area(0,0,x2,y2,x3,y3)==A )
								{
									find = true;
									break;
								}
							}
							if( find ) break;
						}
						if( find ) break;
					}
					if( find ) break;
				}
				/*if( find ) break;
			}
			if( find ) break;
		}*/
		printf("Case #%d: ", c);
		if( find )
			printf("%d %d %d %d %d %d\n", 0,0,x2,y2,x3,y3);
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}
