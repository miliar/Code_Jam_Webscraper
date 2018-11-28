#include<stdio.h>
#include<string.h>

FILE *in=stdin;
FILE *out=stdout;
FILE *dbg=stderr;
void file()
{
	in =fopen("0a.in" ,"r");
	out=fopen("0a.out","w");
	//dbg=out;
	//dbg=fopen("debug.txt","w");
}
int len(char* x) { return strlen(x); }

char i[16384][64];
char j[64*32];

int main()
{
	file();
	int n,k,l;
	int t,o;
	char c;
	int a,s,d,f;
	fscanf(in,"%d%d%d",&l,&n,&k);
	for(a=0;a<n;a++) fscanf(in,"%s",&i[a]);
	for(a=0;a<k;a++)
	{
		fscanf(in,"%s",&j);
		o=0;
		for(s=0;s<n;s++)
		{
			t=1;
			f=0;
			for(d=0;d<l;d++)
			{
				c=i[s][d];
				if( j[f]=='(' )
				{
					for(f++;j[f]!=')';f++) if( c==j[f] ) break;
					if( c!=j[f] ) { t=0; break; }
					for(f++;j[f]!=')';f++); f++;
				}
				else
				{
					if( c!=j[f] ) { t=0; break; }
					f++;
				}
			}
			o+=t;
		}
		fprintf(out,"Case #%d: %d\n",a+1,o);
	}
	return 0;
}