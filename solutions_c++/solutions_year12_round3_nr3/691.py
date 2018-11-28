#include<cstdio>
using namespace std;
int i1t[1000],i2t[1000],n,m;
long long b[1000][1000],i1[1000],i2[1000];
long long max(long long x,long long y){ if( x>=y ) return x; return y; }
long long min(long long x,long long y){ if( x<=y ) return x; return y; }
long long dp(int x,int y)
{
	int xp,yp;
	long long mx,t,xx,yy;
	if( x==n || y==m ) return 0;
	if( b[x][y]>=0ll ) return b[x][y];
	if( i1t[x]!=i2t[y] ) return max(dp(x+1,y),dp(x,y+1));
	mx=0;
	xp=x; yp=y;
	xx=i1[xp]; yy=i2[yp];
	while( 1 )
	{
		t=dp(xp+1,yp+1)+min(xx,yy);
		if( t>mx ) mx=t;
		if( xx<yy )
		{
			xp++;
			if( xp>=n ) goto skp;
			while( 1 )
			{
				if( i1t[xp]==i2t[yp] ) break;
				xp++;
				if( xp>=n ) goto skp;
			}
			xx+=i1[xp];
		}
		else
		{
			yp++;
			if( yp>=m ) goto skp;
			while( 1 )
			{
				if( i1t[xp]==i2t[yp] ) break;
				yp++;
				if( yp>=m ) goto skp;
			}
			yy+=i2[yp];
		}
	}
skp:;
	b[x][y]=mx;
	return mx;
}
int main()
{
int T,N;
scanf("%d",&N);
for(T=1;T<=N;T++)
{
	int a,s;
	scanf("%d%d",&n,&m);
	for(a=0;a<n;a++) scanf("%I64d%d",&i1[a],&i1t[a]);
	for(a=0;a<m;a++) scanf("%I64d%d",&i2[a],&i2t[a]);
	for(a=0;a<n;a++) for(s=0;s<m;s++) b[a][s]=-1ll;
	printf("Case #%d: %I64d\n",T,dp(0,0));
/*for(a=0;a<n;a++)
{
	for(s=0;s<m;s++) fprintf(stderr,"%I64d ",b[a][s]);
	fprintf(stderr,"\n");
}*/
}
	return 0;
}
