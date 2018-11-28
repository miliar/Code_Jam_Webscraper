#include <cstdio>
#include <cstdlib>
#include <list>
#include <iostream>
#include <cmath>
using namespace std;
int len ; 
double get_area(int x1, int y1, int x2, int y2, int x3, int y3)
{
	double area = fabs( (double)x1*(double)y2+ (double)x2 *(double)y3  + (double)x3*(double)y1      -(double)y1*(double)x2  -(double)y2*(double)x3  -(double)y3*(double)x1      ) ;
	area = area/2;
	return area;
}
int main()
{
	int tn;
	const float ERR = 0.00001;
	int casen=1;
	/*
	cout << get_area(0, 0, 0, 1, 1, 1) << endl;
	cout << get_area(1, 1, 2, 3, 5, 8) << endl;
	*/
	scanf("%d",&tn);
	while ( tn--)
	{
		int x1 = 0; 
		int y1 =0 ; 
		int n,m,a; 
		scanf("%d %d %d",&n,&m,&a);
		int chk =0 ; 
		for ( int x2 = 0 ; x2 <=n ; x2++)
		{
			for ( int  y2 = 0 ; y2 <= m; y2++)
			{
				for ( int x3 = 0 ; x3 <= n ; x3++)
				{
					for ( int y3 = 0 ; y3 <= m; y3++)
					{
						double area = get_area(x1,y1,x2,y2,x3,y3);
						double halfa;
						halfa = (double)a / 2.0 ;
						if ( fabs( area - halfa ) < ERR )
						{
							printf("Case #%d: %d %d %d %d %d %d\n",casen++,x1,y1,x2,y2,x3,y3);
							goto brk;
						}
					}
				}
			}
		}
		printf("Case #%d: IMPOSSIBLE\n",casen++);
		brk:
		;
	}
	return 0 ;
}
