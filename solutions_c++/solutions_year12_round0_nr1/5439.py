// Google01.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

char enc[]="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
char dec[]="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
char map[] ="yhesocvxduiglbkrqtnwjpfmaz";
char map2[]="yhesocvxduiglbkrztnwjpfmaq";
char decrypt(char c)
{
	return map2[c-'a'];
}
int main(int argc, char* argv[])
{
	char cLetter = 0;
	FILE * fp = fopen("A-small-attempt1.in","r");
	fseek(fp,0,0);
	int line = 0, lines = 0;
	//printf("Case #1: ");
	fscanf(fp,"%d",&lines);
	while(!feof(fp))
	{
		cLetter = fgetc(fp);
		if( cLetter>='a' && cLetter<='z')
		{
			printf("%c",decrypt(cLetter));
		}
		else if( cLetter=='\n' )
		{
			line++;
			if(line!=1)
				printf("\n");
			printf("Case #%d: ",line);
		}
		else
		{
			printf("%c",cLetter);
		}
	}
	getchar();
	return 0;
}
