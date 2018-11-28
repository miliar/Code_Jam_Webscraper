#include <stdio.h>

const int R = 10;
const int X = 100;
const int Y = 100;

typedef struct state
{
	int count;
	int cell[X][Y];
}state;

const state INIT = {};

state next(state);

main()
{
	int c;
	int r;
	int x1, x2, y1, y2;
	int ans;
	state now;
	scanf("%d", &c);
	for (int i=1;i<=c;i++)
	{
		ans=0;
		now=INIT;
		
		scanf("%d", &r);
		for (int j=0;j<r;j++)
		{
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			x1--;
			y1--;
			x2--;
			y2--;
			for (int k=x1;k<=x2;k++)
				for (int l=y1;l<=y2;l++)
					now.cell[k][l]=1;
		}
		for (int j=0;j<X;j++)
			for (int k=0;k<Y;k++)
				if (now.cell[j][k])
					now.count++;
		
		while (now.count)
		{
			now=next(now);
			ans++;
		}
		
		printf("Case #%d: %d\n", i, ans);
	}
}

state next(state now)
{
	state next=now;
	
	for (int i=0;i<X;i++)
		for (int j=0;j<Y;j++)
			if (next.cell[i][j])
			{
				if ((i==0||(!now.cell[i-1][j])) && (j==0||(!now.cell[i][j-1])))
					next.cell[i][j]=0;
			}
			else
			{
				if ((i>0&&now.cell[i-1][j]) && (j>0&&now.cell[i][j-1]))
					next.cell[i][j]=1;
			}
	
	next.count=0;
	for (int i=0;i<X;i++)
		for (int j=0;j<Y;j++)
			if (next.cell[i][j])
				next.count++;
	
	return next;
}
