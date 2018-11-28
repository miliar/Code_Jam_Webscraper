// -*- compile-command: "g++ -o main -Wall -Wextra -g tictactoa.cpp" -*-
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <vector>
#include <utility>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <sstream>
#include <stack>
#define FOR(i,c) for(__typeof(c.begin()) i=c.begin();i!=c.end();++i)
using namespace std;

int diagX[2][4] = {{0,1,2,3},{3,2,1,0}};
int diagY[2][4] = {{0,1,2,3},{0,1,2,3}};

int main() {
    int T = 0;
    scanf("%d", &T);
    getchar();
    // field[x][y]
    char field[4][4] = {};
    for( int t = 0; t < T; t++ ) {
	// For each testcase
	for( int iy = 0; iy < 4; iy++ ) {
	    for( int ix = 0; ix < 4; ix++ ) {
		field[ix][iy] = getchar();
	    }
	    getchar();
	}
	getchar();
	

	bool isFull = true;
	bool hasWinner = false;
	char winner;

	// check horizontal
	for( size_t y = 0; y < 4 && !hasWinner; y++ ) {
	    bool xWin = true;
	    bool oWin = true;
	    for( size_t x = 0; x < 4; x++ ) {
		if( field[x][y] == '.') {
		    isFull = false;
		    xWin = false;
		    oWin = false;
		} else if( field[x][y] == 'X')
		    oWin = false;
		else if( field[x][y] == 'O')
		    xWin = false;		
	    }
	    if( xWin ) {
		hasWinner = true;
		winner = 'X';
	    }
	    if( oWin ) {
		hasWinner = true;
		winner = 'O';
	    }
	}

	//check vertical
	for( size_t x = 0; x < 4 && !hasWinner; x++ ) {
	    bool xWin = true;
	    bool oWin = true;
	    for( size_t y = 0; y < 4; y++ ) {
		if( field[x][y] == '.' ) {
		    xWin = false;
		    oWin = false;
		}
		if( field[x][y] == 'X')
		    oWin = false;
		if( field[x][y] == 'O')
		    xWin = false;
	    }
	    if( xWin ) {
		hasWinner = true;
		winner = 'X';
	    }
	    if( oWin ) {
		hasWinner = true;
		winner = 'O';
	    }
	}
       

	// check diagonal
	for( size_t x = 0; x < 2 && !hasWinner; x++ ) {
	    bool xWin = true;
	    bool oWin = true;
	    for( size_t y = 0; y < 4; y++ ) {
		char diagField = field[diagX[x][y]][diagY[x][y]];
		if( diagField == '.' ) {
		    xWin = false;
		    oWin = false;
		}
		if( diagField == 'X')
		    oWin = false;
		if( diagField == 'O')
		    xWin = false;
	    }
	    if( xWin ) {
		hasWinner = true;
		winner = 'X';
	    }
	    if( oWin ) {
		hasWinner = true;
		winner = 'O';
	    }
	}
	
	if( isFull && !hasWinner )
	    printf("Case #%d: Draw\n", t+1);
	if( !isFull && !hasWinner )
	    printf("Case #%d: Game has not completed\n", t+1);
	if( hasWinner && winner == 'X')
	    printf("Case #%d: X won\n", t+1);
	if( hasWinner && winner == 'O')
	    printf("Case #%d: O won\n", t+1);
    }


  return 0;
}
