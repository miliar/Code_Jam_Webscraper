#include <iostream>
#include <memory.h>
#include <vector>
#include <limits.h>
#include <assert.h>

using namespace std;

vector< vector< int > > give_scores_without_suprises( const vector< int >& googlers )
{
	vector< vector< int > > scores;
	for ( int i = 0; i < googlers.size(); i++ )
	{
		vector< int > triplet;
	
		triplet.push_back( 0 );
		triplet.push_back( 0 );
		triplet.push_back( 0 );

		int value = googlers[ i ];
		int index = 0;

		while ( value-- > 0 )
		{
			triplet[ index++ % triplet.size() ]++;
		}

		scores.push_back( triplet );
	}
	return scores;
}

void maximize_scores_based_on_suprises( int s, int p, vector< vector< int > >& triplets )
{
	while ( s > 0 )
	{
		//cout << "s: " << s << " p: " << p << " triplets.size = " << triplets.size() << "\n";

		// find best triplet to skew with a suprise
		int bestIndex = -1;
		int bestIndexIncrement = -1;
		int bestIndexDecrement = -1;
		int bestDiff = INT_MAX;
		for ( int i = 0; i < triplets.size(); i++ )
		{
			//cout << i << "\n";
			int bestIndexIncrementTemp = -1;
			int bestIndexDecrementTemp = -1;
			int bestDiffTemp = INT_MAX;			

			int maxValue = -INT_MAX;
			int minValue = INT_MAX;
			for ( int j = 0; j < triplets[ i ].size(); j++ )
			{
				maxValue = triplets[ i ][ j ] > maxValue ? triplets[ i ][ j ] : maxValue;
				minValue = triplets[ i ][ j ] < minValue ? triplets[ i ][ j ] : minValue;

				// find best index for incrementing
				if ( p - triplets[ i ][ j ] < bestDiffTemp )
				{
					bestDiffTemp = p - triplets[ i ][ j ];
					bestIndexIncrementTemp = j;
				}
				else if ( triplets[ i ][ j ] > 0 && bestIndexIncrementTemp != -1 && triplets[ i ][ j ] == triplets[ i ][ bestIndexIncrementTemp ] )
				{
					bestIndexDecrementTemp = j;
				} 
			}

			// can't skew this any more
			if ( maxValue - minValue  >= 2 )
			{
				//cout << "can't skew more\n";
				continue;
			}

			// did not find a suitable index to decrement
			if ( bestIndexDecrementTemp == -1 || bestIndexIncrementTemp == -1 )
			{
				//cout << "ignore: no dec/inc index\n";
				continue;
			}

			// above p threshold
			if ( maxValue >= p )
			{
				//cout << "ignore: " << maxValue << " above p " << p << "\n";
				continue;
			}

			if ( bestDiffTemp >= bestDiff )
			{
				//cout << "ignore: " << bestDiffTemp << " above diff " << bestDiff << "\n";	
				continue;
			}
			

			bestIndex = i;
			bestDiff = bestDiffTemp;
			bestIndexIncrement = bestIndexIncrementTemp;
			bestIndexDecrement = bestIndexDecrementTemp;
		}

		//cout << " bestIndex: " << bestIndex << "\n";

		if ( bestIndex < 0 )
		{
			break;
		}

		// skew
		//cout << "skew triplets[" << bestIndex << "][" << bestIndexIncrement << "]" << " and " << bestIndexDecrement << "\n";
		triplets[ bestIndex ][ bestIndexIncrement ]++;
		triplets[ bestIndex ][ bestIndexDecrement ]--;		
		
		s--;
	}
}

int solve( int suprising, int p, const vector< int >& googlers )
{
	vector< vector< int > > triplets;

	// distribute scores by judge without suprises
	triplets = give_scores_without_suprises( googlers );

	/*
	for ( int i = 0; i < triplets.size(); i++ )
	{
		cout << i << ":";
		for ( int j = 0; j < triplets[ i ].size(); j++ )
		{
			cout << " " << triplets[ i ][ j ];
		}
		cout << "\n";
	}
	*/

	maximize_scores_based_on_suprises( suprising, p, triplets );

	/*
	for ( int i = 0; i < triplets.size(); i++ )
	{
		cout << i << ":";
		for ( int j = 0; j < triplets[ i ].size(); j++ )
		{
			cout << " " << triplets[ i ][ j ];
		}
		cout << "\n";
	}
	*/

	// add up people with at least one judge above or equal to p
	int result = 0;
	for ( int i = 0; i < triplets.size(); i++ )
	{
		bool found = false;
		for ( int j = 0; j < triplets[ i ].size(); j++ )
		{
			if ( triplets[ i ][ j ] >= p )
			{
				found = true;
				break;
			}
		}
		if ( found )
		{
			result++;
		}
	}

	return result;
}

int main( int argc, char* argv[] )
{
	int cases;
	cin >> cases;
	//cout << "cases: " << cases << "\n";
	cin.ignore();
	
	int cur = 0;
	while ( cur++ < cases )
	{
		int numGooglers;
		cin >> numGooglers;
		//cout << "g: " << numGooglers << " ";

		int suprising;
		cin >> suprising;
		//cout << "s: " << suprising << " ";

		int p;
		cin >> p;
		//cout << "p: " << p << " ";

		//cout << "p: ";
		vector< int > googlers;
		while ( numGooglers-- > 0 )
		{
			int value;
			cin >> value;
			googlers.push_back( value );
			//cout << " " << googlers[ googlers.size() - 1 ];
		}
		//cout << "\n";

		int result = solve( suprising, p, googlers );
		cout << "Case #" << cur << ": " << result << "\n";
	}

	return 0;
}
