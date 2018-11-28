#include<stdio.h>
#define MAX 200

struct Point
{
	__int64 x;
	__int64 y;
}content[MAX];

int search(__int64 n,__int64 x,__int64 y)
{
	__int64 i;
	for(i=0;i<n;i++)
	{
		if(content[i].x == x && content[i].y == y)	return 0;
	}
	return 1;
}

int process(__int64 n)
{
	int i,count=0,j,k;
	for(i=0;i<n-2;i++)
	{
		for(j=i+1;j<n-1;j++)
		{
			for(k=j+1;k<n;k++)
			{
				if((content[i].x + content[j].x + content[k].x) % 3 == 0 && (content[i].y + content[j].y + content[k].y) % 3 == 0)
				{
					count++;
				}
			}
		}
	}
	return count;
}

int main(void)
{
	__int64 N,A,B,C,D,x0,y0,M,n,i,j,k,X,Y,count;

	freopen("A-small-attempt1(2).in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%I64d",&N);

	for(i=1;i<=N;i++)
	{
		scanf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&n,&A,&B,&C,&D,&x0,&y0,&M);

		X = x0;
		Y = y0;
		content[0].x = X;
		content[0].y = Y;
		k = 1;
		for(j = 1 ;j<=n-1 ;j++)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			if(search(k,X,Y))
			{
				content[k].x = X;
				content[k].y = Y;
				k++;
			}
			else	break;
		}
		count = process(k);
		printf("Case #%I64d: %I64d\n",i,count);
	}
	return 0;
}