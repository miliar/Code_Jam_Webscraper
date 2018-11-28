#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include "iostream.h"
#include "conio.h"
	char map[51][51];
int main()
{	
	//freopen("A-large.in","r",stdin);
	//freopen("A-outlarge.out","w",stdout);
	int T,R,C;
	int i,j,n;
scanf("%d",&T);

	for (n=0;n<T;n++)
	{
		int sum=0;
		int win=0;
		scanf("%d%d\n",&R,&C);
		for(i=0;i<R;i++)
		{
			for (j=0;j<C;j++)
			{
				scanf("%c",&map[i][j]);
				if(map[i][j]=='#') {
					sum++;
				}
			}
			getchar();
		}
		//  	for(i=0;i<R;i++)
		//  	{
		//  		for (j=0;j<C;j++)
		//   		{
		//   			printf("%c",map[i][j]);
		//   		}
		//  		printf("\n");
		//  	}
		
		for(i=0;i<R;i++)
		{
			for (j=0;j<C;j++)
			{
				if(map[i][j]=='#')
				{
					if(map[i+1][j]=='#'&&map[i][j+1]=='#'&&map[i+1][j+1]=='#') 
					{
						map[i][j]='/'; 
						map[i][j+1]='\\';
						map[i+1][j]='\\'; 
						map[i+1][j+1]='/';
						sum-=4;
						if(sum==0) {
							win=1;
							goto h;
						}
					}
					else {
						win=0;
						goto h;
					}
				}
			}
		}
h:
		if(sum!=0) printf("Case #%d:\nImpossible\n",n+1);
		else{
			printf("Case #%d:\n",n+1);
			for(i=0;i<R;i++)
			{
			  		for (j=0;j<C;j++)
			   		{
			   			printf("%c",map[i][j]);
			   		}
			  		printf("\n");
		 	}
		}
	}
	return 0;
}