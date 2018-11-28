// problem1.cpp : Defines the entry point for the console application.
//

#include<stdio.h>


bool firstLine = true; 
char getencode(char ch)
{
	char tempchar = NULL;
	switch(ch)
	{
	case 'a':tempchar = 'y';
		break;
	case 'b' :tempchar = 'h';
		break;
	case 'c':tempchar = 'e';
		break;
	case 'd':tempchar = 's';
		break;
	case 'e':tempchar = 'o';
		break;
	case 'f':tempchar = 'c';
		break;
	case 'g':tempchar = 'v';
		break;
	case 'h':tempchar = 'x';
		break;
	case 'i':tempchar = 'd';
		break;
	case 'j':tempchar = 'u';
		break;
	case 'k':tempchar = 'i';
		break;
	case 'l':tempchar = 'g';
		break;
	case 'm':tempchar = 'l';
		break;
	case 'n':tempchar = 'b';
		break;
	case 'o':tempchar = 'k';
		break;
	case 'p':tempchar = 'r';
		break;
	case 'q':tempchar = 'z';
		break;
	case 'r':tempchar = 't';
		break;
	case 's':tempchar = 'n';
		break;
	case 't':tempchar = 'w';
		break;
	case 'u':tempchar = 'j';
		break;
	case 'v':tempchar = 'p';
		break;
	case 'w':tempchar = 'f';
		break;
	case 'x':tempchar = 'm';
		break;
	case 'y':tempchar = 'a';
		break;
	case 'z':tempchar = 'q';
		break;
	case ' ':tempchar = ' ';
		break;
	case '\n':tempchar = '\n';
		break;
	default :
		tempchar = ' ';
	}
	return tempchar;
}

int main()
{
	FILE * file = fopen("A-small-attempt5.in", "r");
	char buffer[9];
	if(!file)
		return -1;
	char buf[2]; 

	fgets(buf,sizeof(int),file);
		int noLines =(int)(buf[0] - 48) * 10 ;
		noLines =noLines + (buf[1] - 48);

	
	
	
	
	FILE * optputFile = fopen("output.txt","w");
	if(!optputFile)
		return -1;


	char indexChar = '1';
	int index = 1;
	while(!feof(file))
	{
		char tempchar;
		if(!firstLine)
		 tempchar = getc(file);
		if( tempchar == '\n' || firstLine )
		{
			if(firstLine)
			{
				fseek(optputFile,0,SEEK_SET);
				
			}
			else
			{
				char temp = getencode(tempchar);
				putc(temp,optputFile );
			}
			 firstLine =false;
		

			sprintf(buffer,"Case #%d: ",index);
			
			
			
			
			if(index  <= noLines )
				fputs(buffer,optputFile);
			index++;
			indexChar ++;
		}
		else
		{
			char temp = getencode(tempchar);
			putc(temp,optputFile );
		}
		
	
	}
	fclose(file);
	fclose(optputFile);

	
}

