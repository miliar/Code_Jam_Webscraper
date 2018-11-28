#ifdef WIN32
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <cstdlib>
#include <cstdio>

int count(char* from, const char* what)
{
	if(*what == 0)
		return(1);
	int seqs = 0;
	char* ptr = from;
	while(*ptr != 0)
	{
		if(*ptr == *what)
		{
			seqs += count(ptr + 1, what + 1);
		}
		ptr++;
	}
	return(seqs);
}

int main(int argc, char* argv[])
{
	if(argc < 2)
	{
		printf("Usage: %s inputfile\n", argv[0]);
		return(0);
	}
	FILE* finput = fopen(argv[1], "r");
	if(finput == 0)
	{
		printf("Input file could not be opened\n");
		return(0);
	}

	int cases;
	fscanf(finput, "%d ", &cases);
	char line[501];
	const char* str = "welcome to code jam";
	for(int i = 0; i < cases; i++)
	{
		printf("Case #%d: ", i + 1);
		fgets(line, 501, finput);
		
		int seqs = count(line, str);
		printf("%04d\n", seqs % 10000);
	}

	fclose(finput);
	return(0);
}