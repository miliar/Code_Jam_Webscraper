#include <stdio.h>
#include <string.h>
#include <vector>
#include <string>
#include <conio.h>

using namespace std;

void remove_newline(char *str)
{
	int len = strlen(str);
	if (len >= 1) 
		if (str[len - 1] == '\n') str[len - 1] = '\0';
	if (len >= 2) 
		if (str[len - 2] == '\r') str[len - 2] = '\0';
}

void read_line(FILE *fin, char *buffer, int n)
{
	fgets(buffer, n, fin);
	remove_newline(buffer);
}

void skip_newline(FILE *fin)
{
	while (fgetc(fin) != '\n')
		;
}

int main()
{
	const int BUFF_SIZE = 200;
	char buffer[BUFF_SIZE];
	FILE *fin = fopen("A-large.in", "rt");
	FILE *fout = fopen("A-large.out", "wt");
	if (fin == NULL) return 1;

	int ncases;
	fscanf(fin, "%d", &ncases);

	// --------------- Test Case -----------------------
	for (int i = 0; i < ncases; i++)
	{
		// -------- Read the Engine Names ----------
		int numEngines;

		// Number of engines
		fscanf(fin, "%d", &numEngines);
		vector<string> engineArray(numEngines);
		skip_newline(fin);
		
		// The engine names
		for (int j = 0; j < numEngines; j++)
		{
			read_line(fin, buffer, BUFF_SIZE);
			engineArray[j] = string(buffer);
		}

		// Print the engine names
		/*printf("The engines are:\n");
		for (int j = 0; j < (int)engineArray.size(); j++)
			printf("%d: %s\n", j + 1, engineArray[j].c_str());*/

		// ------------ Read the Queries -------------
		int numQueries;
		fscanf(fin, "%d", &numQueries);
		skip_newline(fin);

		vector<bool> engineTaken(numEngines, false);
		int numAvailable = numEngines;
		int numSwitches = 0;
		for (int j = 0; j < numQueries; j++)
		{
			read_line(fin, buffer, BUFF_SIZE);
			string query(buffer);

			// Find the index of the engine
			int index;
			for (index = 0; index < numEngines; index++)
			{
				if (engineArray[index] == query) break;
			}

			/*if (index < numEngines) printf("Query: %s\n", engineArray[index].c_str());
			else printf("Query Failed!\n");*/

			// Use up the indexed engine
			if (!engineTaken[index])
			{
				if (numAvailable == 1) 
				{
					numSwitches++;
					for (int i = 0; i < numEngines; i++)
					{
						engineTaken[i] = false;
						numAvailable = numEngines;
					}
				}
				numAvailable--;
				engineTaken[index] = true;
			}
		}

		//printf("Num switches: %d\n", numSwitches);
		fprintf(fout, "Case #%d: %d\n", i + 1, numSwitches);
	}
	fclose(fin);
	fclose(fout);
	//getch();
}