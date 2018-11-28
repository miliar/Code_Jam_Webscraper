#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <assert.h>
#include <string.h>

/*
2 ¡Ü S ¡Ü 100 

0 ¡Ü Q ¡Ü 1000 
*/

void fgetline(FILE* fin, char line[])
{
	// skip spaces
	int pos = 0;
	int c;
	c = fgetc(fin);
	while (isspace(c))
		c = fgetc(fin);
	while (c != '\n') {
		line[pos++] = c;

		c = fgetc(fin);
	}
	line[pos] = 0x00;
}

struct SearchSet {// 32 * 4 = 128 - 100 = 28
	unsigned long u[4];
};

SearchSet Query[1000+1];

int num_query = 0;
int num_engine = 0;


SearchSet SSAnd(const SearchSet& s1, const SearchSet& s2)
{
	SearchSet ret = {0,0,0,0};
	for (int i = 0; i < 4; i++) {
		ret.u[i] = s1.u[i] & s2.u[i];
	}
	return ret;
}
// from left to right is bit1 bit2 bit3.....bit32...bit100
void SSSetBit(SearchSet& s1, int posOfBit, int val)
{
	int unitSize = sizeof(unsigned long) * 8;
	assert(unitSize==32);
	int unitPos = posOfBit / unitSize;
	int InUnitPos = posOfBit % unitSize; // start from 0
	if (InUnitPos == 0)
		InUnitPos = 32;
	if (val)
		s1.u[unitPos] |= ((unsigned long)0x00000001 << (unitSize-InUnitPos));
	else 
		s1.u[unitPos] &= (~((unsigned long)0x00000001 << (unitSize-InUnitPos)));
}

// set bits of num_engine to be one
void SSAllUp(SearchSet& s1)
{
	int unitSize = sizeof(unsigned long) * 8;
	int unitPos = num_engine / unitSize;
	int InUnitPos = num_engine % unitSize; // 
	if (InUnitPos == 0)
		InUnitPos = 32;

	for (int i = 0; i < unitPos; i++)
		s1.u[i] = (unsigned long)-1;
	s1.u[i] = ((unsigned long)-1) << (unitSize-InUnitPos);
}

// set all to zero
void SSAllDown(SearchSet& s1)
{
	for (int i=0; i<4; i++)
		s1.u[i] = 0;
}

bool isZero(const SearchSet& s1)
{
	if (s1.u[0]|s1.u[1]|s1.u[2]|s1.u[3])
		return false;
	else 
		return true;
}

struct PairOfSet {
	char setName[100+1];
} EngineSet[100+1];

int SearchPairOfSet(char queryName[100+1])
{
	int ret = -1;
	for (int i = 1; i <= num_engine; i++) {
		if (0 == strcmp(queryName, EngineSet[i].setName)) {
			ret = i;
			break;
		}
	}
	if (ret == -1)
		return -1;
	else
		return ret;
}

void InitSearchSet(char queryName[100+1], int curPos)
{
	int engine_num = 0;
	SSAllUp(Query[curPos]);
	engine_num = SearchPairOfSet(queryName);

	SSSetBit(Query[curPos], engine_num, 0);
}

void DoDispachQuery(int& num_switches)
{
	if (num_query <= 0)
		return;
	SearchSet curFriends = Query[1];
	
	for (int i=2; i<=num_query; i++) {
		curFriends = SSAnd(curFriends, Query[i]);
		if (isZero(curFriends)) {
			curFriends = Query[i];
			num_switches++;
		}
	}
}

void InitQuery()
{
	for (int i=1; i<=num_query; i++) {
		SSAllDown(Query[i]);
	}
}
int main()
{
	FILE *fin, *fout;
	int num_case = 0;
	int num_switches = 0;
	char queryName[100+1];


	fin = fopen("D:\\A-small-attempt2.in.txt", "r");
	fout = fopen("D:\\A-small-attempt2.out.txt", "w");

	if (fin == NULL || fout == NULL) {
		fprintf(stderr, "file open error\n");
		exit(-1);
	}

	fscanf(fin, "%d", &num_case);
	for (int i = 1; i <= num_case; i++) {
		num_switches = 0;
		fscanf(fin, "%d", &num_engine);
		
		for (int j = 1; j <= num_engine; j++) {
			fgetline(fin, EngineSet[j].setName);
		}

		fscanf(fin, "%d", &num_query);
		
		InitQuery();

		for (int k = 1; k <= num_query; k++) {
			fgetline(fin, queryName);

			InitSearchSet(queryName, k);
		}
		
		DoDispachQuery(num_switches);
		fprintf(fout, "Case #%d: %d\n", i, num_switches);
	}
	
	fclose(fin);
	fclose(fout);

	return 1;
}
