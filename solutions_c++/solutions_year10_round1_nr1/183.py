#include<stdio.h>

FILE *in,*out,*dbg;
void io()
{
	in =fopen("a.in" ,"r");
	out=fopen("a.out","w");
	dbg=fopen("debug.txt","w");
}

char i[1024][1024];

int main()
{
	io();
	int k;
	int n,c;
	int x,y;
	bool red,blue;
	int a,s,d,f,g,h;
	fscanf(in,"%d",&k);
	for(a=0;a<k;a++)
	{
		fscanf(in,"%d%d",&n,&c);
		for(s=0;s<n;s++) for(d=0;d<n;d++) fscanf(in," %c",&i[s][d]);
		for(s=0;s<n;s++)
		{
			f=n-1;
			for(d=n-1;d>=0;d--)
			{
				if( i[s][d]!='.' ) { i[s][f]=i[s][d]; f--; }
			}
			for(;f>=0;f--) i[s][f]='.';
		}
		red=false;
		blue=false;
		for(s=0;s<n;s++) for(d=0;d<n;d++)
		{
			for(f=-1;f<=1;f++) for(g=-1;g<=1;g++)
			{
				if( f==0 && g==0 ) continue;
				for(h=1;h<c;h++)
				{
					x=s+f*h;
					y=d+g*h;
					if( x<0 || y<0 || x>=n || y>=n ) break;
					if( i[x][y]!=i[s][d] ) break;
				}
				if( h==c )
				{
					if( i[s][d]=='R' ) red=true;
					if( i[s][d]=='B' ) blue=true;
				}
			}
		}
		fprintf(out,"Case #%d: ",a+1);
		if( red&&blue ) fprintf(out,"Both");
		if( red&&!blue ) fprintf(out,"Red");
		if( !red&&blue ) fprintf(out,"Blue");
		if( !red&&!blue ) fprintf(out,"Neither");
		fprintf(out,"\n");
	}
	return 0;
}