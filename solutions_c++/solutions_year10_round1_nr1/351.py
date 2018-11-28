#include <stdio.h>
#include <math.h>
int N,K;
int matrix[600][600];
bool wins[4];
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d %d",&N,&K);
		for(int i=0;i<2*N+1;i++)
			for(int j=0;j<2*N+1;j++)
				matrix[i][j]=0;
		
		for(int i=0;i<N;i++)
		{
			char line[60];
			scanf("%s",&line);
			for(int j=0;j<N;j++)
				matrix[i][j]=(line[j]=='.'?0:(line[j]=='R'?1:2));
			
		}
		
		for(int i=0;i<N;i++)
		{
			for(int j=N-2;j>=0;j--)
			{
				if(matrix[i][j]!=0)
				{
					int k=j;
					while(k<N-1 && matrix[i][k+1]==0)
					{
						k++;
					}
					if(k!=j)
					{
						matrix[i][k]=matrix[i][j];
						matrix[i][j]=0;
					}
					
					
				}
				
				
			}
		}
		
		
		wins[1]=wins[2]=0;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(matrix[i][j]!=0)
				{
					int nums=0;
					int k=0;
					while(matrix[i-k][j]==matrix[i][j] && nums<K)
					{
						nums++;
						k++;
						if(i-k<0)
							break;
					}
					if(nums>=K)
						wins[matrix[i][j]]=1;
					
					
					nums=0;
					k=0;
					while(matrix[i][j-k]==matrix[i][j] && nums<K)
					{
						nums++;
						k++;
						if(j-k<0)
							break;
					}
					if(nums>=K)
						wins[matrix[i][j]]=1;
					
					
					nums=0;
					k=0;
					while(matrix[i+k][j+k]==matrix[i][j] && nums<K)
					{
						nums++;
						k++;
						if(i+k>=N||j+k>=N)
							break;
					}
					if(nums>=K)
						wins[matrix[i][j]]=1;
					k=0;
					nums=0;
					while(matrix[i-k][j+k]==matrix[i][j] && nums<K)
					{
						nums++;
						k++;
						if(i-k<0||j+k>=N)
							break;
					}
					if(nums>=K)
						wins[matrix[i][j]]=1;
					
			
					
					
					
				}
				
				
			}
		}
		if(wins[1]&&wins[2])
			printf("Case #%d: Both\n",t);
		if(wins[1]&&!wins[2])
			printf("Case #%d: Red\n",t);
		if(!wins[1]&&wins[2])
			printf("Case #%d: Blue\n",t);
		if(!wins[1]&&!wins[2])
			printf("Case #%d: Neither\n",t);
		
		
		
		
		
	}
}