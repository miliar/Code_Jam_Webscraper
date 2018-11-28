#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *fin=fopen("a2.in","r"),
	*fout=fopen("a2.out","w");

char result[200];
int n,ctop,dtop;
char cb[100][10],dl[100][10];

int main()
{
	int w,i,j,k,t;
	char s[1000];
	fscanf(fin,"%d",&t);
	for (w=1; w<=t; ++w)
	{
		fscanf(fin,"%d",&ctop);
		for (i=1; i<=ctop; ++i)
			fscanf(fin,"%s",cb[i]);
		fscanf(fin,"%d",&dtop);
		for (i=1; i<=dtop; ++i)
			fscanf(fin,"%s",dl[i]);
		fscanf(fin,"%d%s",&i, s);
		n=0;
		for (i=0; i<strlen(s); ++i)
		{
			if (n==0)
			{
				result[++n]=s[i];
				continue;
			}
			//combine
			bool once=false;
			for (j=1; j<=ctop; ++j)
			{
				if (((result[n]==cb[j][0])&&(s[i]==cb[j][1]))||((result[n]==cb[j][1])&&(s[i]==cb[j][0])))
				{
					result[n]=cb[j][2];
					once=true;
					break;					
				}
			}
			if (once)
				continue;

			//delete
			once=false;
			for (j=1; j<=dtop; ++j)
			{
				for (k=1; k<=n; ++k)
					if (((result[k]==dl[j][0])&&(s[i]==dl[j][1]))||((result[k]==dl[j][1])&&(s[i]==dl[j][0])))
					{
						once=true;
						n=0;
						break;
					}
			}
			if (!once)
				result[++n]=s[i];
		}
	
		fprintf(fout,"Case #%d: [", w);
		for (i=1; i<=n; ++i)
		{
			if (i>1)
				fprintf(fout,", ");
			fprintf(fout,"%c",result[i]);
		}
		fprintf(fout,"]\n");
	}
	fclose(fin);
	fclose(fout);
	return 0;
}