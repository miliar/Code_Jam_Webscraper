#include<iostream>
using namespace std;

int times,len,sp,r,ti,n;
const int MAXN = 1000+100; 
int b[MAXN], e[MAXN], w[MAXN]; 
int min(int a, int b){ return a < b ? a : b; }

struct person
	{
	int l,r,s;
	} wal[1024];

inline bool cmp2 ( const person &a,const person &b )
	{
	return ( a.l<b.l );
	}

inline bool cmp ( const person &a,const person &b )
	{
	return ( a.s<b.s );
	}

int qs ( int l, int r )
	{
	int p, mid, i, j;

	i = l;
	j = r;
	mid = b[ ( i+l ) >>1];
	do
		{
		while ( b[i] < mid ) ++i;
		while ( b[j] > mid ) --j;
		if ( i <= j )
			{
			swap ( b[i], b[j] );
			swap ( e[i], e[j] );
			++i;
			--j;
			}
		}
	while ( i <= j );
	if ( l<j ) qs ( l,j );
	if ( i<r ) qs ( i,r );
	}

int main()
	{
	freopen ( "1.in","r",stdin );
	freopen ( "1out.out","w",stdout );
	
	scanf ( "%d",&times );
	int z; 
	for ( z=1; z<=times; ++z )
		{
		scanf ( "%d%d%d%d%d",&len,&sp,&r,&ti,&n );
		//printf("[%d,%d,%d,%d,%d]",len,sp,r,ti,n);
		for ( int a=1; a<=n; ++a )
			{
			scanf ( "%d%d%d",&wal[a].l,&wal[a].r,&wal[a].s );
			//wal[a].p=a;
			}
		sort ( wal+1,wal+1+n,cmp2 );
		int now=0,all=n;;
		for ( int a=1; a<=n; ++a )
			{
			if ( wal[a].l!=now )
				{
				++all;
				wal[all].l=now;
				wal[all].r=wal[a].l;
				wal[all].s=0;
				}
			now=wal[a].r;
			}
		if ( now!=len )
			{
			++all;
			wal[all].l=now;
			wal[all].r=len;
			wal[all].s=0;
			}
		sort ( wal+1,wal+1+all,cmp );
		double res=ti,ans=0,ll;
		for ( int a=1; a<=all; ++a )
			{
			//	printf("[%d]",wal[a].s);
			ll=wal[a].r-wal[a].l;
			if ( ll/ ( r+wal[a].s ) <=res )
				{
				res-=ll/ ( r+wal[a].s );
				ans+=ll/ ( r+wal[a].s );
				}
			else
				{
				ll-= ( r+wal[a].s ) *res;
				ans+=res;
				res=0;
				////////
				ans+=ll/ ( wal[a].s+sp );
				}
			}
		printf ( "Case #%d: %.10lf\n",z,ans );
		}
		return 0;
	}
