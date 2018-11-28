#include<stdio.h>
#include<ctype.h>

FILE *f = fopen("goglerese.in","r");
FILE *g = fopen("goglerese.out","w");

#define MaxN 300

int T;
char S[MaxN];
char Negativ[] = "yhesocvxduiglbkrztnwjpfmaq ";

void Rezolva(void)
{
	for(int i=0;S[i];i++)
		if(isalpha(S[i]))
			S[i] = Negativ[S[i]-'a'];
}

int main()
{
	fscanf(f,"%d\n",&T);
	for(int i=1;i<=T;i++)
	{
		fgets(S,sizeof(S),f);
		Rezolva();
		fprintf(g,"Case #%d: %s",i,S);
	}
}