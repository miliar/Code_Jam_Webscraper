#include <stdio.h>
#include <stdlib.h>
#include <new>
#include <limits.h>
#include <iostream>

using namespace std;
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

void sortIt(int *anArray, int aCount)
{
  qsort (anArray, aCount, sizeof(int), compare);
}

int main()
{
	int nrCases;	
	cin >> nrCases;
	
	for (int caseNr = 0; caseNr < nrCases; caseNr++)
	{
		int count;
		cin >> count;
		long result = 0;
		long smallest = 0;
		long total = 0;
		for (int i = 0; i < count; i++)
		{
			long next;
			cin >> next;
			result = result ^ next;
			
			if (smallest == 0 || smallest > next)
			{
				smallest = next;
			}
			
			total = total + next;
			
			
		}
		
		cout << "Case #" << caseNr + 1 << ": ";
		if (result != 0)
		{
			cout << "NO";
		}
		else
		{
			cout << total - smallest;

		}
		
		cout <<endl;
		
	}
}
