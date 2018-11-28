#include <iostream>
#include <fstream>
#include <vector>

int patrickAdd( int v1, int v2 )
{
	int result = 0;
	for( int i = 0; i < 32; ++i )
	{
		int v1Mask = v1 & (1 << i);
		int v2Mask = v2 & (1 << i);

		if ( v1Mask & v2Mask )
			continue;
		if ( v1Mask | v2Mask )
			result += 1 << i;
	}
	return result;
}

int getPatricPileSize( std::vector< int >& pList )
{
	int result = 0, listSize = pList.size();
	for ( int j = 0; j < listSize; ++j )
		result = patrickAdd( result, pList[j] );
	return result;
}

int getSeanPileSize( std::vector< int >& pList )
{
	int result = 0, listSize = pList.size();
	for ( int j = 0; j < listSize; ++j )
		result += pList[j];
	return result;
}

void recursiveSearch( int index, std::vector< int >& pList, int pListSize, int pCurrentTotal, int pPatTotal, int& pLargestTotal, bool& pFound )
{
	int val = pList[ index ];
	pList[ index ] = 0;

	int accumTotalPat = patrickAdd( pPatTotal, val );
	int listTotalPat = getPatricPileSize( pList );

	int accumTotal = pCurrentTotal + val;

	if ( accumTotalPat == listTotalPat && listTotalPat != 0 )
	{
		int listTotal = getSeanPileSize( pList );

		pFound = true;
	
		if ( accumTotal > pLargestTotal )
			pLargestTotal = accumTotal;

		if ( listTotal > pLargestTotal )
			pLargestTotal = listTotal;
	}

	int modInt = index;

	while ( ++modInt < pListSize )
		recursiveSearch( modInt, pList, pListSize, accumTotal, accumTotalPat, pLargestTotal, pFound );

	pList[ index ] = val;	
}

int main()
{
	std::ifstream fin( "C:/Users/0xc0deface/Downloads/C-small-attempt0.in" );
	std::ofstream fout( "C:/Users/0xc0deface/Desktop/test.out" );

	int testCases;
	fin >> testCases;

	for ( int i = 0; i < testCases; ++i )
	{

		int numCandies;
		fin >> numCandies;

		std::vector< int > candyList;

		for ( int j = 0; j < numCandies; ++j )
		{
			int candy;
			fin >> candy;
			candyList.push_back( candy );
		}

		int pileSize = 0;
		bool foundMatch = false;

		recursiveSearch( 0, candyList, candyList.size(), 0, 0, pileSize, foundMatch );

		if ( !foundMatch )
			fout << "Case #" << i+1 << ": NO" << std::endl;
		else
			fout << "Case #" << i+1 << ": " << pileSize << std::endl;
	}
	return 0;
}
