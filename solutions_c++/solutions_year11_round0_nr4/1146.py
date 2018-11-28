#include <cstdio>
#include <algorithm>
#include <vector>
#include <cassert>
#include <cmath>
#include <sstream>
#include <string>
#include <map>
using namespace std;

vector<int> viPermutation;
double dAnswer;

void readTestCase()
{
	viPermutation.clear();
	int n;
	scanf("%d", &n);
	for(int i=0; i<n; i++)
	{
		int iTemp;
		scanf("%d", &iTemp);
		viPermutation.push_back(iTemp);
	}
}

void compute()
{
	dAnswer = viPermutation.size();
	for(int i=1; i<=viPermutation.size(); i++)
		dAnswer -= (viPermutation[i-1]==i);
}

void writeAnswer()
{
	printf("%.6lf\n", dAnswer);
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
 
 
 
