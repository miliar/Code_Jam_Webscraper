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


typedef struct
{
	char r;
	int num;
}Act;

typedef std::vector<Act> Problem;

int solve( const Problem &p )
{
	int total = 0;
	int cost[2];
	cost[0] = cost[1] = 0;

	char current = '\0';
	int s[2];
	s[0] = s[1] = 1;

	for( int i = 0 ; i < p.size() ; ++i )
	{
		int index = ( p[i].r == 'O' ) ? 1 : 0;
		int step = abs( s[index] - p[i].num ) + 1;
		cost[index] = max(cost[index^1]+1 , cost[index] + step);
		s[index] = p[i].num;
		current = p[i].r;
	}
	return max(cost[0],cost[1]);
}

bool read_problem( const _TCHAR *fname , std::vector<Problem>& problems )
{
	std::fstream ifs;
	ifs.open( fname );
	std::string line;

	if( ifs.is_open() )
	{
		if( getline( ifs , line ) )
		{
			int number = strtoul( line.c_str() , NULL , 10);
			while( getline( ifs , line ) )
			{
				int number2 = strtoul( line.c_str() , NULL , 10);
				int pos = line.find(" ");
				Problem p;
				for( int j = 0 ; j < number2 ; ++j )
				{
					Act a;
					a.r = *(line.c_str() + pos+1);
					pos = line.find(" ",pos+1);
					a.num = strtoul( line.c_str() + pos , NULL , 10 );
					pos = line.find(" ",pos+1);

					p.push_back(a);
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

	std::vector<Problem> problem;

	if( !read_problem(argv[1],problem) ) return -1;

	int count = 0;
	for( auto itr = problem.begin() ; itr != problem.end() ; ++itr )
	{
		int s = solve(*itr);
		printf("Case #%d: %d\n",++count,s);
	}

	return 0;
}

