// SnapperChain.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include "SnapperTree.h"

using namespace std;

bool getState( int N, int K );
bool getSnapperState( SnapperTree* snapperList, int size );


int main(int argc, char* argv[])
{
	int T( 10000 ); 
	int *N = new int[T];
	int *K = new int[T];
	int testCase;
	cin>> testCase;
	for( int i =0 ; i < testCase ; i++ )
	{
		cin >> N[i] >> K[i];
	}

	for( int i =0 ; i < testCase ; i++ )
	{
		char* string( getState( N[i], K[i] )?"ON":"OFF" ); 		
		cout << "case #"<< i+1 << " " << string << "\n"; 
	}
	
	delete[] N;
	delete[] K;
	cin >> T;
	return 0;
}


bool getState( int N, int K )
{
	SnapperTree *snapperState = new SnapperTree[N];

	while( K )
	{
		for( int counter = 0; counter < N; counter++ )
		{	
			snapperState[ counter ].setState( !snapperState[ counter ].getState() );
			if( snapperState[ counter ].getState() )
			{
				break;
			}			
		}
		K--;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
	}

	return (getSnapperState( snapperState, N ));

}

bool getSnapperState( SnapperTree* snapperList, int size )
{
	bool state(true);
	for( int counter = 0; counter < size ; counter++ )
	{
		if( !snapperList[ counter ].getState() )
		{
			state = false;
			break;
		}
	}
	return state;
}