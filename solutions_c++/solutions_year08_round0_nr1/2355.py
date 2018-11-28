#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE_BUFF 128
#define SIZE_ENGINE 100

void trim(char* src)
{
	int length = strlen(src);
	for (int i = length - 1; i > -1; i--)
	{
		if (src[i] == '\n')
			src[i] = 0;
		else
			break;
	}
	return;
}

void code(char* in, char* out)
{
	// Open Input File
	FILE* fin;
	fin = fopen(in, "rb");
	
	// Open Output File
	FILE* fout;
	fout = fopen(out, "wb");
	
	// Read Line Count
	char buff[SIZE_BUFF];
	fgets(buff, SIZE_BUFF, fin);
	int count = atoi(buff);

	// Loop
	int engine_stat[SIZE_ENGINE];
	char engine[SIZE_ENGINE][SIZE_BUFF];
	for (int i = 0; i < count; i++)
	{
		// Read Engine Count
		fgets(buff, SIZE_BUFF, fin);
		int count_engine = atoi(buff);

		// Read Engine Name & Set Engine Stat
		for (int j = 0; j < count_engine; j++)
		{
			fgets(engine[j], SIZE_BUFF, fin);
			trim(engine[j]);
			engine_stat[j] = 0;
		}

		// Read Query Count
		fgets(buff, SIZE_BUFF, fin);
		int count_query = atoi(buff);

		// Switch Query
		int count_used = 0;
		int count_switch = 0;
		for (int j = 0; j < count_query; j++)
		{
			fgets(buff, SIZE_BUFF, fin);
			trim(buff);
			for (int k = 0; k < count_engine; k++)
			{
				if (!strcmp(engine[k], buff))
				{
					if (!engine_stat[k])
					{
						count_used++;
						engine_stat[k] = 1;
						if (count_engine == count_used)
						{
							count_switch++;
							for (int l = 0; l < count_engine; l++)
								engine_stat[l] = 0;
							count_used = 1;
							engine_stat[k] = 1;
						}
					}
					break;
				}
			}
		}

		// Write Result
		if (i > 0)
			fprintf(fout, "\n");
		fprintf(fout, "Case #%d: %d", i + 1, count_switch);
		
	}

	// Close Output File
	fclose(fout);

	// Close Input File
	fclose(fin);

	// Return
	return;
}

int main(int argc, char** argv)
{
	// Call Function
	code("c:\\CodeJam\\A-large.in.txt", "c:\\CodeJam\\A-large.out.txt");

	// Return Result
	return 0;
}