#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	FILE *fp1;
	char oneword[100];
	char *c;
	int num_test, num_engine, num_query;
	char szEngine[100][100], szQuery[1000][100];
	int idxEngine[100];
	int max = -1;
	int max_engine_idx = -1;
	int switches = 0;
	int test;
	int i, j, k, ptr;

	fp1 = fopen("in.txt", "r");
	if (fp1 == NULL)
	{
		printf("File failed to open\n");
		exit (EXIT_FAILURE);
	}

	fscanf(fp1, "%d", &num_test);
	for (test=0; test<num_test; test++)
	{
		fscanf(fp1, "%d", &num_engine);
		c = fgets(oneword, 100, fp1);  /* get one line from the file */
		for (i=0; i<num_engine; i++)
		{
			c = fgets(szEngine[i], 100, fp1);  /* get one line from the file */
		}
		fscanf(fp1, "%d", &num_query);
		c = fgets(oneword, 100, fp1);  /* get one line from the file */
		for (i=0; i<num_query; i++)
		{
			c = fgets(szQuery[i], 100, fp1);  /* get one line from the file */
		}

		ptr = 0;
		switches = 0;
		max = -1;
		max_engine_idx = -1;
		while (ptr < num_query)
		{
			bool b_found = false;
			for (i=0; i<num_engine; i++)
			{
				b_found = false;
				for (j=ptr; j<num_query; j++)
				{
					if ( strcmp(szEngine[i], szQuery[j]) == 0 )
					{
						b_found = true;
						idxEngine[i] = j;
						if ( j > max )
						{
							max = j;
							max_engine_idx = i;
						}
						break;
					}
				}
				if ( !b_found )
				{
					break;
				}
			}
			if ( !b_found )
			{
				break;
			}
			ptr = max;
			switches++;
		}

		printf("Case #%d: %d\n", test+1, switches);

	}

	fclose(fp1);

	return 0;
}
