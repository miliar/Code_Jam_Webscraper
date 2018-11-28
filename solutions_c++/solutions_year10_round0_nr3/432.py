
#include <stdio.h>
#include <string.h>

int groupList[1000] = {0};
int beMap[1000] = {0}; 

int main(int argc, char* argv[])
{
	FILE *pIn = fopen("C:\\jam\\C-large.in", "r");
	FILE *pOt = fopen("C:\\jam\\C-large.ot", "w");

	int caseNum = 0;

	fscanf(pIn, "%d", &caseNum);

	for(int i = 0 ; i < caseNum ; i++)
	{
		int RUN = 0;
		fscanf(pIn, "%d", &RUN);
		int KAPACITY = 0;
		fscanf(pIn, "%d", &KAPACITY);
		int GROUPN = 0;
		fscanf(pIn, "%d", &GROUPN);

		for(int g = 0 ; g < GROUPN ; g++)
		{
			fscanf(pIn, "%d", &groupList[g]);
		}

		// build map
		{
			for(int g = 0 ; g < GROUPN ; g++)
			{
				int sum = 0;
				int index = g;
				int groupOn = 0;

				while(sum + groupList[index] <= KAPACITY && groupOn < GROUPN)
				{
					sum += groupList[index];

					groupOn++;
					index++;
					if(index >= GROUPN)
						index = 0;
				}

				if(groupOn>0)
					beMap[g] = (g + groupOn)%GROUPN;
				else
					beMap[g] = -1;
			}
		}
		

		int beginGID = 0;
		int endGID = 0;
		int round = 0;

		for(int r = 0 ; r < RUN ; r++)
		{
			endGID = beMap[beginGID];

			if(endGID<0) break;

			if(endGID <= beginGID)
				round++;

			beginGID = endGID;
		}

		//calculate money
		long long money = 0;
		for(int g = 0 ; g < GROUPN ; g++)
		{
			money += groupList[g];
		}

		money = money * round;

		for(int g = 0 ; g < beginGID ; g++)
		{
			money += groupList[g];
		}

		// out
		fprintf(pOt, "Case #%d: %I64d\n", i+1 , money);

	}
	fclose(pOt);
	fclose(pIn);

	return 0;
}



