// qr.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"

#include<stdio.h>
#include<fstream>
#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>

using namespace std;

int solve( const vector<int> &p )
{
	int solved = 0;
	int sum = 0;
	int m = INT_MAX;
	for( auto itr = p.begin() ; itr != p.end() ; ++itr )
	{
		solved ^= *itr;
		sum += *itr;
		m = min( m , *itr );
	}
	if( solved != 0 ) return 0;

	return sum - m;
}

bool read_problem( const _TCHAR *fname , vector<vector<int>>& problems )
{
	std::fstream ifs;
	ifs.open( fname );
	std::string line;

	if( ifs.is_open() )
	{
		if( getline( ifs , line ) )
		{
			int number = strtoul( line.c_str() , NULL , 10);
			for( int i = 0 ; i < number ; ++i )
			{
				getline( ifs , line );
				int number2 = strtoul( line.c_str() , NULL , 10);
				getline( ifs , line );
				int pos = 0;
				vector<int> p(number2);
				for( int j = 0 ; j < number2 ; ++j )
				{
					int t = strtoul( line.c_str() + pos , NULL , 10 );
					pos = line.find(" ",pos+1);
					p[j] = t;
				}
				problems.push_back( p );
			}
		}
		ifs.close();
		return true;
	}
	return false;
}


int _tmain(int argc, wchar_t* argv[])
{
	if( argc != 2 ) return -1;

	std::vector<vector<int>> problem;

	if( !read_problem(argv[1],problem) ) return -1;

	int count = 0;
	for( auto itr = problem.begin() ; itr != problem.end() ; ++itr )
	{
		int s = solve(*itr);
		if( s )
		{
			printf("Case #%d: %d\n",++count,s);
		}else
		{
			printf("Case #%d: NO\n",++count);
		}
	}

	return 0;
}

