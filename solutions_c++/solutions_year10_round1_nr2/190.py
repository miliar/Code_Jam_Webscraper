#include<stdio.h>

FILE *in,*out,*dbg;
void io()
{
	in =fopen("b.in" ,"r");
	out=fopen("b.out","w");
	dbg=fopen("debug.txt","w");
}
int max(int x,int y) { if( x>y ) return x; return y; }
int min(int x,int y) { if( x<y ) return x; return y; }
int abs(int x) { if( x>0 ) return x; return -x; }

int inf=100000000;
int i[1024];
int b[1024][1024];

int main()
{
	io();
	int k;
	int n,m;
	int c0,c1;
	int v,o;
	int a,s,d,f;
	fscanf(in,"%d",&k);
	for(a=0;a<k;a++)
	{
		fscanf(in,"%d%d%d%d",&c0,&c1,&m,&n);
		for(s=0;s<n;s++) fscanf(in,"%d",&i[s]);
		for(s=0;s<256;s++) b[0][s]=0;
		for(s=0;s<n;s++)
		{
			for(d=0;d<256;d++) b[s+1][d]=inf;
			for(d=0;d<256;d++)
			{
				for(f=0;f<256;f++)
				{
					v=b[s][f] + (abs(d-f)<=m?abs(d-i[s]):inf);
					if( v<b[s+1][d] ) b[s+1][d]=v;
					v=b[s][f] + (m==0?(d-f==0?0:inf):c1*(abs(d-f)>m?(abs(d-f)-1)/m:0)) + abs(d-i[s]);
					if( v<b[s+1][d] ) b[s+1][d]=v;
				}
				v=b[s][d]+c0;
				if( v<b[s+1][d] ) b[s+1][d]=v;
			}
			for(d=0;d<256;d++) if( b[s+1][d]>inf ) b[s+1][d]=inf;
		}
		o=inf;
		for(s=0;s<256;s++) if( b[n][s]<o ) o=b[n][s];
		fprintf(out,"Case #%d: ",a+1);
		fprintf(out,"%d\n",o);
	}
	return 0;
}