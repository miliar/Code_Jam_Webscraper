#include <stdio.h>
#include <string.h>

FILE *fin=fopen("a.in","r"),
	*fout=fopen("a.out","w");//stdout;

char a[26];

int main()
{
	int i,t;
	char s[1000];
	fscanf(fin,"%d",&t);
	fgets(s,1000,fin);
	strcpy(a,"yhesocvxduiglbkrztnwjpfmaq");
	for (i=1; i<=t; ++i)
	{
		fprintf(fout,"Case #%d: ",i);
		fgets(s,1000,fin);
		int len=strlen(s);
		for (int j=0; j<len; ++j)
		{
			if ((s[j]==' ')||(s[j]=='\n'))
				fprintf(fout,"%c",s[j]);
			else fprintf(fout,"%c",a[s[j]-'a']);
		}
	}
	fprintf(fout,"\n");
	fclose(fin);
	fclose(fout);
	return 0;
}