//B

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
using namespace std;

#define LD long double
#define EPS 1e-9

int main()
{
	//files
	freopen("a.in","r",stdin);
	freopen("b.out","w",stdout);
	//vars
	int t,T;
	int sy,sx,w,y,x,a,b,ans;
	char grid[15][15];
	LD cy,cx,vy,vx;
	//testcase loop
	scanf("%d",&T);
		for (t=1; t<=T; t++)
		{
			//input
			scanf("%d%d%d\n",&sy,&sx,&w);
				for (y=0; y<sy; y++)
					scanf("%s\n",&grid[y]);
			//brute force
				for (ans=min(sy,sx); ans>2; ans--)
					for (y=0; y+ans-1<sy; y++)
						for (x=0; x+ans-1<sx; x++)
						{
							cy=y+(LD)(ans-1)/2;
							cx=x+(LD)(ans-1)/2;
							//cy=0.54,cx=0.46;
							vy=vx=0;
								for (a=y; a<y+ans; a++)
									for (b=x; b<x+ans; b++)
									{
											if ((a==y) || (a==y+ans-1))
												if ((b==x) || (b==x+ans-1))
													continue;
										vy+=(LD)(a-cy)*(w+grid[a][b]-'0');
										vx+=(LD)(b-cx)*(w+grid[a][b]-'0');
									}
								if ((fabs(vy)<EPS) && (fabs(vx)<EPS))
									goto done;
						}
			//output
done:
			printf("Case #%d: ",t);
				if (ans<3)
					printf("IMPOSSIBLE\n");
				else
					printf("%d\n",ans);
		}
	return(0);
}