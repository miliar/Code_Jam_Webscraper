#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;

const double eps=1e-9;

int w[15][15];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int tt,i,j,r,c,d,k,x,y;
	char ch;
	double cx,cy,resx,resy;
	bool flag;
	scanf("%d",&tt);
	for (int cnt=1;cnt<=tt;cnt++)
	{
		flag=false;
		scanf("%d%d%d",&r,&c,&d);
		for (i=0;i<r;i++)
		{
			scanf("%c",&ch);
			for (j=0;j<c;j++)
			{
				scanf("%c",&ch);
				w[i][j]=ch-'0';
			}
		}
		int maxk=min(r,c);
		for (k=maxk;k>=3;k--)
		{
			for (i=k/2;i<=r-(k+1)/2;i++)
				for (j=k/2;j<=c-(k+1)/2;j++)
				{
					cx=i;
					cy=j;
					resx=0;
					resy=0;
					if (k%2==1) 
						{
							for (x=i-k/2;x<=i+k/2;x++)
								for (y=j-k/2;y<=j+k/2;y++)
								{
									resx+=(x-cx)*w[x][y];
									resy+=(y-cy)*w[x][y];
								}
								resx+=k/2*w[i-k/2][j-k/2]+k/2*w[i-k/2][j+k/2];
								resy+=k/2*w[i-k/2][j-k/2]+k/2*w[i+k/2][j-k/2];
								resx-=k/2*w[i+k/2][j-k/2]+k/2*w[i+k/2][j+k/2];
								resy-=k/2*w[i-k/2][j+k/2]+k/2*w[i+k/2][j+k/2];
						}
					else
					{
						for (x=i-k/2;x<i+k/2;x++)
								for (y=j-k/2;y<j+k/2;y++)
								{
									resx+=(x+0.5-cx)*w[x][y];
									resy+=(y+0.5-cy)*w[x][y];
								}
						resx+=(k/2-0.5)*w[i-k/2][j-k/2]+(k/2-0.5)*w[i-k/2][j+k/2-1];
						resy+=(k/2-0.5)*w[i-k/2][j-k/2]+(k/2-0.5)*w[i+k/2-1][j-k/2];
						resx-=(k/2-0.5)*w[i+k/2-1][j-k/2]+(k/2-0.5)*w[i+k/2-1][j+k/2-1];
						resy-=(k/2-0.5)*w[i-k/2][j+k/2-1]+(k/2-0.5)*w[i+k/2-1][j+k/2-1];
					}
					if (abs(resx)<eps && abs(resy)<eps)
					{
						flag=true;
						break;
					}
				}
			if (flag) break;
		}
		printf("Case #%d: ",cnt);
		if (flag) printf("%d\n",k);
		else printf("IMPOSSIBLE\n");
	}
 	return 0;
}