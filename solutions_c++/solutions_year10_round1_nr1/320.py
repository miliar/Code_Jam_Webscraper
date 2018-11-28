#include<iostream>
using namespace std;
char b[50][51];
int main()
{
	int a,s,n,k,c,mxc,R,B,t;
int _,T;
scanf("%d",&T);
for(_=1;_<=T;_++)
{
	scanf("%d%d",&n,&k);
	for(a=0;a<n;a++) scanf("%s",b[a]);
	for(a=0;a<n;a++)
	{
		for(s=0;s<n/2;s++){ t=b[a][s]; b[a][s]=b[a][n-1-s]; b[a][n-1-s]=t; }
		c=0;
		for(s=0;s<n;s++)
		{
			if( b[a][s]!='.' )
			{
				b[a][c]=b[a][s];
				if( s!=c ) b[a][s]='.';
				c++;
			}
		}
//printf("%s\n",b[a]);
	}
	mxc=0;
	for(a=0;a<n;a++)
	{
		c=0;
		for(s=0;s<n;s++)
		{
			if( b[a][s]=='.' || b[a][s]=='B' ) c=0;
			else{ c++; if( c>mxc ) mxc=c; }
		}
	}
	for(s=0;s<n;s++)
	{
		c=0;
		for(a=0;a<n;a++)
		{
			if( b[a][s]=='.' || b[a][s]=='B' ) c=0;
			else{ c++; if( c>mxc ) mxc=c; }
		}
	}
	for(a=-n+1;a<n;a++)
	{
		c=0;
		for(s=max(0,-a);s<min(n,n-a);s++)
		{
//printf("%d %d %c\n",a,a+s,b[a][a+s]);
			if( b[a+s][s]=='.' || b[a+s][s]=='B' ) c=0;
			else{ c++; if( c>mxc ) mxc=c; }
		}
//printf("\n");
	}
	for(a=0;a<n+n-1;a++)
	{
		c=0;
		for(s=max(0,a-n+1);s<min(n,a+1);s++)
		{
			if( b[a-s][s]=='.' || b[a-s][s]=='B' ) c=0;
			else{ c++; if( c>mxc ) mxc=c; }
		}
	}
	R=mxc;
	mxc=0;
	for(a=0;a<n;a++)
	{
		c=0;
		for(s=0;s<n;s++)
		{
			if( b[a][s]=='.' || b[a][s]=='R' ) c=0;
			else{ c++; if( c>mxc ) mxc=c; }
		}
	}
	for(s=0;s<n;s++)
	{
		c=0;
		for(a=0;a<n;a++)
		{
			if( b[a][s]=='.' || b[a][s]=='R' ) c=0;
			else{ c++; if( c>mxc ) mxc=c; }
		}
	}
	for(a=-n+1;a<n;a++)
	{
		c=0;
		for(s=max(0,-a);s<min(n,n-a);s++)
		{
			if( b[a+s][s]=='.' || b[a+s][s]=='R' ) c=0;
			else{ c++; if( c>mxc ) mxc=c; }
		}
	}
	for(a=0;a<n+n-1;a++)
	{
		c=0;
		for(s=max(0,a-n+1);s<min(n,a+1);s++)
		{
			if( b[a-s][s]=='.' || b[a-s][s]=='R' ) c=0;
			else{ c++; if( c>mxc ) mxc=c; }
		}
	}
	B=mxc;
//printf("%d %d\n",R,B);
	if( R>=k && B>=k ) printf("Case #%d: Both\n",_);
	else if( R>=k ) printf("Case #%d: Red\n",_);
	else if( B>=k ) printf("Case #%d: Blue\n",_);
	else printf("Case #%d: Neither\n",_);
}
	return 0;
}
