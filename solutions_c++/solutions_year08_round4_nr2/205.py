#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<ctime>

using namespace std;

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))

int area(int x1,int y1,int x2,int y2,int x3,int y3)
{
	if(x1==x2 && y1==y2) return 0;
	if(x1==x3 && y1==y3) return 0;
	if(x3==x2 && y3==y2) return 0;

	return x1*(y2-y3) +  x2*(y3-y1)  + x3*(y1-y2) ;

}

int main()
{
	int i,j,k,tests,cs=0;

	//freopen("C:\\.in","r",stdin);
	freopen("C:\\Bsmall.txt","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		int R,C,A,sol=0;
		int x,y,a;
		int pts[5][2];

		scanf("%d %d %d",&R,&C,&A);

		pts[0][0]=0,pts[0][1]=0;
		pts[1][0]=R,pts[1][1]=0;
		pts[2][0]=0,pts[2][1]=C;
		pts[3][0]=R,pts[3][1]=C;



		printf("Case #%d: ",++cs);
		for(i=0;i<=R && !sol;i++)
			for(j=0;j<=C && !sol;j++)
				for(x=i;x<=R && !sol;x++)
					for(y=0;y<=C && !sol;y++)
						for(k=0;k<4 && !sol;k++)
						{
							a=area(pts[k][0],pts[k][1],i,j,x,y);
							a=abs(a);

						//	printf("%d ",a);
							if(a==A)
							{
								sol=1;
								
								printf("%d %d %d %d %d %d\n",pts[k][0],pts[k][1],
									i,j,x,y);

							}
						}
					if(!sol)
						printf("IMPOSSIBLE\n");
					
		

	}
	return 0;
}