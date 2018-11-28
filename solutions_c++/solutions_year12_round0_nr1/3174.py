#include <stdio.h>
#include <string.h>

void main()
{
	FILE *infp = fopen("input.txt","r");
	FILE *outfp = fopen("output.txt","w");

	char s[] ="yhesocvxduiglbkrztnwjpfmaq";
	char string[120]={0,};
	int i,j,k;
	int l;

	int T;

	fscanf(infp,"%d ",&T);

	for(i=1;i<=T;i++)
	{
		fgets(string,120,infp);
		l = strlen(string);
		fprintf(outfp,"Case #%d: ",i);
		for(j=0;j<l;j++)
		{
			if(string[j] == ' ')
			{
				fprintf(outfp," ");
				continue;
			}
			else if(string[j] == 10) continue;
			fprintf(outfp,"%c",s[ string[j] - 'a']);
		}
		fprintf(outfp,"\n");
	}
}