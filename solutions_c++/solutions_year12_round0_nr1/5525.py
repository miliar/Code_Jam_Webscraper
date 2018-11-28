// SpeakinginTongues.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "stdlib.h"
#include "string.h"
#include <List>
using std::list;

void swapchar(char* src,char* des)
{
	while(*src!='\0')
	{
		if (*src==' ')
		{
			*des=' ';
			src++;
			des++;
			continue;
		}
		switch(*src)
		{	
		case 'a':*des='y';break;
		case 'b':*des='h';break;	
		case 'c':*des='e';break;
		case 'd':*des='s';break;	
		case 'e':*des='o';break;
		case 'f':*des='c';break;
		case 'g':*des='v';break;
		case 'h':*des='x';break;	
		case 'i':*des='d';break;
		case 'j':*des='u';break;	
		case 'k':*des='i';break;
		case 'l':*des='g';break;
		case 'm':*des='l';break;
		case 'n':*des='b';break;	
		case 'o':*des='k';break;
		case 'p':*des='r';break;	
		case 'q':*des='z';break;
		case 'r':*des='t';break;
		case 's':*des='n';break;
		case 't':*des='w';break;
		case 'u':*des='j';break;
		case 'v':*des='p';break;	
		case 'w':*des='f';break;
		case 'x':*des='m';break;	
		case 'y':*des='a';break;
		case 'z':*des='q';break;
		case '\n':*des='\n';break;
		}
		src++;
		des++;
	}
	
	*des='\0';
	
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *source_file=fopen("E:\\googlejam\\A-small-attempt3.in","r");
	FILE *destination_file=fopen("E:\\googlejam\\Output.txt","w");
	char buffer[102];
	fgets(buffer,102,source_file);
	int col=atoi(buffer);

	for(int i=1;i<=col;i++)
	{
		char output[102],size[4];
		strcpy(output,"Case #");

		sprintf(size,"%d: ",i);
		strcat(output,size);
		fwrite(output,strlen(output),1,destination_file);
		memset(buffer,0,102);
		fgets(buffer,102,source_file);
		swapchar(buffer,output);
		fputs(output,destination_file);
		
	}
	fclose(source_file);
	fclose(destination_file);
	return 0;
}

