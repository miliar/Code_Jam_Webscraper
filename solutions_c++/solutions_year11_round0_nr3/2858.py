#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef unsigned int uint;
typedef unsigned long ulong;

int numCases;
int N;
int values[1000];
vector<int> leftPileIndices;
int maxValue = 0;


int add(int a, int b)
{
	int newa = 0;
	int newb = 0;
	int digit = 0;
	while (a || b)
	{
		if ((a ^ b) & 1)
		{
			newa |= (a & 1) << digit;
			newb |= (b & 1) << digit;
		}
		a >>= 1;
		b >>= 1;
		digit++;
	}
	return newa + newb;
}

void recurse(int splitSize, int startIndex)
{
	if (leftPileIndices.size() == splitSize)
	{
//		for (vector<int>::iterator it = leftPileIndices.begin(); it != leftPileIndices.end(); it++)
//		{
//			cout << *it << " ";
//		}
//		cout << endl;

		int pile1 = 0;
		int pile2 = 0;
		int pile1Real = 0;
		int pile2Real = 0;
		int leftPileIndex = 0;
		for (int i = 0; i < N; i++)
		{
			if (leftPileIndex < leftPileIndices.size() && i == leftPileIndices[leftPileIndex])
			{
				pile1Real += values[i];
				pile1 = add(pile1, values[i]);
				leftPileIndex++;
			} else
			{
				pile2Real += values[i];
				pile2 = add(pile2, values[i]);
			}
		}
		
		if (pile1 == pile2)
		{
			if (pile1Real > maxValue)
			{
				maxValue = pile1Real;
			}
			if (pile2Real > maxValue)
			{
				maxValue = pile2Real;
			}
		}
	} else
	{
		for (int i = startIndex; i < N; i++)
		{
			leftPileIndices.push_back(i);
			recurse(splitSize, i + 1);
		}
	}
	leftPileIndices.pop_back();
}

int main (int argc, char * const argv[]) 
{
	if ( argc != 2 ) return -1;

	FILE * f = fopen(argv[1], "r");
	fscanf(f, "%d", &numCases);

//	printf("5+4 = %d\n", add(5, 4));
//	printf("7+9 = %d\n", add(7, 9));
//	printf("50+10 = %d\n", add(50, 10));
	for ( int caseIndex = 0; caseIndex < numCases; caseIndex++ )
	{
		cout << "Case #" << caseIndex + 1 << ": ";

		fscanf(f, "%d", &N);
		for (int i = 0; i < N; i++)
		{
			fscanf(f, " %d", &values[i]);
		}
		
		maxValue = 0;
		
		for (int splitSize = 1; splitSize <= N / 2; splitSize++)
		{
			leftPileIndices.clear();
			recurse(splitSize, 0);
		}
		
		if (maxValue == 0)
		{
			cout << "NO" << endl;
		} else
		{
			cout << maxValue << endl;
		}
	}

	fclose(f);
	return 0;
}
