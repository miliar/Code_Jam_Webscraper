////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam '2011
// Qualificatino Round - A. 
//
// Author : Kang, Jin-Kook, 2011.05.07
//
// * 
//

#include <stdio.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

////////////////////////////////////////////////////////////////////////////////
//
/*
Input 
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

Output 
Case #1: 6
Case #2: 100
Case #3: 4
*/

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("input.txt");
//#define cin fin

#define MAX_INST	100

enum ROBOT_TYPES {
	ORANGE = 0,
	BLUE,
	ROBOT_COUNT
};

struct Instruction
{
	char m_cRobot;		// robot id
	int m_nButton;		// button number
};

int calcSeconds( Instruction* rgInst, int const& count )
{
	// initialize robots
	int rgLastButton[ ROBOT_COUNT ] = { 1, 1 };
	int rgLastMoved[ ROBOT_COUNT ] = { 0, 0 };
	int nSeconds = 0;

	// count
	for ( int i = 0; i < count; ++i ) {
		Instruction const& curInst = rgInst[ i ];
		char robot = curInst.m_cRobot;
		int button = curInst.m_nButton;

		int needed = abs( button - rgLastButton[ robot ] );
		int extraSecond = max( needed - ( nSeconds - rgLastMoved[ robot ] ), 0 ) + 1;
		nSeconds += extraSecond;

		rgLastButton[ robot ] = button;
		rgLastMoved[ robot ] = nSeconds;
	}

	return nSeconds;
}

int main( int argc, char *argv[] )
{
	Instruction instructions[ MAX_INST ];

	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		int n, button;
		char robot;
		cin >> n;

		for ( int j = 0; j < n; ++j ) {
			Instruction& inst = instructions[ j ];
			cin >> robot >> button;

			if ( robot == 'O' ) robot = ORANGE;
			else if ( robot == 'B' ) robot = BLUE;
			else exit( 1 );

			inst.m_cRobot = robot;
			inst.m_nButton = button;
		}

		int nResult = calcSeconds( instructions, n );

		cout << "Case #" << i << ": " << nResult << endl;
	}

	return 0;
}
