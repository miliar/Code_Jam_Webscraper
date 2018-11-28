#include <iostream>
#include <string>
using namespace std;

// Patrick McCulloch
// patmcculloch@gmail.com
// Saturday, May 7 2011
// Let's hope this works
// but really, it probably won't

void combineElements(string combinePairs[], int numComb, char elementList[], int &size);
void opposeElements(string opposePairs[], int numOpp, char elementList[], int &size);

int main()
{
	// start with number of test cases T
	int T;
	cin >> T;
	

	for (int i=0; i<T; i++)
	{
		cout << "Case #" << i+1 << ": ";
		// then spit out the list
		int numComb;
		cin >> numComb;	
		
		string combinePairs[40];
		for (int j=0; j<numComb; j++)
		{
			cin >> combinePairs[j];
		}
		int numOpp;
		cin >> numOpp;

		string opposePairs[40];
		for (int j=0; j<numOpp; j++)
		{
			cin >> opposePairs[j];
		}	
				
		int N;
		cin >> N;
			
		char elementList[100];
		int size = 0;
		for (int j=0; j<N; j++)
		{
			cin >> elementList[size];
			size++;
			if (size > 1)
			{
				combineElements(combinePairs, numComb, elementList, size);
				opposeElements(opposePairs, numOpp, elementList, size);
			}
		}
		// now print out elementList
		cout << "[";

		for (int k=0; k<size; k++)
		{
			if (k > 0)
			{
				cout << ", ";
			}
			cout << elementList[k];
		}

		cout << "]";
		cout << endl;

	}
	return 0;
}

void combineElements(string combinePairs[], int numComb, char elementList[], int &size)
{
	char firstChar = elementList[size-2];
	char secondChar = elementList[size-1];

	for (int i=0; i<numComb; i++)
	{
		if (combinePairs[i][0] == firstChar && combinePairs[i][1] == secondChar)
		{
			elementList[size-2] = combinePairs[i][2];
			size--;
			return;	
		}
		else if (combinePairs[i][0] == secondChar && combinePairs[i][1] == firstChar)
		{
			elementList[size-2] = combinePairs[i][2];
			size--;
			return;
		}

	}
	return;
}
void opposeElements(string opposePairs[], int numOpp, char elementList[], int &size)
{
	char newChar = elementList[size-1];
	
	for (int i=0; i<numOpp; i++)
	{
		if (opposePairs[i][0] == newChar)
		{
			for (int j=0; j<size; j++)
			{
				if (elementList[j] == opposePairs[i][1])
				{
					size = 0;
					return;
				}
			}
		}
		else if (opposePairs[i][1] == newChar)
		{
			for (int j=0; j<size; j++)
			{
				if (elementList[j] == opposePairs[i][0])
				{
					size = 0;
					return;
				}
			}
		}
	}
	return;
}
