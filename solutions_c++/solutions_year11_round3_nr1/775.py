#include<iostream>
using namespace std;
char map[55][55];
int n,m;
int isok(int x,int y)
{
 	if((x+1)<n&&(y+1)<m&&map[x+1][y]=='#'&&map[x][y+1]=='#'&&map[x+1][y+1]=='#')
 	{
		return 1;
    }
    else
        return 0;
}
int main()
{
 	int t;
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
 	int i,j;
 	int cas;
 	scanf("%d",&t);
 	for(cas=1;cas<=t;cas++)
 	{
        scanf("%d%d",&n,&m);
        getchar();
        for(i=0;i<n;i++)
        {
		    for(j=0;j<m;j++)
		        scanf("%c",&map[i][j]);
            getchar();
		}
		bool flag=0;
        for(i=0;i<n;i++)
		{
		   for(j=0;j<m;j++)
		   {
		       if(map[i][j]=='#')
		       {
				   if(isok(i,j)==1)
				   {
				       map[i][j]='/';
				       map[i][j+1]='\\';
				       map[i+1][j]='\\';
				       map[i+1][j+1]='/';
				   }
				   else
				       flag=1;
	           }
	           if(flag==1) break;
		   }
		   if(flag==1) break;
		}    
		if(flag==1)
		{
             printf("Case #%d:\nImpossible\n",cas);
        }
        else
        {
		 	printf("Case #%d:\n",cas);
		 	for(i=0;i<n;i++)
		 	{
			     for(j=0;j<m;j++)
		 	        printf("%c",map[i][j]);
                 printf("\n");
		    }
 	    }
    }
 	return 0;
}
