#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;
using namespace std;

struct task
{
	int _n;
};


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int testCase;
	cin >> testCase;
	char _ch;
	int _value;
	for( int tCase=1; tCase<=testCase; ++tCase )
	{
		vector<int> _Task[2];
		
		int solution = 0;
		
		int taskNum;
		cin >> taskNum;
		_Task[0].resize( taskNum );
		_Task[1].resize( taskNum );
		for( int tn=0; tn<taskNum; ++tn )
		{
			cin >> _ch  >> _value;
			_Task[_ch=='B'?0:1][tn] = _value;
		}

		// 수행해야하는 task수
		int start[2];
		start[0] = start[1] = 1;
		int overlap[2];
		overlap[0] = overlap[1] = 0;
		int time = 0;

		for( int tn=0; tn<taskNum; ++tn )
		{
			int B = _Task[0][tn]==0?1:0;

			int move = abs( _Task[B][tn] - start[B] );
			int eng = move + 1;
			if( overlap[B] >= eng )
			{
				overlap[B] = 0;
				time += 1;
				overlap[ B ^ 1 ] += 1;
			}
			else
			{
				overlap[ B ^ 1 ] += (eng - overlap[B]);
				time += (eng - overlap[B]);
				overlap[B] = 0;
			}

			start[B] = _Task[B][tn];
		}

		printf( "Case #%d: %d", tCase, time );
		if( tCase != testCase )
			printf( "\n" );
	}

	return 0;
}