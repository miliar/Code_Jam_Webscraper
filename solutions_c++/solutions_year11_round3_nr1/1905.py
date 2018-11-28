#import <Foundation/Foundation.h>


int validPicture (char *picture, int R, int C)
{
	int valid = 1;
	for (int row = 0; row < R; row++)
	{
		for (int col = 0; col < C; col++)
		{
			if (*(picture + row * C + col) == '#') 
			{
				valid = 0;
			}
		}
	}
	
	return valid;
}

void readPicture(FILE *inFile, char *picture, int R, int C)
{
	for (int row = 0; row < R; row++)
	{
		for (int col = 0; col < C; col++)
		{
			fscanf(inFile, "%c", picture + row * C + col);
		}
		fscanf(inFile, "\n");
	}
	fscanf(inFile, "\n");
}

void processPicture(char *picture, int R, int C)
{
	for (int row = 1; row < R; row++)
	{
		for (int col = 1; col < C; col++)
		{
			char *point1 = picture + (row - 1)* C + col - 1;
			char *point2 = picture + (row - 1)* C + col;
			char *point3 = picture + (row) * C + col - 1;
			char *point4 = picture + (row) * C + col;
			if (( *point1 == '#') && ( *point2 == '#') &&
				( *point3 == '#') && ( *point4 == '#'))
			{
				*point1 = '/';
				*point2 = '\\';
				*point3 = '\\';
				*point4 = '/';
			}
		}
	}
}

void printPicture1(FILE *outFile, char *picture, int R, int C, int testNumber)
{	
	fprintf(outFile, "Case #%d:\n", testNumber);
	
	{
		for (int row = 0; row < R; row++)
		{
			for (int col = 0; col < C; col++)
			{
				fprintf(outFile, "%c", *(picture + row * C + col));
			}
			fprintf(outFile, "\n");
		}
	}
}

void printPicture(FILE *outFile, char *picture, int R, int C, int testNumber)
{
	int valid = validPicture(picture, R, C);
	
	fprintf(outFile, "Case #%d:\n", testNumber);
	
	if (valid) 
	{
		for (int row = 0; row < R; row++)
		{
			for (int col = 0; col < C; col++)
			{
				fprintf(outFile, "%c", *(picture + row * C + col));
			}
			fprintf(outFile, "\n");
		}
	}
	else
	{
		fprintf(outFile, "Impossible\n");
	}
}

int main (int argc, const char * argv[]) 
{	
	FILE *inFile = fopen("/Users/alex/Downloads/A-large.in", "r");
	FILE *outFile = fopen("/Users/alex/Downloads/A-large.out", "w");
	
	int T = 0;
	fscanf(inFile, "%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		int R, C;
		fscanf(inFile, "%d %d\n", &R, &C);
		char *picture = malloc(R * C * sizeof(char));
		readPicture(inFile, picture, R, C);
		processPicture(picture, R, C);
		printPicture(outFile, picture, R, C, i + 1);
		free(picture);
	}
	
    return 0;
}
