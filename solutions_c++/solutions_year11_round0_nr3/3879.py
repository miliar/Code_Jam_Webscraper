// CandySplitting.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <math.h>
#include <algorithm>
#include <stdlib.h>


//Visual Studio 2010 Express

using namespace std;

bool checkSum(long int tab[], int tabSize)
{
	long int result = 0;

	for (int i=0 ; i< tabSize; ++i)
	{
		result ^= tab[i];
	};

	if (result != 0) 
		return false;
	else 
		return true;
};

class RecurState 
{
	public:
		long int currXorOne;
		long int currSumOne;

		long int currXorTwo;
		long int currSumTwo;

		int      n;
		
		long int maxSum;

		void reset() {
			currXorOne = 0;
			currSumOne = 0;
			
			currXorTwo = 0;
			currSumTwo = 0;
                  n =  0;
		      maxSum = 0;
		};
};

long int generateSolution(long int tab[], int maxN, RecurState state)
{

	if (state.n >= maxN)
	{
		if  ((state.currXorOne == state.currXorTwo) && (state.currSumOne != state.maxSum) && (state.currSumOne!=0) )
			return max(state.currSumOne, state.currSumTwo);
		else
			return -1;
	};

	RecurState inFirst = state;
	inFirst.currXorOne ^= tab[state.n];
	inFirst.currSumOne += tab[state.n];
	inFirst.n += 1;

	long int sumInOne = generateSolution(tab, maxN, inFirst);

	RecurState inSecond = state;
	inSecond.currXorTwo ^= tab[state.n];
	inSecond.currSumTwo += tab[state.n];
	inSecond.n += 1;

	long int sumInTwo = generateSolution(tab, maxN, inSecond);

	return max(sumInOne, sumInTwo);
}

int main(int argc, char* argv[])
{
	long int tab[200];
	int tabSize;
	int T, maxN;
	RecurState state;

	freopen ("c://temp//C-small-attempt0.in","r",stdin);
	freopen ("c://temp//CandySplitting.out","w",stdout);

	scanf("%i", &T);

	for (int i=1; i <=T; ++i)
	{
		state.reset();
		scanf("%i", &maxN);
		for (int j=1; j<= maxN; ++j)
		{
			scanf("%li", &tab[j-1]);
			state.maxSum += tab[j-1];
		};

		if (! checkSum(tab, maxN) )
		{
			printf("Case #%i: NO\n",i);
		} 
		else {
				long int result = generateSolution(tab, maxN, state);
				printf("Case #%i: %li\n", i, result);
		}

	};

	return 0;
}

