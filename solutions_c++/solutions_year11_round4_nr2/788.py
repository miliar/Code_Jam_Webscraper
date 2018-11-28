#include<stdio.h>
#include<algorithm>
using namespace std;

int T,R,C,D;
char g[501][501];

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.in.txt","w",stdout);
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		scanf("%d%d%d",&R,&C,&D);
		for (int i=0;i<R;i++)
		{
			scanf("%s",&g[i]);
			for (int j=0;j<C;j++) g[i][j]-='0';
		}
		int d=R;
		int ans=-1;
		if (C<d) d=C;
		for (;d>=3;d--)
		{
			for (int i=0;i<R-d+1;i++)
				for (int j=0;j<C-d+1;j++)
				{
					int ix=0,iy=0,tot=0;
					for (int ii=i;ii<i+d;ii++)
						for (int jj=j;jj<j+d;jj++)
						{
							ix+=ii*g[ii][jj];
							iy+=jj*g[ii][jj];
							tot+=g[ii][jj];
						}
					tot-=g[i][j]+g[i][j+d-1]+g[i+d-1][j]+g[i+d-1][j+d-1];
					ix-=i*(g[i][j]+g[i][j+d-1])+(i+d-1)*(g[i+d-1][j]+g[i+d-1][j+d-1]);
					iy-=j*(g[i][j]+g[i+d-1][j])+(j+d-1)*(g[i][j+d-1]+g[i+d-1][j+d-1]);
					//printf("%d i,j: %d %d %d %d\n",d,i,j,ix,iy);
					if (d%2==1&&ix==(i+d/2)*tot&&iy==(j+d/2)*tot||
						d%2==0&&ix*2==(2*i+d-1)*tot&&iy*2==(2*j+d-1)*tot)
					{
						ans=d;
						goto lab;
					}
				}
		}
lab:
		if (ans!=-1)
			printf("Case #%d: %d\n",cas,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",cas);
		//printf("Case #%d: %.8f\n",cas,ans);

	}
	//while(1);
}