#include <stdio.h>
#include <vector>
#include <iostream>
#include <string.h>
#include <limits>

#define MAX_ENGINES 110
#define MAX_QUERIES 1100
#define MIN(a,b) ((a<b) ? (a) : (b))

using namespace std;

int dp[ MAX_ENGINES ][ MAX_QUERIES ];
vector<string>	engines;
vector<string>	queries;	

int optimize_switching(int S, int Q)
{
	int		i, j, k;
	int 	result = std::numeric_limits<int>::max();
	int 	max_int = std::numeric_limits<int>::max() - MAX_ENGINES;
	int		best_res;
	int		best_in_row;

	memset( dp, 0, sizeof(dp) );
	
	for ( i = 0; i < S; i++ ){
		dp[ i ][ Q ] = 0;
	}

	for ( i = Q-1; i >= 0; i-- ){
		best_in_row = max_int;

		for (j = 0; j < S; j++)
			best_in_row = MIN(dp[ j ][ i+1 ], best_in_row);	

		for ( j = 0; j < S; j++ ){
			if ( engines[ j ] == queries[ i ] ){
				dp[ j ][ i ] = max_int;
			} else {
				dp[ j ][ i ] = MIN(best_in_row + 1, dp[ j ][ i+1 ]);
			}
		}
	}	

	for ( i = 0; i < S; i++ ){
		result = MIN(result, dp[ i ][ 0 ]);
	}	

	

	return result;
}

int main(){
	int 			nCases;
	int				nSE, nQueries;
	int				i,j;
	int				minSwitches;
	int				caseCount = 1;

	scanf("%d", &nCases);

	while (nCases--){
		scanf("%d\n", &nSE);
			

		//cleanup
		engines.clear(); queries.clear();

		for ( i = 0; i < nSE; i++ ){
			string engine;

			getline(cin, engine);
			engines.push_back(engine);
		}
		
		scanf("%d\n", &nQueries);

		for ( i = 0; i < nQueries; i++ ){
			string query;

			getline(cin, query);
			queries.push_back(query);

		}

		minSwitches = optimize_switching(nSE, nQueries);
		
		printf("Case #%d: %d\n",caseCount, minSwitches);

		caseCount++;
	}

}
