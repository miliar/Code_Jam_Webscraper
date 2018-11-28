#include<stdio.h>
FILE *in,*out,*dbg;
long long i[16384];
int n;
long long j,k;
long long p[1048576][2];
int c;
long long o;
void dfs(long long x,int r)
{
	int a;
	if( r==c )
	{
		if( j<=x && x<=k )
		{
			if( o==-1 || x<o )
			{
				for(a=0;a<n;a++) if( x%i[a]!=0 && i[a]%x!=0 ) return;
				o=x;
			}
		}
		return;
	}
	dfs(x,r+1);
	for(a=0;a<p[r][1];a++)
	{
		x*=p[r][0];
		dfs(x,r+1);
	}
}
long long gcd(long long x,long long y)
{
	if( x==0 ) return y;
	if( y==0 ) return x;
	if( x>=y ) return gcd(y,x%y);
	return gcd(x,y%x);
}
int main()
{
	in =fopen("c.in" ,"r");
	out=fopen("d.out","w");
//	dbg=fopen("debug.txt","w");
	int tests,test;
	int a,s,d;
	long long x,y,z;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fscanf(in,"%d%I64d%I64d",&n,&j,&k);
		for(a=0;a<n;a++)
		{
			fscanf(in,"%I64d",&i[a]);
		}
		fprintf(out,"Case #%d: ",test+1);
		for(;j<=k;j++)
		{
			for(a=0;a<n;a++)
			{
				if( i[a]%j!=0 && j%i[a]!=0 ) break;
			}
			if( a==n )
			{
				fprintf(out,"%I64d\n",j);
				break;
			}
		}
		if( j==k+1 ) fprintf(out,"NO\n");
	}
	return 0;
}