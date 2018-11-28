#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define Max 	10000
#define Pi      acos(-1)
#define Ee      exp(1)


void Kevinew()
{
#ifndef  ONLINE_JUDGE
	freopen("in.txt","r",stdin);
#endif
}


struct PP{
	int y, x;	
}p[2];


int main()
{
	int  i,j,k,n,kevin,T,ncase,N,M,A,x1,x2,y1,y2;
	bool f;
	//Kevinew();	
	scanf("%d",&T);
	for(ncase = 1 ; ncase <= T; ncase ++ ){
		scanf("%d%d%d",&N,&M,&A);
		f = false;
		for(p[0].x=0; p[0].x<=N; p[0].x++)
		{
		
			for(p[0].y=0;p[0].y<=M;p[0].y++)
			{
				
				for(p[1].x=0;p[1].x<=N;p[1].x++)			
				{
					for(p[1].y=0;p[1].y<=M;p[1].y++)
					{
						if(f) break;
						if( abs(p[0].x*p[1].y-p[1].x*p[0].y)==A )
						{
							f = true; break;
						}

					}if(f) break;
				}if(f) break;
			}	if(f) break;
		}
		if(f==false){
			printf("Case #%d: IMPOSSIBLE\n",ncase);
		}
		else printf("Case #%d: 0 0 %d %d %d %d\n",ncase,p[0].x,p[0].y,p[1].x,p[1].y);

	}


	return 0;
}