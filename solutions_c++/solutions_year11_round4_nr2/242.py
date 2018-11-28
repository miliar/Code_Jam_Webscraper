#include <stdio.h>
#include <iostream>
using namespace std;
char map[16][16];
int tot,r,c,d;
int findans()
{
	int ans=2;
	for(int len=3;len<=r;len++)
	{
		bool flag=false;
		for(int x=0;x<r;x++)
			for(int y=0;y<c;y++)
				if(x+len<=r&&y+len<=c)
				{
					int mx=0,my=0,mxx=0,myy=0,mtot=0;
					for(int xx=x;xx<x+len;xx++)
						for(int yy=y;yy<y+len;yy++)
						{
							mx+=(map[xx][yy]-'0')*xx;
							my+=(map[xx][yy]-'0')*yy;
							mtot+=(map[xx][yy]-'0');
						}
					mx-=(map[x][y]-'0')*x;
					mx-=(map[x+len-1][y]-'0')*(x+len-1);
					mx-=(map[x][y+len-1]-'0')*x;
					mx-=(map[x+len-1][y+len-1]-'0')*(x+len-1);
					my-=(map[x][y]-'0')*y;
					my-=(map[x+len-1][y]-'0')*y;
					my-=(map[x][y+len-1]-'0')*(y+len-1);
					my-=(map[x+len-1][y+len-1]-'0')*(y+len-1);
					mtot-=(map[x][y]-'0');
					mtot-=(map[x+len-1][y]-'0');
					mtot-=(map[x][y+len-1]-'0');
					mtot-=(map[x+len-1][y+len-1]-'0');
					if(len%2==1)
					{
						mxx=(x+(len/2+1)-1)*mtot*2;
						myy=(y+(len/2+1)-1)*mtot*2;
					}else
					{
						mxx=(x+(len/2)-1)*2*mtot+mtot;
						myy=(y+(len/2)-1)*2*mtot+mtot;
					}
					if(mxx==mx*2&&myy==my*2)
					{
						flag=true;
						break;
					}
				}
		if(flag)ans=len;
	}
	return ans;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&tot);
	for(int t=1;t<=tot;t++)
	{
		scanf("%d%d%d",&r,&c,&d);
		getchar();
		for(int x=0;x<r;x++)gets(map[x]);
		int kk=findans();
		if(kk==2)printf("Case #%d: IMPOSSIBLE\n",t);
		else
		printf("Case #%d: %d\n",t,kk);
	}
	return 0;
}
