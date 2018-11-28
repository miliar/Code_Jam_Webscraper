#include <stdio.h>

int p[10][4]={{0,5,10,15},{3,6,9,12},{0,1,2,3},{4,5,6,7},{8,9,10,11},
{12,13,14,15},{0,4,8,12},{1,5,9,13},{2,6,10,14},{3,7,11,15}};

int check(int *a)
{
	int i,j;
	for(i=0;i<10;i++)
	{
		for(j=0;j<3;j++)
		{
			if(!(a[p[i][j]]&a[p[i][j+1]]))
				break;
		}
		if(j==3)
			return a[p[i][0]]&a[p[i][1]];
	}
	return 0;
}
int main()
{
	int t,test=0;
	char map[5][7];
	int a[22],i,j,k,count,tmp;
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("s.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		for(i=0;i<4;i++)
			scanf("%s",map[i]);
		count=0;
		k=0;
		for(i=0,k=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				if(map[i][j]=='X')
					a[k++]=1;
				else if(map[i][j]=='O')
					a[k++]=2;
				else if(map[i][j]=='T')
					a[k++]=3;
				else
				{
					a[k++]=0;
					count++;
				}
			}
		tmp=check(a);
		printf("Case #%d: ",++test);
		if(tmp==1)
			puts("X won");
		else if(tmp==2)
			puts("O won");
		else if(count==0)
			puts("Draw");
		else
			puts("Game has not completed");
	}

	return 0;
}