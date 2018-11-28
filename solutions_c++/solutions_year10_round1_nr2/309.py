#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;
int D,I,M,N;
int arr[300];
int opt[401][300][300];//[100][256];
int main()
{
	int T;
	int oo=100000000;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d %d %d %d",&D,&I,&M,&N);
		
		for(int i=1;i<=N;i++)
			scanf("%d",&arr[i]);
	
	
		
		
		for(int a=1;a<=N;a++)
		{
			for(int x=0;x<256;x++)
				opt[0][a][x]=D*a;
		}
		for(int p=1;p<=N;p++)
			for(int x=0;x<256;x++)
				opt[p][0][x]=I*p;
		
		int MAXX=270;
		for(int p=1;p<=MAXX;p++)
			for(int a=1;a<=N;a++)
				for(int x=0;x<256;x++)
				{
					opt[p][a][x]=oo;
					for(int y=0;y<256;y++)
					{
						
						if(abs(x-y)<=M || p==1)
							opt[p][a][x]=min(opt[p][a][x],opt[p-1][a][y]+I);
						
						if(x==y)
							opt[p][a][x]=min(opt[p][a][x],opt[p][a-1][y]+D);//DEL
						
						if(abs(x-y)<=M || p==1)
							opt[p][a][x]=min(opt[p][a][x],opt[p-1][a-1][y]+abs(x-arr[a]));
					}
				}
		
	
			
		
		
		int answer=opt[0][N][0];
		for(int p=0;p<=MAXX;p++)
			for(int c=0;c<256;c++)
				answer=min(answer,opt[p][N][c]);
		
		
		printf("Case #%d: %d\n",t,answer);
		
		
		
	}
}