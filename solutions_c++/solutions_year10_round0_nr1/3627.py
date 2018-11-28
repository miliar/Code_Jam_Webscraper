#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <math.h>
using namespace std;

int main(void)
{
	int numberOfTest ;
	int numberOfSnapper ;
	unsigned long numberOfSnap ;


	cin >> numberOfTest ;


	for(int i = 1 ; i <= numberOfTest ; i++)
	{
		cin >> numberOfSnapper ;
		cin >> numberOfSnap ;

		unsigned long checkNumber = 1 ;
		
		for(int j = 0 ; j < numberOfSnapper ; j++)
		{
			checkNumber *= 2 ;
		}

		checkNumber-- ;

		if( (numberOfSnap & checkNumber) == checkNumber )
		{
			cout << "Case #" << i << ": ON" << endl ;
		}
		else
		{
			cout << "Case #" << i << ": OFF" << endl ;
		}
	}

	return 0 ;
}