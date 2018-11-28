/*++

	Input

	The first line of the input file contains the number of cases, N. 
	N test cases follow. 
	Each case starts with the number S -- the number of search engines. 
	The next S lines each contain the name of a search engine. 
	Each search engine name is no more than one hundred characters long and contains only uppercase letters, 
	lowercase letters, spaces, and numbers. 
	There will not be two search engines with the same name. 
	The following line contains a number Q -- the number of incoming queries. 
	The next Q lines will each contain a query. 
	Each query will be the name of a search engine in the case. 

	Output

	For each input case, you should output: 

	Case #X: Y
	
	where X is the number of the test case and Y is the number of search engine switches. 
	Do not count the initial choice of a search engine as a switch. 

	Limits

	0 < N ¡Â 20 

	Small dataset

	2 ¡Â S ¡Â 10 
	0 ¡Â Q ¡Â 100 

	Large dataset

	2 ¡Â S ¡Â 100 
	0 ¡Â Q ¡Â 1000 

--*/
#include <stdio.h>
#include <stdlib.h>
#include <io.h>
#include <string.h>
#include <list>


#define max_character	100
#define _small_data_set 1
#define min(x, y)		(((x) < (y)) ? (x) : (y))

#ifdef _small_data_set
#define max_engine		10
#define max_query		100
#else
#define max_engine		100
#define max_query		1000
#endif


typedef unsigned int uint;

typedef struct _eitem	{
	char name[max_character + 1];
	bool b;
	uint cnt;
} eitem;

// char engine[max_engine][max_character + 1] = {0, };
eitem engine[max_engine];
char query[max_query][max_character + 1] = {0, };
uint icase = 0;
uint ocase = 0;
uint iengine = 0;
uint oengine = 0;
uint iquery = 0;
uint oquery = 0;

uint
find_next_route(uint pos)
{
	uint i = 0, k;
	uint find = 0;
	uint last = 0;

	for (i = 0; i < iengine; i++)
	{
		engine[i].b = false;
		// engine[i].cnt = 0;
	}

	for (i = pos; i < iquery; i++)
	{
		for (k = 0; k < iengine; k++)
		{
			if (!stricmp(query[i], engine[k].name))
			{
				if (engine[k].b == false)
				{
					engine[k].b = true;
					find++;
				}
			}

			if (find == iengine)
				break;
		}

		if (find == iengine)
			break;
	}

	if (find == iengine)
		i = k;
	else
	{
		for (i = 0; i < iengine; i++)
		{
			if (engine[i].b == false)
				break;
		}
	}
	
	return i;

}

char *
out(uint *len, uint ncase)
{
	char *out = 0;
	int i = 0;
	uint k = 0/* query number */, n = 0 /* which engine starts with*/, l, j;
	uint tr[max_engine] = {0, } /* try count */, exam[max_engine] = {0, };
	uint mi = 0;
	
	while (k != iquery)
	{
		i = find_next_route(k);
		for ( ; k < iquery; k++)
		{
			if (!stricmp(engine[i].name, query[k]))
			{
				//
				// bomb..
				//
				break;
			}
		}

		if (k == iquery)
		{
			//
			// succeeded
			//
			k = 0;
			iquery = 0;
		}		
		else
			mi++;
	}

	if (!(out = (char *)malloc(260)))
	{
		*len = 0;
		return 0;
	}

	*len = sprintf(out, "Case #%d: %d\n", ncase + 1, mi);
	return out;
}

int
main(int argc, char *argv[])
{
	FILE *fp = 0, *of;
	char input[max_character + 1] = {0, };
	char *buf = 0;
	uint outlen = 0;

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
		fgets(input, max_character, fp);
		
		if (icase == 0)
			icase = atoi(input);
		else if (icase == ocase)
			break;
		else if (icase > ocase)
		{
			if (iengine == 0)
				iengine = atoi(input);
			else if (iengine > oengine)
 				strcpy(engine[oengine++].name, input);
			else if (iengine == oengine)
			{
				if (iquery == 0)
				{
					if ((iquery = atoi(input)) == 0)
					{
						if (buf = out(&outlen, ocase++))
						{
							fwrite(buf, outlen, 1, of);
							free(buf);
						}

						iquery = 0;
						iengine = 0;
						oengine = 0;
					}
				}
				else if (iquery > oquery)
					strcpy(query[oquery++], input);
				else if (iquery == oquery)
				{
					if (buf = out(&outlen, ocase++))
					{
						fwrite(buf, outlen, 1, of);
						free(buf);
					}

					iquery = 0;
					iengine = atoi(input);
					oengine = 0;
					oquery = 0;					
				}	
			}			
		}
		

		memset(input, 0, max_character);
	}

	if (fp)
		fclose(fp);

	if (of)
		fclose(of);

	return 0;
}