#include<iostream>
#include<algorithm>

using namespace std;

struct pp
{
	long long x,y;
}p[100005];
int T,n,m,a,b,c,d,x0,y0;
bool comp(pp A, pp B)
{
	if(A.x != B.x)
		return A.x  < B.x;
	else
		return A.y < B.y;
}
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int t,i,j,k;
	scanf("%d",&T);
	for(t = 1; t <= T; t ++)
	{
		scanf("%d %d %d %d %d %d %d %d",&n,&a,&b,&c,&d,&x0,&y0,&m);
		p[0].x = x0;	p[0].y = y0;
		for(i = 1; i < n; i ++)
		{
			p[i].x = (a*p[i-1].x+b)%m;
			p[i].y = (c*p[i-1].y+d)%m;
		}
		long long ans = 0;
		long long x,y;
		for(i = 0; i < n; i ++)
		{
			for(j = i+1; j < n; j ++)
			{
				for(k = j+1; k < n; k ++)
				{
					if(((p[i].x+p[j].x+p[k].x)%3 == 0)  && ((p[i].y+p[j].y+p[k].y)%3 == 0) )
						ans ++;
				}
			}
		}

		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}