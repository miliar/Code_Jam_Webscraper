#include<stdio.h>
#include<vector>
#define MAXX 100

using namespace std;

int T,H,W;
int data[MAXX][MAXX];
short basin[MAXX][MAXX];
int count = 1;

int read_dat(int x,int y)
{
	if(x >= 0 && x < H && y >= 0 && y <W)
		return data[x][y];
	else
		return -1;
}

int min(int a,int b,int c,int d)
{
	int min = 10001;
	if(a != -1 && a < min)
		min = a;
	if(b != -1 && b < min)
		min = b;
	if(c != -1 && c < min)
		min = c;
	if(d != -1 && d < min)
		min = d;
	return min;
}

short find_base(int x,int y)
{
	if(basin[x][y] > 0)
		return basin[x][y];
	int no = read_dat(x-1,y),so = read_dat(x+1,y),ea = read_dat(x,y+1),we = read_dat(x,y-1);
	int mini = min(no,so,ea,we);
	//printf("%d--\n",mini);
	if(mini >= read_dat(x,y))
	{
		basin[x][y] = count++;
		return basin[x][y];
	}
	int ans;
	if(no == mini)
		ans = find_base(x-1,y);
	else if(we == mini)
		ans = find_base(x,y-1);
	else if(ea == mini)
		ans = find_base(x,y+1);
	else if(so == mini)
		ans = find_base(x+1,y);
	basin[x][y] = ans;
	return ans;
}

int main()
{
	scanf("%d",&T);
	for(int round=1;round<=T;round++)
	{		
		scanf("%d %d",&H,&W);
		count=1;
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
			{
				scanf("%d",&data[i][j]);
				basin[i][j] = 0;
			}
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)		
				basin[i][j] = find_base(i,j);
		printf("Case #%d: \n",round);
		for(int i=0;i<H;printf("\n"),i++)
			for(int j=0;j<W;j++)
			{	
				//printf("%d ",basin[i][j]);		
				printf("%c ",('a'+ basin[i][j]-1));
			}
	}
	return 0;
}
