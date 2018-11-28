// code jam A.cpp: archivo de proyecto principal.


#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

char Cadena[200];
char Sol[200];

char Valorverdadero(char c)
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
	int cont;
	scanf("%d\n",&n);
	cont=1;
	while(n!=0)
	{
		memset(Cadena,0,sizeof(Cadena));
		memset(Sol,0,sizeof(Sol));
		gets(Cadena);
		for(int i=0;i<strlen(Cadena);i++)
		{
			if(Cadena[i]!=' ')
			{
				Sol[i]=Valorverdadero(Cadena[i]);
			}
			else 
				Sol[i]=' ';
		}
		printf("Case #%d: ",cont);
		for(int i=0;i<strlen(Cadena);i++)//
			printf("%c",Sol[i]);
		printf("\n");
		cont++;
		n--;
	}
    return 0;
}
