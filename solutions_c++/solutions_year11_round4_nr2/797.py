#include <stdio.h>
#include <string.h>
#include <queue>
#include <string>
#include <map>
#include <algorithm>
#include <math.h>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

int cs,cn=1;
int R,C,D;

struct point
{
	double x,y;
};

char mp[505][505];
point ct;

int check(int sx,int sy,int len)
{
	int i,j;
	double s1 = 0,s2 = 0;
	for(i=sx;i<sx+len;i++)
	{
		for(j=sy;j<sy+len;j++)
		{
			if((i==sx&&j==sy) || (i==sx+len-1&&j==sy) || (i==sx&&j==sy+len-1) || (i==sx+len-1&&j==sy+len-1))
				continue;
			s1 += (i+0.5-ct.x)*(D+mp[i][j]-'0');
			s2 += (j+0.5-ct.y)*(D+mp[i][j]-'0');
		}
	}
	if(fabs(s1)<1e-6 && fabs(s2)<1e-6) return 1;
	return 0;
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.out","w",stdout);
	int i,j;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%d%d%d",&R,&C,&D);
		for(i=0;i<R;i++)
		{
			scanf("%s",mp[i]);
		}
		int len = min(R,C);
		for(;len>=3;len--)
		{
			int ok = 0;
			for(i=0;i<=R-len;i++)
			{
				for(j=0;j<=C-len;j++)
				{
					ct.x = i+1.0*len/2;
					ct.y = j+1.0*len/2;
					if(check(i,j,len))
					{
						ok = 1;
						break;
					}
				}
				if(ok) break;
			}
			if(ok) break;
		}
		if(len >= 3)
		{
			printf("Case #%d: %d\n",cn++,len);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n",cn++);
		}
	}
	return 0;
}


