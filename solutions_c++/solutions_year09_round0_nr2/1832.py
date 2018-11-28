#include <stdio.h>
#include <string.h>

int mat[103][103];
int ans[103][103];
int s = 'a';
int h,w;

int find_sink(int i,int j)
{
	int min;
	char dir;
	if(ans[i][j] != 0)  
		return ans[i][j];
	min = mat[i][j];
	if(i  >0 && mat[i-1][j] < min)  
	{
		min = mat[i-1][j];
		dir = 'n'; 
	}
	if(j > 0 && mat[i][j-1] < min)  
	{
		min = mat[i][j-1];
		dir = 'w';
	}
	if(j < w-1 && mat[i][j+1] < min)  
	{
		min = mat[i][j+1];
		dir = 'e';
	}
	if(i < h-1 && mat[i+1][j] < min)  
	{
		min = mat[i+1][j];
		dir = 's';
	}
	
	if(min == mat[i][j])  
		ans[i][j] = s++;
    else if(dir == 'n')
		ans[i][j] = find_sink(i-1,j);
	else if(dir == 'w')  
		ans[i][j] = find_sink(i,j-1);
	else if(dir == 'e') 
		ans[i][j] = find_sink(i,j+1);
	else if(dir == 's') 
		ans[i][j] = find_sink(i+1,j);
	
	return ans[i][j];
}


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("data.txt","w",stdout);
	int cas,i,j,k,p,q;
	scanf("%d",&cas);
	for (k=1;k<=cas;k++)
	{
		scanf("%d%d",&h,&w);
		for (i=0;i<h;i++)
		{
			for (j=0;j<w;j++)
			{
				scanf("%d",&mat[i][j]);
			}
		}
		memset(ans,0,sizeof(ans));
		s = 'a';
		
		for (p = 0;p < h;p++)
		{
			for (q = 0;q < w;q++)
			{
				find_sink(p,q);
			}
		}
		printf("Case #%d:\n",k);
		
		for (i=0;i<h;i++)
		{
			for (j=0;j<w;j++)
			{
				printf("%c ",ans[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
