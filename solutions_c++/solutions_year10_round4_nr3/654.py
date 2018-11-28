#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

int m[1000][1000];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int t;
	cin>>t;

	for(int tt=1;tt<=t;tt++)
	{
		int r;
		cin>>r;

		memset(m,0,sizeof(m));

		int xmin,xmax,ymin,ymax;
		xmin=ymin=10000000;
		xmax=ymax=-1;
		int cnt = 0;
		for(int i=0;i<r;i++)
		{
			int x1,y1,x2,y2;
			cin>>x1>>y1>>x2>>y2;
			--x1;--x2;--y1;--y2;
			xmin=min(x1,xmin);
			ymin=min(y1,ymin);
			xmax=max(x2,xmax);
			ymax=max(y2,ymax);
			for(int x=x1;x<=x2;++x)
				for(int y=y1;y<=y2;++y)
				{
					if (m[x][y]==0) ++cnt;
					m[x][y] = 1;
				}
		}

		int s = 0;
		while(cnt!=0)
		{
			for(int x=xmin;x<=xmax;++x)
				for(int y=ymin;y<=ymax;++y)
				{
					if (m[x][y]==0)
					{
						if (x>0&&y>0&&(m[x-1][y]&1)&&(m[x][y-1]&1))
						{
							m[x][y] = 2;
							++cnt;
						}
					}
					else if (m[x][y]==1)
					{
						int k = 0;
						if (x>0&&(m[x-1][y]&1)) ++k;
						if (y>0&&(m[x][y-1]&1)) ++k;
						if (k==0)
						{
							m[x][y] = 3;
							--cnt;
						}
					}
				}

			
			for(int x=xmin;x<=xmax;++x)
				for(int y=ymin;y<=ymax;++y)
				{
					if (m[x][y]>1) m[x][y]=3-m[x][y];
				}

			++s;
		}
		printf("Case #%d: %d\n",tt,s);
	}
	return 0;
}
