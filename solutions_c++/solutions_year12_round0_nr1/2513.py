#include<stdio.h>
#include<string.h>
FILE *in,*out;
char g[32]="yhesocvxduiglbkrztnwjpfmaq";
char i[1024],j;
int main()
{
	in =fopen("a.in" ,"r");
	out=fopen("a.out","w");
	int tests,test;
	int a;
	fscanf(in,"%d",&tests);
	fscanf(in,"%[^\n]s",&i); fscanf(in,"%c",&j);
	for(test=0;test<tests;test++)
	{
		fprintf(out,"Case #%d: ",test+1);
		fscanf(in,"%[^\n]s",&i); fscanf(in,"%c",&j);
		for(a=0;a<strlen(i);a++) fprintf(out,"%c",(i[a]>='a'&&i[a]<='z'?g[i[a]-'a']:i[a]));
		fprintf(out,"\n");
	}
	return 0;
}