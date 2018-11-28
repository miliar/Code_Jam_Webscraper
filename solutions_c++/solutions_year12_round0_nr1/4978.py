// code jam A.cpp: archivo de proyecto principal.

#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

char Cadena[200];
char CadFinal[200];

char DevuelveLetra(char c)
{
	char Val;
	switch(c)
	{
		case 'a': Val='y'; break;
		case 'b': Val='h'; break;
		case 'c': Val='e'; break;
		case 'd': Val='s'; break;
		case 'e': Val='o'; break;
		case 'f': Val='c'; break;
		case 'g': Val='v'; break;
		case 'h': Val='x'; break;
		case 'i': Val='d'; break;
		case 'j': Val='u'; break;
		case 'k': Val='i'; break;
		case 'l': Val='g'; break;
		case 'm': Val='l'; break;
		case 'n': Val='b'; break;
		case 'o': Val='k'; break;//
		case 'p': Val='r'; break;
//no hay q
		case 'r': Val='t'; break;
		case 't': Val='w'; break;
		case 's': Val='n'; break;
		case 'u': Val='j'; break;
		case 'v': Val='p'; break;
		case 'w': Val='f'; break;
		case 'x': Val='m'; break;
		case 'y': Val='a'; break;
		

		case 'z': Val='q'; break;//<----
		case 'q': Val='z'; break;
	}

	return Val;

}

int main()
{
    int n;

	scanf("%d\n",&n);

	for(int j=1;j<=n;j++)
	{
		memset(Cadena,0,sizeof(Cadena));
		memset(CadFinal,0,sizeof(CadFinal));
		gets(Cadena);
		for(int i=0;i<strlen(Cadena);i++)
		{
			if(Cadena[i]!=' ')
			{
				CadFinal[i]=DevuelveLetra(Cadena[i]);
			}
			else 
				CadFinal[i]=' ';
		}

		printf("Case #%d: ",j);
		for(int i=0;i<strlen(Cadena);i++)//
			printf("%c",CadFinal[i]);

		printf("\n");

	}
    return 0;
}
