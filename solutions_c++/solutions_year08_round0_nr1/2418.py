#include <stdio.h>
#include <windows.h>
#include <ctype.h>

int main()
{
	FILE *f;
	char buf[256];
	int temp;
	int numberOfCases;
	char *name =  "E:\\1.in";
	f = fopen(name,"r");
	fgets(buf, sizeof(buf), f);
	sscanf(buf, "%d", &numberOfCases);
	for(int i = 0; i < numberOfCases; i++)
	{
		int numberOfEngines;
		fgets(buf, sizeof(buf), f);
		sscanf(buf, "%d", &numberOfEngines);
		char engines[numberOfEngines][256];
		for(int i = 0; i < numberOfEngines; i++)
		{
			fgets(engines[i], sizeof(engines[i]), f);
		}
		
		int numberOfQueries;
		fgets(buf, sizeof(buf), f);
		sscanf(buf, "%d", &numberOfQueries);
		char queries[numberOfQueries][256];
		for(int i = 0; i < numberOfQueries; i++)
		{
			fgets(queries[i], sizeof(queries[i]), f);
		}
		
		
		int numberOfNoEquals[numberOfEngines];
		memset(&numberOfNoEquals, 0, sizeof(numberOfNoEquals));
		int completedWay, TcompletedWay, temp_completedWay, currEngine, lastEngine, number;
		completedWay = 0;
		TcompletedWay = 0;
		temp_completedWay = 0;
		number = 0;
		lastEngine = 0;
		while(completedWay < numberOfQueries)
		{
			for(int i = 0; i < numberOfEngines; i++)
			{
				temp_completedWay = completedWay;
				for(int j = completedWay; j < numberOfQueries; j++)
				{
					if(strcmp(engines[i], queries[j]) != 0)
					{
						temp_completedWay++;
						//printf("engine%i:%s\n", i, queries[j]);
					} else {
						if(temp_completedWay > TcompletedWay)
						{
							TcompletedWay = temp_completedWay;
							currEngine = i;
						}
						break;
					}
					if(j == numberOfQueries - 1)
					{
						TcompletedWay = temp_completedWay;
						currEngine = i;
					}
					//getchar();
				}
				//printf("Tcompleted way:%d\n", TcompletedWay);
				if(TcompletedWay >= numberOfQueries)
					break;
			}
			completedWay = TcompletedWay;
			
			
			//if(lastEngine != currEngine)
				number++;
		}
		printf("#%d: %d\n", i+1, number-1);
	}
	fclose(f);
	
	return 0;
}
