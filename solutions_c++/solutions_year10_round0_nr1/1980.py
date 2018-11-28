////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam '2010
// Qualificatino Round - A. 
//
// Author : Kang, Jin-Kook, 2010.05.08
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
4
1 0
1 1
4 0
4 47   
   
Output 
Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON
*/

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("input.txt");
//#define cin fin

bool _isLightOn( int n, int k )
{
	return ( k % ( 1 << n ) ) + 1 == ( 1 << n );
}

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		int n, k;
		cin >> n >> k;

		bool bResult = _isLightOn( n, k );

		cout << "Case #" << i << ":" << ( bResult ? " ON" : " OFF" ) << endl;
	}

	return 0;
}
