#include<stdio.h>
#include<string.h>

FILE *in=stdin;
FILE *out=stdout;
FILE *dbg=stderr;
void file()
{
	in =fopen("0b.in" ,"r");
	out=fopen("0b.out","w");
	//dbg=out;
	//dbg=fopen("debug.txt","w");
}
int len(char* x) { return strlen(x); }

int i[256][256];
int j[256][256];
char o[256][256];

char c;

char test(int x,int y)
{
	if( o[x][y]!=-1 ) return o[x][y];
	if( j[x][y]==0 ) o[x][y]=test(x-1,y);
	if( j[x][y]==1 ) o[x][y]=test(x,y-1);
	if( j[x][y]==2 ) o[x][y]=test(x,y+1);
	if( j[x][y]==3 ) o[x][y]=test(x+1,y);
	if( j[x][y]==-1 )
	{
		o[x][y]=c;
		c++;
	}
	return o[x][y];
}

int main()
{
	int k,m,n;
	int t,l;
	int x,y,z;
	int a,s,d,f;
	file();
	fscanf(in,"%d",&k);
	for(a=0;a<k;a++)
	{
		fscanf(in,"%d%d",&m,&n);
		for(s=0;s<m;s++) for(d=0;d<n;d++) fscanf(in,"%d",&i[s][d]);
		for(s=0;s<m;s++) for(d=0;d<n;d++)
		{
			j[s][d]=-1;
			o[s][d]=-1;
		}
		for(s=0;s<m;s++) for(d=0;d<n;d++)
		{
			l=i[s][d];
			if( s-1>=0 ) { t=i[s-1][d]; if( t<l ) { l=t; z=0; } }
			if( d-1>=0 ) { t=i[s][d-1]; if( t<l ) { l=t; z=1; } }
			if( d+1< n ) { t=i[s][d+1]; if( t<l ) { l=t; z=2; } }
			if( s+1< m ) { t=i[s+1][d]; if( t<l ) { l=t; z=3; } }
			if( l<i[s][d] ) j[s][d]=z;
		}
		c='a';
		for(s=0;s<m;s++) for(d=0;d<n;d++) test(s,d);
		fprintf(out,"Case #%d:\n",a+1);
		for(s=0;s<m;s++) { for(d=0;d<n;d++) fprintf(out,"%c ",o[s][d]); fprintf(out,"\n"); }
	}
	return 0;
}