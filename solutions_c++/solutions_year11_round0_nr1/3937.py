#include <stdio.h>
#include <stdlib.h>

FILE *fin=fopen("a1.in","r"),
	*fout=fopen("a1.out","w");

int result=0;

int main()
{
	int i,j,n,t,p1,p2,p,last1,last2;
	char c;
	fscanf(fin,"%d",&t);
	for (i=1; i<=t; ++i)
	{
		result=0;
		p1=p2=1;		
		last1=last2=0;
		fscanf(fin,"%d",&n);
		for (j=1; j<=n; ++j)
		{
			do{
				fscanf(fin,"%c",&c);
			}while ((c!='O')&&(c!='B'));
			fscanf(fin,"%d", &p);
			if (c=='O')
			{
				if (last1+abs(p1-p)+1<=result+1)
				{
					++result;
					last1=result;
				}
				else result=last1=last1+abs(p1-p)+1;
				p1=p;
			}
			else {
				if (last2+abs(p2-p)+1<=result+1)
				{
					++result;
					last2=result;
				}
				else result=last2=last2+abs(p2-p)+1;
				p2=p;
			}
		}
		fprintf(fout,"Case #%d: %d\n",i,result);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}