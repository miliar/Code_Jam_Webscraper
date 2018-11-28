#include "stdio.h"
#include "string.h"

int main()
{
	freopen("small.txt","r",stdin);
	freopen("small_out.txt","w",stdout);
	int f,ca,h,r,a,b,i,j,w;
	scanf("%d",&ca);
	for(f=1;f<=ca;f++)
	{
		bool ex[200][200]={0};
		int way[200][200]={0};
		scanf("%d%d%d",&h,&w,&r);
		for(i=0;i<r;i++)
		{
			scanf("%d%d",&a,&b);
			ex[a][b]=1;
		}
		way[1][1]=1;
		for(i=1;i<=h;i++)
		{
			for(j=1;j<=w;j++)
			{
				if(i>1&&j>2&&!ex[i-1][j-2])
				{
					way[i][j]=way[i][j]+way[i-1][j-2];
				}
				if(i>2&&j>1&&!ex[i-2][j-1])
				{
					way[i][j]=way[i][j]+way[i-2][j-1];
				}
				way[i][j]=way[i][j]%10007;
			}
		}
		printf("Case #%d: %d\n",f,way[h][w]);
	}
	return 0;
}