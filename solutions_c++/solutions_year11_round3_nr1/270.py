#include<stdio.h>
#include<string.h>
#include<vector.h>
FILE *in,*out,*dbg;
char i[256][256];
int main()
{
	in =fopen("a.in" ,"r");
	out=fopen("a.out","w");
//	dbg=fopen("debug.txt","w");
	int tests,test;
	int m,n,a,s,d;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fscanf(in,"%d%d",&m,&n);
		for(a=0;a<m;a++) for(s=0;s<n;s++) fscanf(in," %c",&i[a][s]);
		d=1;
		for(a=0;a<m;a++) for(s=0;s<n;s++)
		{
			if( i[a][s]=='#' )
			{
				if( a+1<m && s+1<n && i[a][s+1]=='#' && i[a+1][s]=='#' && i[a+1][s+1]=='#' )
				{
					i[a][s]='/';
					i[a][s+1]='\\';
					i[a+1][s]='\\';
					i[a+1][s+1]='/';
				}
				else
				{
					d=0;
					a=m;
					break;
				}
			}
		}
		fprintf(out,"Case #%d: ",test+1);
		if( d==1 )
		{
			fprintf(out,"\n");
			for(a=0;a<m;a++)
			{
				for(s=0;s<n;s++) fprintf(out,"%c",i[a][s]);
				fprintf(out,"\n");
			}
		}
		else
		{
			fprintf(out,"\nImpossible\n");
		}
	}
	return 0;
}