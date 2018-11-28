#include <iostream>
#include <algorithm>

using namespace std;


int area2(int p1x,int p1y,int p2x,int p2y,int p3x,int p3y)
{
	return abs(p1x*p2y+p2x*p3y+p3x*p1y-p1y*p2x-p2y*p3x-p3y*p1x);
}


int main()
{
	int C;
	cin >> C;
	for (int ca=0; ca<C; ca++)
	{
		int n, m, a;
		
		cin >> n >> m >> a;
		printf("Case #%d: ", ca+1);
		//(x1, 0), (0, y2), (x3, y3)
		for (int x1=0; x1<=n; x1++)
			for (int y2=0; y2<=m; y2++)
				for (int x3=0; x3<=n; x3++)
					for (int y3=0; y3<=m; y3++)
						if (area2(x1,0,0,y2,x3,y3) == a)
						{
							printf("%d %d %d %d %d %d\n", x1,0,0,y2,x3,y3);
							goto done;
						}
imp:
		printf("IMPOSSIBLE\n");							
done:
		;
	}
}
