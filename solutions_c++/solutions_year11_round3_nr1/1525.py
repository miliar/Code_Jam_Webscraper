#include<iostream>
using namespace std;
#include<stdio.h>
#define S 51
main()
{
	int t,i,j,r,c,ic=1,flag;
	char a[S][S];
	scanf("%d",&t);
	while(t--)
	{
	scanf("%d%d",&r,&c);
	for(i=0;i<r;i++)	
		scanf("%s",a[i]);
	flag=1;
	for(i=0;i<r && flag==1;i++)
	{
		for(j=0;j<c && flag==1;j++)
		{
			if(a[i][j]=='#')
			{
				if(a[i+1][j]=='#' && a[i][j+1]=='#' && a[i+1][j+1]=='#')
				{
					a[i][j]='/';
					a[i+1][j+1]='/';
					a[i+1][j]='\\';
					a[i][j+1]='\\';
				}
				else
				{
					flag=0;
					break;
				}
			}
		}
	}
	if(flag==0)
		printf("Case #%d:\nImpossible\n",ic++);	
	else
	{
		printf("Case #%d:\n",ic++);	
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
				printf("%c",a[i][j]);
			printf("\n");
		}
	}
	}
}
