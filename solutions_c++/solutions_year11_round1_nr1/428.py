#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <new>
#include <limits.h>
#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

void sortIt(int *anArray, int aCount)
{
  qsort (anArray, aCount, sizeof(int), compare);
}
int GCD(int a, int b)
{
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}

int main()
{
    cout.precision(6);

    cout.setf(ios::fixed, ios::floatfield);
    cout.setf(ios::showpoint);

	int nrCases;	
	cin >> nrCases;
	
	for (int caseNr = 0; caseNr < nrCases; caseNr++)
	{
		cout << "Case #" << caseNr + 1<< ": " ;
		long long N;
		int PD, PG;
		
		cin >> N >> PD >> PG;
		
		if (PG <= 0 && PD > 0)
		{
			cout << "Broken";
		}
		else if (PG >= 100 && PD < 100)
		{
			cout << "Broken";
		}
		else if ( N == 0)
		{
			cout << "Broken";
		}
		else if (PD == 0 && N > 0)
		{
			cout << "Possible";
		}
		else 
		{
			if (N >= 100)
			{
				cout << "Possible";
			}
			else
			{
				if (100 / GCD(100, PD) <= N)
				{
					cout << "Possible";
				}
				else
				{
					cout << "Broken";
				}
				
			}
		}
		
		cout << endl;
		
		
	}
}
