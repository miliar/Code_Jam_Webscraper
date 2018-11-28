#ifdef WIN32
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <cstdlib>
#include <cstdio>

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
	int length;
	int words;
	char dict[5000][16];

	fscanf(finput, "%d%d%d", &length, &words, &cases);
	for(int i = 0; i < words; i++)
	{
		fscanf(finput, "%s", dict[i]);
	}

	for(int i = 0; i < cases; i++)
	{
		printf("Case #%d: ", i + 1);
		int matches = 0;
		char pattern[(26 + 2) * 15 + 1];
		fscanf(finput, "%s", pattern);
		for(int j = 0; j < words; j++)
		{
			int pos = 0;
			char* ptr = pattern;
			while(pos < length)
			{
				if(*ptr != '(')
				{
					if(*ptr == dict[j][pos])
					{
						ptr++;
						pos++;
						continue;
					}
					else
						break;
				}
				else
				{
					ptr++;
					while(*ptr != ')')
					{
						if(*ptr == dict[j][pos])
						{
							while(*ptr != ')')
								ptr++;
							ptr++;
							pos++;
							goto cont1;
						}
						ptr++;
					}
					break;
				}
cont1:
				continue;
			}
			if(pos == length)
				matches++;
		}
		printf("%d\n", matches);
	}

	fclose(finput);
	return(0);
}