#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define maxLength 101
#define PAUSE (printf("\n  ")|system("pause"))

char* translate(char *Str)
{
	for(int i = 0; i < strlen(Str); i++)
	{
		switch(Str[i])
		{
		case 'a':
			Str[i] += 24; break;
		case 'b':
			Str[i] += 6; break;
		case 'c':
			Str[i] += 2; break;
		case 'd':
			Str[i] += 15; break;
		case 'e':
			Str[i] += 10; break;
		case 'f':
			Str[i] -= 3; break;
		case 'g':
			Str[i] += 15; break;
		case 'h':
			Str[i] += 16; break;
		case 'i':
			Str[i] -= 5; break;
		case 'j':
			Str[i] += 11; break;
		case 'k':
			Str[i] -= 2; break;
		case 'l':
			Str[i] -= 5; break;
		case 'm':
			Str[i] -= 1; break;
		case 'n':
			Str[i] -= 12; break;
		case 'o':
			Str[i] -= 4; break;
		case 'p':
			Str[i] += 2; break;
		case 'q':
			Str[i] += 9; break;
		case 'r':
			Str[i] += 2; break;
		case 's':
			Str[i] -= 5; break;
		case 't':
			Str[i] += 3; break;
		case 'u':
			Str[i] -= 11; break;
		case 'v':
			Str[i] -= 6; break;
		case 'w':
			Str[i] -= 17; break;
		case 'x':
			Str[i] -= 11; break;
		case 'y':
			Str[i] -= 24; break;
		case 'z':
			Str[i] -= 9; break;
		default:
			break;
		}
	}
	return Str;
}

int main()
{
	char str[maxLength], **G;
	printf("\n  Number of test cases: ");
	int T = atoi(gets(str));
	while(T > 30 || T < 1)
	{
		system("cls");
		printf("\n  Number of test cases: ");
		T = atoi(gets(str));
	}
	G = new char*[T];
	for(int i = 0; i < T; i++)
	{
		printf("  Case #%d: ", i+1);
		gets(str);
		char *pG = new char[strlen(str)+1];
		strcpy(pG, str);
		G[i] = pG;
	}
	printf("\n");
	for(int i = 0; i < T; i++)
		printf("  Case #%d: %s\n", i+1, translate(G[i]));
	PAUSE;
	return 0;
}