#include<stdio.h>
#include<string.h>

FILE *in=stdin;
FILE *out=stdout;
FILE *dbg=stderr;
void file()
{
	in =fopen("0c.in" ,"r");
	out=fopen("0c.out","w");
	//dbg=out;
	dbg=fopen("debug.txt","w");
}
int len(char* x) { return strlen(x); }

char i[16384];
char j[32]="welcome to code jam";
int b[2][16384];

int main()
{
	file();
	int k,m,n;
	int a,s,d;
	n=len(j);
	fscanf(in,"%d",&k);
	for(a=0;a<k;a++)
	{
		fscanf(in," %[^\n]s",&i);
		m=len(i);
		b[0][0]=1;
		for(s=1;s<=n;s++) b[0][s]=0;
		for(s=0;s<m;s++)
		{
			for(d=0;d<=n;d++) b[1-s%2][d]=b[s%2][d];
			for(d=0;d<n;d++)
			{
				if( i[s]==j[d] )
				{
//fprintf(dbg,"%d:%c %d",d,i[d])
					b[1-s%2][d+1]+=b[s%2][d];
					b[1-s%2][d+1]%=10000;
				}
fprintf(dbg,"%d ",b[1-s%2][d+1]);
			}
fprintf(dbg,"\n");
		}
fprintf(dbg,"\n");
		fprintf(out,"Case #%d: ",a+1);
		fprintf(out,"%04d\n",b[m%2][n]);
	}
	return 0;
}