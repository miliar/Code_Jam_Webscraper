#include<stdio.h>
#include<string.h>
#include<vector.h>

FILE *in,*out,*dbg;
void io()
{
	in =fopen("a.in" ,"r");
	out=fopen("a.out","w");
	dbg=fopen("debug.txt","w");
}
long long abs(long long x) { if( x<0 ) return -x; return x; }
int len(char* x) { return strlen(x); }

int i[1024];

int main()
{
	io();
	int k;
	char j;
	int n,t,o;
	int a,s,d,f;
	fscanf(in,"%d",&k);
	for(a=0;a<k;a++)
	{
		fscanf(in,"%d",&n);
		for(s=0;s<n;s++)
		{
			t=-1;
			for(d=0;d<n;d++)
			{
				fscanf(in," %c",&j);
				if( j=='1' ) t=d;
			}
			i[s]=t;
		}
		o=0;
		for(s=0;s<n;s++)
		{
			for(d=s;d<n;d++)
			{
				if( i[d]<=s )
				{
					o+=d-s;
					t=i[d];
					for(f=d;f>s;f--) i[f]=i[f-1];
					i[s]=t;
					break;
				}
			}
		}
		fprintf(out,"Case #%d: ",a+1);
		fprintf(out,"%d\n",o);
	}
	return 0;
}