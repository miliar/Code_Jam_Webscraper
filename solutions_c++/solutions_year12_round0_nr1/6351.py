#include <stdio.h>
#include <string.h>

void main()
{
	FILE *in,*out;;
	in=fopen("A-small-attempt1.in","r");
	out=fopen("A-Real.out","w");

	int a,b,T;
	char S[32][102];

	fscanf(in,"%d",&T);fflush(stdin);

	for(a=0;a<=T;a++)
	{
		fgets(S[a],102,in);
		for(b=0;b<=strlen(S[a]);b++)
		{
			switch(S[a][b])
			{
			case 'a': S[a][b]='y'; break;
			case 'b': S[a][b]='h'; break;
			case 'c': S[a][b]='e'; break;
			case 'd': S[a][b]='s'; break;
			case 'e': S[a][b]='o'; break;

			case 'f': S[a][b]='c'; break;
			case 'g': S[a][b]='v'; break;
			case 'h': S[a][b]='x'; break;
			case 'i': S[a][b]='d'; break;
			case 'j': S[a][b]='u'; break;

			case 'k': S[a][b]='i'; break;
			case 'l': S[a][b]='g'; break;
			case 'm': S[a][b]='l'; break;
			case 'n': S[a][b]='b'; break;
			case 'o': S[a][b]='k'; break;

			case 'p': S[a][b]='r'; break;
			case 'q': S[a][b]='z'; break;
			case 'r': S[a][b]='t'; break;
			case 's': S[a][b]='n'; break;
			case 't': S[a][b]='w'; break;

			case 'u': S[a][b]='j'; break;
			case 'v': S[a][b]='p'; break;
			case 'w': S[a][b]='f'; break;
			case 'x': S[a][b]='m'; break;
			case 'y': S[a][b]='a'; break;

			case 'z': S[a][b]='q'; break;
			}
			
		}
		if(a!=0) fprintf(out,"Case #%d: %s",a,S[a]);
	}
}