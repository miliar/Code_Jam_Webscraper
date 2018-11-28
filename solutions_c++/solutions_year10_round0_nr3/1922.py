////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam '2010
// Qualificatino Round - C. 
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
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3

Output 
Case #1: 21
Case #2: 100
Case #3: 20 
*/

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("input.txt");
//#define cin fin

typedef unsigned long long ull;

struct GroupInfo
{
	int		m_nCount;
	bool	m_bVisited;
};

struct HeadInfo
{
	int		m_nNext;
	ull		m_nEuros;
};

typedef vector< GroupInfo > Groups;
typedef vector< HeadInfo > Heads;


ull calcIncome( int r, int k, Groups& groups )
{
	int n = groups.size(), index = 0;
	Heads heads;
	heads.resize( n );
	
	ull sum = 0;
	for ( int nCur = 0, nNext = 0, len = 0; nCur < n; ) {
		GroupInfo& infoCur = groups[ nCur % n ];
		GroupInfo& infoNext = groups[ nNext % n ];

		if ( sum + infoNext.m_nCount > k || len + 1 > n ) {
			heads[ nCur ].m_nNext = nNext;
			heads[ nCur ].m_nEuros = sum;
			sum -= infoCur.m_nCount;
			--len;
			++nCur;
		}
		else {
			++len;
			sum += infoNext.m_nCount;
			nNext = ( nNext + 1 ) % n;
		}
	}

	vector< int > path;
	vector< ull > accumEuros;
	path.resize( n );
	accumEuros.resize( n );
	sum = 0;
	int i;
	for ( i = 0; i <= n; ++i ) {
		GroupInfo& info = groups[ index ];

		if ( i == r )
			return sum;

		if ( info.m_bVisited )
			break;

		info.m_bVisited = true;
		sum += heads[ index ].m_nEuros;
		path[ i ] = index;
		accumEuros[ i ] = sum;
		index = heads[ index ].m_nNext;
	}

	int loopBegin = 0;
	for ( ; loopBegin < n; ++loopBegin ) {
		if ( path[ loopBegin ] == index )
			break;
	}

	ull loopEuros = loopBegin ? ( sum - accumEuros[ loopBegin - 1 ] ) : sum;
	int loopLen = i - loopBegin;
	int loopCount = ( r - loopBegin ) / loopLen;
	int remain = ( r - loopBegin ) % loopLen;

	ull beforeLoopEuros = loopBegin ? ( accumEuros[ loopBegin - 1 ] ) : 0;
	ull loopTotalEuros = loopEuros * loopCount;
	ull remainEuros = remain ? ( accumEuros[ loopBegin - 1 + remain ] - beforeLoopEuros ) : 0;

	return beforeLoopEuros + loopTotalEuros + remainEuros;
}

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		int r, k, n;
		cin >> r >> k >> n;

		Groups groups;
		groups.resize( n );
		for ( int j = 0; j < n; ++j ) {
			GroupInfo& info = groups[ j ];
			cin >> info.m_nCount;
			info.m_bVisited = false;
		}

		ull euros = calcIncome( r, k, groups );

		cout << "Case #" << i << ": " << euros << endl;
	}

	return 0;
}
