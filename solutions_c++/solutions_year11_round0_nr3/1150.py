#include <cstdio>
#include <algorithm>
#include <vector>
#include <cassert>
#include <cmath>
#include <sstream>
#include <string>
#include <map>
using namespace std;

vector<int> pieces;
bool bPossible;
int iAnswer;

void readTestCase()
{
	pieces.clear();
	int iPieces, iPiece;
	scanf("%d", &iPieces);
	for(int i=0; i<iPieces; i++)
	{
		scanf("%d", &iPiece);
		pieces.push_back(iPiece);
	}
}

void compute()
{
	int iSum = 0, iXor = 0, iMin = 1000000;
	for(int i=0; i<pieces.size(); i++)
	{
		iSum += pieces[i];
		iXor ^= pieces[i];
		iMin = min(iMin, pieces[i]);
	}
	bPossible = (iXor == 0);
	iAnswer = iSum - iMin;
}

void writeAnswer()
{
	if (!bPossible)
	{
		printf("NO\n");
		return;
	}
	printf("%d\n", iAnswer);
}

int main()
{
	int iTests;
	scanf("%d", &iTests);
	for(int iTestCase = 1; iTestCase <= iTests; iTestCase++)
	{
		readTestCase();
		printf("Case #%d: ", iTestCase);
		compute();
		writeAnswer();
	}
	
	return 0;
}
 
 
