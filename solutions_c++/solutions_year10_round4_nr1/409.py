#include<stdio.h>
#include<string.h>

FILE *in,*out,*dbg;
void io()
{
	in =fopen("a.in" ,"r");
	out=fopen("a.out","w");
//	dbg=fopen("debug.txt","w");
}
long long abs(long long x) { if( x<0 ) return -x; return x; }

int n;
int i[128][128];

bool check(int p,int q,int x,int y)
{
	int z,w;
	z=p-x;
	w=q-y;
	if( x>=0 && x<n && y>=0 && y<n )
		if( z>=0 && z<n && w>=0 && w<n )
			if( i[x][y]!=i[z][w] ) return false;
	z=y+(p-q)/2;
	w=x+(q-p)/2;
	if( x>=0 && x<n && y>=0 && y<n )
		if( z>=0 && z<n && w>=0 && w<n )
			if( i[x][y]!=i[z][w] ) return false;
	z=(p+q)/2-y;
	w=(p+q)/2-x;
	if( x>=0 && x<n && y>=0 && y<n )
		if( z>=0 && z<n && w>=0 && w<n )
			if( i[x][y]!=i[z][w] ) return false;
	return true;
}

int main()
{
	io();
	int tests,test;
	int x,y,t,v,o;
	int a,s,d,f;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fscanf(in,"%d",&n);
		for(a=0;a<n;a++) for(s=0;s<=a;s++) fscanf(in,"%d",&i[s][n-1-a+s]);
		for(a=1;a<n;a++) for(s=0;s<n-a;s++) fscanf(in,"%d",&i[a+s][s]);
//for(a=0;a<n;a++) { for(s=0;s<n;s++) fprintf(out,"%d ",i[a][s]); fprintf(out,"\n"); }
		o=n*4;
		//for(a=-1;a<n*2;a++) for(s=(a+1)%2-1;s<n*2;s+=2)
		for(a=-n*2;a<n*4;a++) for(s=-n*2;s<n*4;s++)
		{
			if( (a+s+n*4)%2!=0 ) continue;
			t=1;
			for(d=(a+n*2)%2;d<=n*2;d+=2)
			{
				for(x=(a-d)/2;x<=(a+d)/2;x++)
				{
					y=(s-d)/2;
					if( !check(a,s,x,y) ) { t=0; break; }
				}
				for(x=(a-d)/2;x<=(a+d)/2;x++)
				{
					y=(s+d)/2;
					if( !check(a,s,x,y) ) { t=0; break; }
				}
				for(y=(s-d)/2;y<=(s+d)/2;y++)
				{
					x=(a-d)/2;
					if( !check(a,s,x,y) ) { t=0; break; }
				}
				for(y=(s-d)/2;y<=(s+d)/2;y++)
				{
					x=(a+d)/2;
					if( !check(a,s,x,y) ) { t=0; break; }
				}
			}
			if( t==1 )
			{
				d=(a>=n?a+1:n*2-1-a);
				f=(s>=n?s+1:n*2-1-s);
				v=(d>f?d:f); if( v<o ) o=v;
			}
		}
		fprintf(out,"Case #%d: ",test+1);
		fprintf(out,"%d\n",o*o-n*n);
	}
	return 0;
}