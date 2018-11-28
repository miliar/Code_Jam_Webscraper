#include <stdio.h>
#include <stdlib.h>
#include <cstring>

#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <list>

FILE* fp;
FILE* fout;

#define JAM_DEBUG

#define MAX_CHAR 100

#ifdef JAM_DEBUG
#define TEST_IN fp
#define TEST_OUT fout
#else
#define TEST_IN stdin
#define TEST_OUT stdout
#endif


std::multiset<int, std::greater<int>> freqs;
int keyletters[1000];
int P,K,L;

int Input()
{
	freqs.clear();
	fscanf(TEST_IN, "%d %d %d\n", &P, &K, &L);
	for (int i=0; i<L; i++)
	{
		int p;
		fscanf(TEST_IN, "%d", &p);
		freqs.insert(p);
	}
	return 0;
}

int Compute()
{
	int nResult = 0;
	memset(keyletters, 0, sizeof(int)*1000);
	std::multiset<int, std::greater<int>>::iterator iter;
	int index = 0;
	for (iter = freqs.begin(); iter!= freqs.end(); iter++)
	{
		keyletters[index]++;
		nResult += keyletters[index]*(*iter);
		index++;
		if (index >= K)
			index = 0;
		
		if (keyletters[index] >= P)
		{
			index++;
			if (index >= K)
				index = 0;
		}
	}
	return nResult;
}

int Program()
{
	int nNumCase;
	fscanf(TEST_IN, "%d\n", &nNumCase);
	for (int i=0; i<nNumCase; i++)
	{
		Input();
		int nResult = Compute();
		fprintf(TEST_OUT, "Case #%d: %d\n",i+1,nResult);
	}
	return 0;
}

int main()
{
	fp = fopen("A-small-attempt0.in", "r");
	fout = fopen("output_r1c_1.txt", "w");
	Program();
	fclose(fp);
	fclose(fout);
#ifdef JAM_DEBUG
	system("pause");
#endif
	return 0;
}

