#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <stack>
#include <set>
#include <cstring>
using namespace std;

int findAllPossibleCombinations( long, long);

int main(int argv, char* argc[] )
{
	fstream myInFile, myOutFile;
	myInFile.open( argc[1], ios::in);
	myOutFile.open( "ProblemC.out", ios::out );
	if( myInFile.is_open() )
	{
		int aNumberOfTestCases;
		int aCount = 1;
		myInFile >> aNumberOfTestCases;
		while( !myInFile.eof() && aNumberOfTestCases > 0 )
		{
			long aStart, aFinish;
			myInFile >> aStart >> aFinish;
			myOutFile << "Case #" << aCount <<": " << findAllPossibleCombinations( aStart, aFinish ) <<endl;
			aCount++;
			aNumberOfTestCases--;
		}
	}

	myOutFile.close();
	myInFile.close();
}

void getAllDigits( long number_in, vector<int>& digits_in)
{
	stack<int> myTempStack;
	while( number_in )
	{
		myTempStack.push( number_in % 10 );
		number_in /= 10;
	}
	while( !myTempStack.empty() )
	{
		digits_in.push_back( myTempStack.top() );
		myTempStack.pop();
	}
}

long convertToNumber( vector<int> digits_in )
{
	vector<int>::iterator anIterator;
	long aNumber = 0;
		
	for( anIterator = digits_in.begin(); anIterator != digits_in.end() ; anIterator++ )
	{
		aNumber = (aNumber * 10) + *anIterator;
	}

	return aNumber;
}

int findAllPossibleCombinations( long begin_in, long end_in )
{
	int aTotalCombinations = 0;
	set<long> myNumbers;
	
	for( long nextNumber = begin_in; nextNumber <= end_in; nextNumber++ )
	{
		vector<int> myDigits;
		vector<int>::iterator myIterator;
				
		getAllDigits( nextNumber, myDigits);
		int noOfCombinations = 0;

		for( int i=1; i < myDigits.size(); i++ )
		{
			vector<int> myDigitsNew;
			myDigitsNew.resize( myDigits.size());
	
			rotate_copy( myDigits.begin(), myDigits.end() - i, myDigits.end(), myDigitsNew.begin() );
			
			long aNewNumber = convertToNumber( myDigitsNew );
			if( aNewNumber <= end_in && aNewNumber >= begin_in && aNewNumber != nextNumber)
			{
				pair<set<long>::iterator,bool> aRet;
				aRet = myNumbers.insert( aNewNumber );
				if( aRet.second )
					noOfCombinations++;
			}
		}
		if( noOfCombinations != 0)
		{
			myNumbers.insert( nextNumber );
			aTotalCombinations += noOfCombinations;
			while( noOfCombinations > 0 )
			{
				noOfCombinations--;
				aTotalCombinations += noOfCombinations;
			}
		}
	}

	return aTotalCombinations;
}