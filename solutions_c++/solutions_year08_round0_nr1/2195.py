#include<iostream>
#include<cstdlib>
#include<fstream>
#include<string>
using namespace std;

class Universe
{
public:
	Universe( string *s, int sCount, int *q, int qCount )
	{
		engines = new string [ sCount ];
		queries = new int [ qCount ];
		numInQ = qCount;
		numOfE = sCount;

		for( int i = 0; i < sCount; i++ )
			engines[ i ] = s[ i ];

		for( int i = 0; i < qCount; i++ )
			queries[ i ] = q[ i ];
	}

	~Universe()
	{
		delete [] engines;
		delete [] queries;
	}

	int switches()
	{
		int count = 0;
		int result = 0;
		int *mem = 0;
		for( int i = 0; i < numInQ; i++ )
		{
			if( i == 0 )
			{
				mem = new int[ numOfE ];
				mem[ 0 ] = queries[ i ];
				count++;
			}
			else
			{
				for( int j = 0; j < count; j++ )
				{
					if( mem[ j ] == queries[ i ] )
						break;

					if( j == count - 1 && mem[ j ] != queries[ i ] )
					{
						mem[ count++ ] = queries[ i ];
					}
				}

				if( count == numOfE )
				{
					result++;
					delete [] mem;
					mem = new int[ numOfE ];
					mem[ 0 ] = queries[ i ];
					count = 1;
				}
			}

		}

		delete [] mem;
		return result;
	}

private:
	string *engines;
	int *queries;
	int numInQ;
	int numOfE;
};

int main()
{
	fstream inClient( "A-large.in", ios::in );
	fstream outClient( "A-large-out.txt", ios::out );

	int numOfCases;
	inClient >> numOfCases;

	string *sTmp = 0;
	int *qTmp = 0;
	Universe *uTmp = 0;

	for( int i = 0; i< numOfCases; i++ )
	{
		int numOfEngines;
		inClient >> numOfEngines;

		sTmp = new string [ numOfEngines ];

		for( int j = 0; j< numOfEngines; j++ )
		{	
			if( j == 0 )
				getline( inClient, sTmp[ j ] );
			getline( inClient, sTmp[ j ] );
		}

		int numOfQueries;
		inClient >> numOfQueries;

		qTmp = new int [ numOfQueries ];
		int qCount = 0;

		for( int j = 0; j< numOfQueries; j++ )
		{
			string temp = "";
			if( j == 0 )
				getline( inClient, temp );
			getline( inClient, temp );
			
			for( int k = 0; k < numOfEngines; k++ )
			{
				if( temp == sTmp[ k ] )
				{
					qTmp[ qCount++ ] = k;
					break;
				}
			}
		}

		uTmp = new Universe( sTmp, numOfEngines, qTmp, numOfQueries );

		outClient << "Case #" << i + 1 << ": " << uTmp -> switches() << endl;

		delete uTmp;
		delete [] sTmp;
		delete [] qTmp;
	}
	
	inClient.close();
	outClient.close();
	
	return 0;
}