#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <string.h>
using namespace std;
__int64 sw[501][501];
__int64 a[500][500];
__int64 sx[501][501];
__int64 sy[501][501];
int min(int i,int j) {return i<=j?i:j;}
void minu(__int64 &mx, __int64 &my, int x, int y, int cx,int cy,__int64 w)
{
	mx-=(x*2+1)*w-cx*w;
	my-=(y*2+1)*w-cy*w;
}
int main()
{
	int tc,cas,nr,nc,nd,i,j,k;
	__int64 m;
	char str[1024];
	freopen("B-large.in","r",stdin);
	freopen("output_la.txt","w",stdout);
	scanf("%d",&tc);
	for (cas=1;cas<=tc;++cas)
	{
		scanf("%d%d%d",&nr,&nc,&nd);
		for (i=0;i<nr;++i)
		{
			scanf("%s", str);
			for (j=0;j<nc;++j)
			{
				a[i][j]=str[j]-'0'+m;
			}
		}
		for (i=1;i<=nr;++i)
		{
			__int64 cx=0,cy=0,cw=0;
			for (j=1;j<=nc;++j)
			{
				cx+=(2*i-1)*a[i-1][j-1];
				cy+=(2*j-1)*a[i-1][j-1];
				cw+=a[i-1][j-1];
				sw[i][j]=sw[i-1][j]+cw;
				sx[i][j]=sx[i-1][j]+cx;
				sy[i][j]=sy[i-1][j]+cy;
			}
		}
		m=nd;
		int ans,x,y;
		for (ans=min(nr,nc);ans>=3;--ans)
		{
			bool found = false;
			for (x=0;x+ans<=nr;++x)
				for (y=0;y+ans<=nc;++y)
				{
					int cx=x*2+ans;
					int cy=y*2+ans;
					__int64 mx=sx[x+ans][y+ans]-sx[x+ans][y]-sx[x][y+ans]+sx[x][y];
					__int64 my=sy[x+ans][y+ans]-sy[x+ans][y]-sy[x][y+ans]+sy[x][y];
					minu(mx,my,x,y,cx,cy,a[x][y]);
					minu(mx,my,x+ans-1,y,cx,cy,a[x+ans-1][y]);
					minu(mx,my,x,y+ans-1,cx,cy,a[x][y+ans-1]);
					minu(mx,my,x+ans-1,y+ans-1,cx,cy,a[x+ans-1][y+ans-1]);
					__int64 mw=sw[x+ans][y+ans]-sw[x+ans][y]-sw[x][y+ans]+sw[x][y];
					if (mw*cx==mx && mw*cy==my) found=true;
				}
			if (found) break;
		}
		if (ans>=3) printf("Case #%d: %d\n", cas,ans);
		else printf("Case #%d: IMPOSSIBLE\n", cas);
	}
	return 0;
}