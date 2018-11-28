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

std::multiset<int> v1;
std::multiset<int, std::greater<int>> v2;

int Input()
{
	int nSize;
	fscanf(TEST_IN, "%d\n", &nSize);
	v1.clear();
	v2.clear();
	for (int i=0;i<nSize; i++)
	{
		int val;
		fscanf(TEST_IN,"%d", &val);
		v1.insert(val);
	}
	for (int i=0;i<nSize; i++)
	{
		int val;
		fscanf(TEST_IN,"%d", &val);
		v2.insert(val);
	}
	return 0;
}

int Compute()
{
	int nSize = (int)v1.size();
	int nResult = 0;
	std::multiset<int>::iterator Iter1 = v1.begin();
	std::multiset<int, std::greater<int>>::iterator Iter2 = v2.begin();
	for (int i=0; i<nSize; i++)
	{
		nResult += (*Iter1)*(*Iter2);
		Iter1++;
		Iter2++;
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
	fout = fopen("output_r1_1.txt", "w");
	Program();
	fclose(fp);
	fclose(fout);
#ifdef JAM_DEBUG
	system("pause");
#endif
	return 0;
}

