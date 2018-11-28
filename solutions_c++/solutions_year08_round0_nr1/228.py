// This should work for small as well as large data sets
//---------------------------------------------------------------------------

#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>

//---------------------------------------------------------------------------

int main()
{
  int N;
  char n[4];
  FILE * inFile, * outFile;
  inFile = fopen ("C:\\Documents and Settings\\Risky\\My Documents\\Borland Studio Projects\\saving_universe\\A-small.in","r");
  outFile = fopen ("C:\\Documents and Settings\\Risky\\My Documents\\Borland Studio Projects\\saving_universe\\A-small.out","w");
  if (inFile!=NULL)
  {
	fgets(n, 4, inFile);
	N = atoi(n);

	int S, Q;
	char s[5], q[6];
	char search_engines[100][101];
	bool visited_search_engines[100];
	char queries[1000][101];
//	char* temp = new char[103];
	char temp[103];
	for (int i = 1; i <= N; i++)
	  {

		// Read search engines input
		fgets(s, 5, inFile);
		S = atoi(s);
		for (int j = 0; j < S; j++)
		{
			fgets(temp, 103, inFile);
			temp[strlen(temp) - 1] = '\0';
			strcpy(search_engines[j], temp);
		}

		// Read search strings input
		fgets(q, 6, inFile);
		Q = atoi(q);
		for (int j = 0; j < Q; j++)
		{
			fgets(temp, 103, inFile);
			temp[strlen(temp) - 1] = '\0';
			strcpy(queries[j], temp);
		}

		// Linear sort is suitable for search_engines which is at most 100 items
		int min;
		for (int j = 0; j < S - 1; j++)
		{
			min = j;
			for (int k = j + 1; k < S; k++)
			{
				if (strcmp(search_engines[min], search_engines[k]) > 0) min = k;
			}
			if (min != j)
			{
				strcpy(temp, search_engines[j]);
				strcpy(search_engines[j], search_engines[min]);
				strcpy(search_engines[min], temp);
			}

		}

		// Counting optimal number of switches
		int total_switches = 0;
		int total_visited = 0;

		for (int k = 0; k < S; k++)
		{
			visited_search_engines[k] = false;
		}

		int j = 0;
		while (j != Q)
		{

			// Binary search to check visited search engines
			int bin_index = S / 2, min_index = 0, max_index = S - 1;
			int diff;
			while (diff = strcmp(search_engines[bin_index], queries[j]))
			{
				if (diff < 0)
				{
					min_index = bin_index + 1;
					bin_index = (min_index + max_index) / 2;
				}
				else
				{
					max_index = bin_index - 1;
					bin_index = (min_index + min_index) / 2;
				}
			}

			if (!visited_search_engines[bin_index])
			{
				visited_search_engines[bin_index] = true;
				total_visited++;
				if (total_visited == S)
				{
					total_switches++;
					j--;
					total_visited = 0;
					for (int k = 0; k < S; k++)
					{
						visited_search_engines[k] = false;
					}
				}

			}

			j++;
		}

		fprintf(outFile, "Case #%d: %d\n", i, total_switches);


	  }

	fclose (inFile);
	fclose (outFile);

  }
//  getch();

  return 0;
}
//---------------------------------------------------------------------------
