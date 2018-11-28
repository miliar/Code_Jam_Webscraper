#include <cstdio>
#include <algorithm>
#include <memory.h>
struct pt
{
	int x,y,a;
};
inline bool cmp(pt a, pt b)
{
	return a.a<b.a;
}
pt tab[10240];
int tabsz;
int map[128][128];
int t,h,w;
char rl[32];
char curr_rl;
int rgnid[128][128];
int curr_rgnid;
inline int min4(int a,int b, int c, int d)
{
	return std::min(a,std::min(b,std::min(c,d)));
}
inline bool wd(int x, int y,int px,int py)
{
	int dn=(y<=0)?999999:map[x][y-1];
	int ds=(y>=h-1)?999999:map[x][y+1];
	int dw=(x<=0)?999999:map[x-1][y];
	int de=(x>=w-1)?999999:map[x+1][y];
	int m=min4(dn,ds,de,dw);
	if(m<map[x][y])
	{
		if(m==dn)
		{
			if(py<y)return true;
			else return false;
		}
		if(m==dw)
		{
			if(px<x)return true;
			else return false;
		}
		if(m==de)
		{
			if(px>x)return true;
			else return false;
		}
		if(m==ds)
		{
			if(py>y)return true;
			else return false;
		}
	}
	return false;
}
void go()
{
	curr_rgnid=0;
	for(int i=0;i<tabsz;++i)
	{
		int x=tab[i].x,y=tab[i].y,a=tab[i].a;
		if(rgnid[x][y]==0)
		{
			rgnid[x][y]=++curr_rgnid;
		}
		if(x>0)
		{
			if(map[x-1][y]>a)
			{
				if(wd(x-1,y,x,y))
				{
					rgnid[x-1][y]=rgnid[x][y];
				}
			}
		}
		if(y>0)
		{
			if(map[x][y-1]>a)
			{
				if(wd(x,y-1,x,y))
				{
					rgnid[x][y-1]=rgnid[x][y];
				}
			}
		}
		if(x<w-1)
		{
			if(map[x+1][y]>a)
			{
				if(wd(x+1,y,x,y))
				{
					rgnid[x+1][y]=rgnid[x][y];
				}
			}
		}
		if(y<h-1)
		{
			if(map[x][y+1]>a)
			{
				if(wd(x,y+1,x,y))
				{
					rgnid[x][y+1]=rgnid[x][y];
				}
			}
		}
	}
	for(int y=0;y<h;++y)
	{
		for(int x=0;x<w;++x)
		{
			if(rl[rgnid[x][y]]==0)
			{
				rl[rgnid[x][y]]=curr_rl++;
			}
		}
	}
}
int main()
{
	scanf("%d",&t);
	for(int i=1;i<=t;++i)
	{
		scanf("%d%d",&h,&w);
		int j=0;
		for(int y=0;y<h;++y)
		{
			for(int x=0;x<w;++x)
			{
				scanf("%d",&map[x][y]);
				tab[j].a=map[x][y];
				tab[j].x=x;
				tab[j].y=y;
				++j;
			}
		}
		tabsz=j;
		std::sort(tab,tab+j,cmp);
		curr_rl='a';
		memset(rl,0,sizeof(rl));
		memset(rgnid,0,sizeof(rgnid));
		go();
		printf("Case #%d:\n",i);
		for(int y=0;y<h;++y)
		{
			for(int x=0;x<w;++x)
			{
				putchar(rl[rgnid[x][y]]);
				putchar(' ');
			}
			putchar('\n');
		}
	}
	return 0;
}

