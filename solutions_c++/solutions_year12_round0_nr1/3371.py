#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *Input, *Output;
	unsigned char InputSymbol = 0, result[50] [ 1000 ];
	int NumberOfTests, i, j;
	if ( ( Input = fopen ( "C:\\test.txt", "r" ) ) == 0 )
		return -1;
	fscanf ( Input, "%d", &NumberOfTests );
	for ( InputSymbol = fgetc ( Input ),j = 0, i = 0;  InputSymbol != 255; i++ )
	{
		InputSymbol = fgetc ( Input );
		if ( InputSymbol == 10 )
		{
			result[j][i] = 0;
			j++;
			i = -1;

		}
		switch ( InputSymbol )
		{
		case 'y':
			result[j][i] = 'a';
			break;
		case 'n':
			result[j][i] = 'b';
			break;
		case 'f':
			result[j][i] = 'c';
			break;
		case 'i':
			result[j][i] = 'd';
			break;
		case 'c':
			result[j][i] = 'e';
			break;
		case 'w':
			result[j][i] = 'f';
			break;
		case 'l':
			result[j][i] = 'g';
			break;
		case 'b':
			result[j][i] = 'h';
			break;
		case 'k':
			result[j][i] = 'i';
			break;
		case 'u':
			result[j][i] = 'j';
			break;
		case 'o':
			result[j][i] = 'k';
			break;
		case 'm':
			result[j][i] = 'l';
			break;
		case 'x':
			result[j][i] = 'm';
			break;
		case 's':
			result[j][i] = 'n';
			break;
		case 'e':
			result[j][i] = 'o';
			break;
		case 'v':
			result[j][i] = 'p';
			break;
		case 'z':
			result[j][i] = 'q';
			break;
		case 'p':
			result[j][i] = 'r';
			break;
		case 'd':
			result[j][i] = 's';
			break;
		case 'r':
			result[j][i] = 't';
			break;
		case 'j':
			result[j][i] = 'u';
			break;
		case 'g':
			result[j][i] = 'v';
			break;
		case 't':
			result[j][i] = 'w';
			break;
		case 'h':
			result[j][i] = 'x';
			break;
		case 'a':
			result[j][i] = 'y';
			break;
		case 'q':
			result[j][i] = 'z';
			break;
		case ' ':
			result[j][i] = ' ';
			break;
		}
	}
	result[j][i-1] = 0;
	fclose ( Input );
	if ( ( Output = fopen ( "C:\\Output.txt", "w" ) ) == 0 )
		return -1;
	for ( i = 0; i < NumberOfTests; i++ )
	{
		fprintf ( Output, "Case #%d: %s\n", i+1, result[i]);
	}
	fclose ( Output );
	return 0;
}