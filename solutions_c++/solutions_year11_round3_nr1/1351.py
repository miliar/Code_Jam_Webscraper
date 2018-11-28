#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char g[100][100];
int main()
{
	int ca,n,m,i,j,test=0,ok;
	char s[100];
	FILE *f;
	f=fopen("A.out","w");


	scanf("%d",&ca);
	while(ca--)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			scanf("%s",s);
			for(j=0;j<m;j++)
			g[i][j]=s[j];
		}

		for(i=0;i<n-1;i++)
		 for(j=0;j<m-1;j++)
		 {
		  if(g[i][j]=='#' && g[i][j+1]=='#' && g[i+1][j]=='#' && g[i+1][j+1]=='#')
		  {
			g[i][j]='/';
			g[i][j+1]='\\';
			g[i+1][j]='\\';
			g[i+1][j+1]='/';
		  }
		 }
		 ok=1;
		 for(i=0;i<n;i++)
		 {
			 for(j=0;j<m;j++) 
				 if(g[i][j]=='#')
			 {
				 ok=0;
				 break;
			 }
			if(ok==0) break;
		 }

		 fprintf(f,"Case #%d:\n",++test);
		 if(ok==0) fprintf(f,"Impossible\n");
		 else
		 {
			 for(i=0;i<n;i++)
			 {
				 for(j=0;j<m;j++)
				 fprintf(f,"%c",g[i][j]);
				 fprintf(f,"\n");
			 }
		 }
	}
	system("pause");
	return 0;
}
