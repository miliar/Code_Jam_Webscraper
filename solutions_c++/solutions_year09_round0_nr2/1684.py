#include <stdio.h>

#define MAX_HW 105

int H,W;
int mat[MAX_HW][MAX_HW];
int ans[MAX_HW][MAX_HW];
int sink = 'a';

int find_sink(int i,int j)
{
	int mn;
	char dir;
	if(ans[i][j] != 0)  return ans[i][j];
	mn = mat[i][j];
	if(i>0 && mat[i-1][j] < mn)  mn = mat[i-1][j],dir = 'n'; //north 
	if(j>0 && mat[i][j-1] < mn)  mn = mat[i][j-1],dir = 'w'; //west
	if(j<W-1 && mat[i][j+1] < mn)  mn = mat[i][j+1],dir = 'e'; //east
	if(i<H-1 && mat[i+1][j] < mn)  mn = mat[i+1][j],dir = 's'; //north

	if(mn == mat[i][j])  ans[i][j] = sink++;
    else if(dir == 'n')  ans[i][j] = find_sink(i-1,j);
	else if(dir == 'w')  ans[i][j] = find_sink(i,j-1);
	else if(dir == 'e')  ans[i][j] = find_sink(i,j+1);
	else if(dir == 's')  ans[i][j] = find_sink(i+1,j);

	return ans[i][j];
}


void solve()
{
	int i,j;
	for (i=0;i<H;i++)
		for (j=0;j<W;j++)
		   ans[i][j] = 0;
    sink = 'a';

	for (i=0;i<H;i++)
	{
		for (j=0;j<W;j++)
		{
		   find_sink(i,j);
		}
	}

}


int main()
{
//	freopen("B-large.in","r",stdin);
//	freopen("B-large-attempt0.txt","w",stdout);
	int cas,i,j,k;
	scanf("%d",&cas);
	for (k=1;k<=cas;k++)
	{
		scanf("%d%d",&H,&W);
		for (i=0;i<H;i++)
		{
			for (j=0;j<W;j++)
			{
				scanf("%d",&mat[i][j]);
			}
		}
		solve();
		printf("Case #%d:\n",k);
		
		for (i=0;i<H;i++)
		{
			for (j=0;j<W;j++)
			{
				printf("%c ",ans[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}