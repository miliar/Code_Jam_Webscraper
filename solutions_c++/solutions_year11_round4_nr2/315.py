#include "stdio.h"
#include "string.h"
#include <algorithm>
using namespace std;
#define M 555

int r,c,d;
int a[M][M];
char s[M];

bool solve(int x,int y,int len)
{
	int i,j;
	double dx=0,dy=0,px=len/2.0+x,py=len/2.0+y;
	if(x==1&&y==1&&len==5)
		len=len;
	for(i=1;i<len-1;i++)
	{
		dx+=(px-x-0.5)*a[x][i+y];
		dy+=(py-y-i-0.5)*a[x][i+y];
	}
	for(i=1;i<len-1;i++)
	{
		for(j=0;j<len;j++)
		{
			dx+=(px-x-i-0.5)*a[i+x][j+y];
			dy+=(py-y-j-0.5)*a[i+x][j+y];
		}
	}
	for(i=1;i<len-1;i++)
	{
		dx+=(px-x-len+1-0.5)*a[len+x-1][i+y];
		dy+=(py-y-i-0.5)*a[len+x-1][i+y];
	}
	return dx==0&&dy==0;
}

int main()
{
	int i,j,k,t,tc=1;
	freopen("gcj/2011.6.4/B-large.in","r",stdin);
	freopen("in.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&r,&c,&d);
		for(i=0;i<r;i++)
		{
			scanf("%s",s);
			for(j=0;j<c;j++)
			{
				a[i][j]=s[j]-'0'+d;
			}
		}
		for(k=r;k>2;k--)
		{
			if(k>c) continue;
			for(i=0;i<r-k+1;i++)
			{
				for(j=0;j<c-k+1;j++)
				{
					if(solve(i,j,k))
						break;
				}
				if(j<c-k+1)
					break;
			}
			if(i<r-k+1)
				break;
		}
		printf("Case #%d: ",tc++);
		if(k>2)
			printf("%d\n",k);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}

/*
2
6 7 2
1111111
1122271
1211521
1329131
1242121
1122211
3 3 7
123
234
345
*/

