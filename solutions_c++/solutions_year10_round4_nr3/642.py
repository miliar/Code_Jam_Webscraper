#include <stdio.h>
#include <math.h>
bool isthere[200][200];
bool markdel[200][200];
bool markocc[200][200];

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int R;
		scanf("%d",&R);
		for(int i=0;i<=200;i++)
			for(int j=0;j<=200;j++)
				isthere[i][j]=0;
		//printf("R=%d\n",R);
		for(int i=1;i<=R;i++)
		{
			int x1,y1,x2,y2;
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for(int x=x1;x<=x2;x++)
				for(int y=y1;y<=y2;y++)
					isthere[x][y]=1;
		}
		int numbacts=0;
		for(int i=1;i<=100;i++)
			for(int j=1;j<=100;j++)
				if(isthere[i][j])
					numbacts++;
		int time=0;
	/*	for(int i=1;i<=6;i++)
		{
			for(int j=1;j<=6;j++)
				printf("%d ",isthere[i][j]);
			printf("\n");
		}
		*/
		while(numbacts>0)
		{
			
			for(int i=1;i<=100;i++)
				for(int j=1;j<=100;j++)
				{
					markdel[i][j]=markocc[i][j]=0;
				}
			
			for(int i=1;i<=100;i++)
				for(int j=1;j<=100;j++)
				{
					if(!isthere[i][j-1] && !isthere[i-1][j] && isthere[i][j])
						markdel[i][j]=1;
					if(!isthere[i][j] && isthere[i][j-1] && isthere[i-1][j])
						markocc[i][j]=1;
				}
			
			
			for(int i=1;i<=100;i++)
				for(int j=1;j<=100;j++)
				{
					if(markdel[i][j])
					{
						isthere[i][j]=0;
						numbacts--;
					}
					if(markocc[i][j])
					{
						isthere[i][j]=1;
						numbacts++;
					}
				}
			time++;
		}
		printf("Case #%d: %d\n",t,time);
		
		
		
		
		
		
	}
}