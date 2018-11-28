#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<list>
#include<string>
#include<cstring>
#include<cstdlib>
#include<set>
#include<map>
#include<vector>
using namespace std;

int test_case;
vector< string > board;

bool isOk( char C, int r, int c ) {
	int charCount = 0;
	for( int i = 0; i < 4; i ++ ) {
		if( r + i < 4 && ( board[ r + i ][ c ] == C || board[ r + i ][ c ] == 'T' ) ) charCount ++ ;
	}
	
	if( charCount == 4 ) return true;

	charCount = 0;
	for( int i = 0; i < 4; i ++ ) {
		if( c + i < 4 && ( board[ r ][ c + i ] == C || board[ r ][ c + i ] == 'T' ) ) charCount ++ ;
	}
	
	if( charCount == 4 ) return true;

	charCount = 0;
	for( int i = 0; i < 4; i ++ ) {
		if( r + i < 4 && c + i < 4 && ( board[ r + i ][ c + i ] == C || board[ r + i ][ c + i ] == 'T' ) ) charCount ++ ;
	}
	
	if( charCount == 4 ) return true;

	charCount = 0;
	for( int i = 0; i < 4; i ++ ) {
		if( r + i < 4 && c - i >= 0 && ( board[ r + i ][ c - i ] == C || board[ r + i ][ c - i ] == 'T' ) ) charCount ++ ;
	}
	
	if( charCount == 4 ) return true;

	return false;
}


int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("outputA.txt", "w", stdout);
	string boardRow;
	int i,j;
	scanf("%d", &test_case);
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		board.clear();
		for( i = 0; i < 4; i ++ ) {
			cin >> boardRow;
			board.push_back( boardRow );
		}

		bool isGameOver = true;
		bool isPlayerAWinner = false;
		bool isPlayerBWinner = false;
		for( i = 0; i < 4; i ++ ) {
			for( j = 0; j < 4; j ++ ) {
				if( board[ i ][ j ] == '.' ) {
					isGameOver = false;
					continue;
				} 
				if( board[ i ][ j ] == 'X' ) {
					if( isOk('X', i, j) ) {
						isPlayerAWinner = true;
					}
				}

				else if( board[ i ][ j ] == 'O' ) {
					if( isOk('O', i, j) ) {
						isPlayerBWinner = true;
					}
				}
			}
		}

		if( isPlayerAWinner ) {
			printf("Case #%d: X won\n", caseId);
		} else if( isPlayerBWinner ) {
			printf("Case #%d: O won\n", caseId);
		} else if( !isGameOver ) {
			printf("Case #%d: Game has not completed\n", caseId);
		} else {
			printf("Case #%d: Draw\n", caseId);
		}
		
		scanf("%*c");
	}
	return 0;
}