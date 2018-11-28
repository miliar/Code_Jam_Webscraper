#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int t,i,j,m,n,k;
	char a[60][60];
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d%d",&m,&n);
		for(i=0;i<m;i++)
			scanf("%s",a[i]);
		bool flag=true;	
		for(i=0;i<m;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[i][j]=='#')
				{
					if(i+1<m && j+1<n && a[i][j+1]=='#' && a[i+1][j+1]=='#' && a[i+1][j]=='#')
					{
						a[i][j]=a[i+1][j+1]='/';
						a[i+1][j]=a[i][j+1]='\\';
					}
					else
						flag=false;
				}
			}
		}
		printf("Case #%d:\n",k);
		if(flag)
		{
			for(i=0;i<m;i++,printf("\n"))
				for(j=0;j<n;j++)
					printf("%c",a[i][j]);
		}
		else
		{
			printf("Impossible\n");
		}
	}
	return 0;
}
