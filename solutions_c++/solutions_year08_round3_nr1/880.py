/*++


--*/
#include <stdio.h>
#include <stdlib.h>
#include <io.h>
#include <string.h>
#include <list>


#define _text_messaging_outrage 1

#ifdef _text_messaging_outrage

#define max_character	100
#define _small_data_set 0
#define min(x, y)		(((x) < (y)) ? (x) : (y))

#ifdef _small_data_set
#else
#endif

typedef unsigned int uint;

uint ocase = 0;
uint N = 0;
uint P;	// letters to place on a key
uint K;	// the number of keys available
uint L;	// alphabet numbers
std::list<uint> letter_list;


char *
out(uint *len)
{
	char *out = 0;
	uint i = 0;
	uint k = 1;
	uint key = 0;
	uint num_key = 0;
	std::list<uint>::const_iterator it = letter_list.begin();

	if (!(out = (char *)malloc(260)))
	{
		*len = 0;
		return 0;
	}

	if (K * P >= L)
	{
		for (i = 0; i < L; i++, it++)
		{
			key += ((*it) * k);
			num_key++;

			if (num_key >= K)
			{
				num_key = 0;
				k++;
			}
		}

		*len = sprintf(out, "Case #%d: %d\n", ocase + 1, key);
	}
	else
		*len = sprintf(out, "Case #%d: impossible\n", ocase + 1);

	return out;
}

bool
max_order(uint p, uint l)
{
	return (p > l);
}

int 
text_messaging_outrage(int argc, char *argv[])
{
	FILE *fp = 0, *of;
	char input[max_character * 100] = {0, };
	char *buf = 0;
	uint out_length = 0;
	uint line_length = 0;
	int i = 0;
	
	if (argc < 3)
		return 0;

	if (!(fp = fopen(argv[1], "r")))
		return 0;

	if (!(of = fopen(argv[2], "w")))
	{
		fclose(fp);
		return 0;
	}

	while (!feof(fp))
	{
		fgets(input, max_character * 100, fp);
		
		if (N == 0)
			N = atoi(input);
		else if (N == ocase)
			break;
		else if (N > ocase)
		{
			if (P == 0)
			{
				P = atoi(input);
				line_length = strlen(input);

				for (i = 0; i < line_length; i++)
				{
					if (input[i] == ' ')
						break;
				}

				K = atoi(&input[i + 1]);

				for (i++; i < line_length; i++)
				{
					if (input[i] == ' ')
						break;
				}

				L = atoi(&input[i + 1]);
			}
			else
			{	
				int n = -1;
				int temp = 0;

				line_length = strlen(input);
				for (i = 0; i < L; i++)
				{
					temp = atoi(&input[++n]);
					letter_list.push_back(temp);
					letter_list.sort(max_order);

					for (; n < line_length; n++)
					{
						if (input[n] == ' ')
							break;
					}
				}	

				if (buf = out(&out_length))
				{
					fwrite(buf, out_length, 1, of);
					free(buf);
				}

				P = K = L = 0;
				letter_list.clear();
				ocase++;
			}
		}
		
		memset(input, 0, max_character * 100);
	}

	if (fp)
		fclose(fp);

	if (of)
		fclose(of);

	return 0;
}

int
main(int argc, char *argv[])
{
	text_messaging_outrage(argc, argv);
	return 0;
}

#endif
