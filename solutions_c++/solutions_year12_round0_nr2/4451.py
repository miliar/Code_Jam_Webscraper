#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

int maxN( int score )
{
	for ( int i = 10; 0 <= i; i-- )
	{
		for ( int j = 0; -1 <= j; j-- )
		{
			for ( int k = 0; -1 <= k; k-- )
			{
				if ( 0 <= i + j &&
					0 <= i + k &&
					i * 3 + j + k == score )
				{
						return i;
				}
			}
		}
	}

	return -1;
};

int maxS( int score )
{
	if ( score < 2 || 28 < score )
	{
		return -1;
	}
	
	for ( int i = 10; 2 <= i; i-- )
	{
		for ( int j = 0; -2 <= j; j-- )
		{
			if ( i * 3 - 2 + j == score )
			{
				return i;
			}
		}
	}

	return -1;
}

int main()
{
	int t;

	cin >> t;

	for ( int i = 1; i <= t; i++ )
	{
		int n, s, p, max = 0;
		vector<int> scores;

		cin >> n >> s >> p;

		for ( int j = 0; j < n; j++ )
		{
			int score;
			cin >> score;
			scores.push_back( score );
		}
		sort( scores.begin(), scores.end() );

		do
		{
			int count = 0;

			for ( int j = 0; j < n; j++ )
			{
				int currentMax;

				currentMax = j < s ? maxS( scores[j] ) : maxN( scores[j] );

				if ( currentMax == -1 )
				{
					count = -1;
					break;
				}
				else if ( p <= currentMax )
				{
					count++;
				}
			}

			if ( max < count )
			{
				max = count;
			}
		} while ( next_permutation( scores.begin(), scores.end() ) );

		cout << "Case #" << i << ": " << max << endl;
	}

	return 0;
}