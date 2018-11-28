#include <cstdio>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
	int n,N;
	scanf("%d",&N);
	for (n=1;n<=N;n++)
	{
		int X,Y,A;
		int x1,x2,x3,y1,y2,y3,notfound=1;
		int x_1,x_2,x_3,y_1,y_2,y_3;
		int xd1,xd2,yd1,yd2,cross;
		scanf("%d %d %d",&X,&Y,&A);
		x1=0;
		y1=0;
		//for (x1=0;x1<=X&&notfound;x1++)
		for (x2=0;x2<=X&&notfound;x2++)
		for (x3=0;x3<=X&&notfound;x3++)
		//for (y1=0;y1<=Y&&notfound;y1++)
		for (y2=0;y2<=Y&&notfound;y2++)
		for (y3=0;y3<=Y&&notfound;y3++)
		{
			xd1=x2-x1;
			xd2=x3-x1;
			yd1=y2-y1;
			yd2=y3-y1;
			cross=xd1*yd2-yd1*xd2;
			if (cross<0) cross=-cross;
			if (cross==A)
			{
				notfound=0;
				x_1=x1;
				y_1=y1;
				x_2=x2;
				y_2=y2;
				x_3=x3;
				y_3=y3;
			}
		}
		if (notfound)
			printf("Case #%d: IMPOSSIBLE\n",n);
		else
			printf("Case #%d: %d %d %d %d %d %d\n",n,x_1,y_1,x_2,y_2,x_3,y_3);
		fprintf(stderr,"%d\n",n);
	}
  	return 0;
}
