#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned int uint;
typedef unsigned long ulong;

int numCases;
int numPeople;
int numSurprising;
int p;
int scores[100];

int main (int argc, char * const argv[]) 
{
	if ( argc != 2 ) return -1;
	
	ifstream inFile(argv[1]);
	inFile >> numCases;
	
	for ( int caseIndex = 0; caseIndex < numCases; caseIndex++ )
	{
		cout << "Case #" << caseIndex + 1 << ": ";
		
		inFile >> numPeople >> numSurprising >> p;
		for (int i = 0; i < numPeople; i++)
		{
			inFile >> scores[i];
		}
		
		int count = 0;
		for (int i = 0; i < numPeople; i++)
		{
			int score = scores[i];
			int div3 = score / 3;
			int mod3 = score % 3;
			if (div3 >= p)
			{
				count++;
			} else if (div3 + 1 >= p && mod3 > 0)
			{
				count++;
			} else if (numSurprising > 0)
			{
				if ((div3 > 0 && div3 + 1 >= p && mod3 == 0) ||
					 (div3 + 2 >= p && mod3 == 2))
				{
					count++;
					numSurprising--;
				}
			}
		}
		
		cout << count << endl;
	}
	
	inFile.close();
	return 0;
}
