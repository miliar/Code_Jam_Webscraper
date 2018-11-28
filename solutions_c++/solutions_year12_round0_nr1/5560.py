#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char utog(char x)
{
switch (x)
	{
	case 'a':
		return 'y';
	case 'b':
		return 'h';
	case 'c':
		return 'e';
	case 'd':
		return 's';
	case 'e':
		return 'o';
	case 'f':
		return 'c';
	case 'g':
		return 'v';
	case 'h':
		return 'x';
	case 'i':
		return 'd';
	case 'j':
		return 'u';
	case 'k' :
		return 'i';
	case 'l' :
		return 'g';
	case 'm':
		return 'l';
	case 'n':
		return 'b';
	case 'o':
		return 'k';
	case 'p':
		return 'r';
	case 'q':
		return 'z';
	case 'r':
		return 't';
	case 's':
		return 'n';
	case 't':
		return 'w';
	case 'u':
		return 'j';
	case 'v':
		return 'p';
	case 'w':
		return 'f';
	case 'x':
		return 'm';
	case 'y':
		return 'a';
	case 'z':
		return 'q';
	default:
		return x;
	}
}



int main()
{
int j,index ;
FILE *fo,*fi;
char strout[100];
char strinp[100];
int noOfTest =0;
int i =0;

fo = fopen("output.in","w");
fi = fopen("input.in","r");

strcpy(strinp, "");
fgets(strinp,70,fi);

noOfTest=atoi(&strinp[0]);

for( index =1; index <= noOfTest; index ++)
{

	strcpy(strinp, "");
	fgets(strinp,100,fi);   /* no of windows */

	strcpy(strout,"");
	for( i=0; strinp[i]!='/0'; i++)
	{
	strout[i]=utog(strinp[i]);
	}


	fputs(strout,fo);
}

return 1;

}
