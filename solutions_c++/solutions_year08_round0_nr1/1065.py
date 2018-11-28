#include <stdio.h>
#include <string.h>

int IndexEngine(char * str, char ** engine, int nengine)
{
	for(int i = 0; i < nengine; i++)
	{
		if(strcmp(str, engine[i]) == 0)
			return i;
	}
	return -1;
}



int IsNotEnd(char ** pool, char ** engine, int npool, int nengine, int & ptrpool)
{
	int * flag;
	int count;
	int index;

	flag = new int[nengine];
	memset(flag, 0, nengine * sizeof(int));
	count = 0;
	while(ptrpool < npool)
	{
		index = IndexEngine(pool[ptrpool], engine, nengine);
		if(index >= 0)
		{
			if(! flag[index])
			{
				flag[index] = 1;
				count ++;
			}
		}
		if(count == nengine)
			break;
		else
			ptrpool ++;
	}

	delete[] flag;

	if(ptrpool >= npool)
		return 0;
	return 1;
}

int GetSwitches(char ** pool, char ** engine, int npool, int nengine)
{
	int ptrpool = 0;
	int count = 0;

	while(IsNotEnd(pool, engine, npool, nengine, ptrpool))
		count ++;

	return count;
}

int main(int argc, char ** argv)
{
	int ncases;
	int nengine;
	int npool;
	char ** pool;
	char ** engine;
	FILE* fpin, * fpout;
	int count;

	if(argc < 3)
	{
		printf("Requires in and out filename!\n");
		return 0;
	}

	pool = new char*[1000];
	engine = new char*[100];
	for(int i = 0; i < 1000; i++)
		pool[i] = new char[120];
	for(int i = 0; i < 100; i++)
		engine[i] = new char[120];

	fpin = fopen(argv[1], "r");
	fpout = fopen(argv[2], "w");

	fscanf(fpin, "%d", &ncases);

	for(int k = 0; k < ncases; k++)
	{
		fscanf(fpin, "%d", &nengine);
		fgets(engine[0], 120, fpin);
		for(int i = 0; i < nengine; i++)
			fgets(engine[i], 120, fpin);
		fscanf(fpin, "%d", &npool);
		fgets(pool[0], 120, fpin);
		for(int i = 0; i < npool; i++)
			fgets(pool[i], 120, fpin);
		count = GetSwitches(pool, engine, npool, nengine);
		fprintf(fpout, "Case #%d: %d\n", k + 1, count);
	}

	fclose(fpin);
	fclose(fpout);

	return 0;
}



