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

int make_word(char a , char b )
{
	return (int)a << 8 | b; 
}

char make_upper_word(int a)
{
	return (char)(a >> 8); 
}

char make_lower_word(int a)
{
	return a & 0xff; 
}

typedef struct
{
	vector<pair<int,char>> com;
	vector<int> opp;
	vector<char> str;
}Problem;

bool is_opp( const vector<int> &opp , vector<char>str )
{
	for( auto itr = opp.begin() ; itr != opp.end() ; ++itr )
	{
		char u = make_upper_word(*itr);
		char l = make_lower_word(*itr);
		if( find(str.begin(),str.end(),u) != str.end() &&
			find(str.begin(),str.end(),l) != str.end() )
		{
			return true;
		}
	}
	return false;
}

vector<char> patch_com( const vector<pair<int,char>> &com , vector<char>str )
{
	if( str.size() < 2 ) return str;

	for( auto itr = com.begin() ; itr != com.end() ; ++itr )
	{
		char u = make_upper_word(itr->first);
		char l = make_lower_word(itr->first);
		if( str[str.size()-1] == u && str[str.size()-2] == l ||
			str[str.size()-1] == l && str[str.size()-2] == u)
		{
			vector<char> newstr( str.begin() , str.end() - 2 );
			newstr.push_back( itr->second );
			return patch_com(com,newstr);
		}
	}
	return str;
}

void solve( const Problem &p , vector<char>& solved )
{
	vector<char> str;
	for( int i = 0 ; i < p.str.size() ; ++i )
	{
		str.push_back( p.str[i] );
		str = patch_com( p.com , str );
		if( is_opp( p.opp , str ) )
		{
			str.clear();
		}
	}
	solved = str;
	return;
}

bool read_problem( const _TCHAR *fname , vector<Problem>& problems )
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
				Problem p;
				int pos = 0;
				int number2 = strtoul( line.c_str() + pos , NULL , 10 );
				pos = line.find(" ",pos+1);
				for( int i = 0 ; i < number2 ; ++i )
				{
					p.com.push_back(
						make_pair( make_word( *(line.c_str() + pos + 1) , *(line.c_str() + pos + 2) ) ,
						*(line.c_str() + pos + 3) ) );
					pos +=3;
				}
				++pos;
				int number3 = strtoul( line.c_str() + pos , NULL , 10 );
				pos = line.find(" ",pos+1);
				for( int i = 0 ; i < number3 ; ++i )
				{
					p.opp.push_back( make_word( *(line.c_str() + pos + 1) , *(line.c_str() + pos + 2) ) );
					pos +=2;
				}
				++pos;

				int number4 = strtoul( line.c_str() + pos , NULL , 10 );
				pos = line.find(" ",pos+1);
				for( int i = 0 ; i < number4 ; ++i )
				{
					p.str.push_back( *(line.c_str() + pos + 1) );
					pos += 1;
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
		vector<char> solved;
		solve(*itr,solved);
		printf("Case #%d: [",++count);
		for( auto itr2 = solved.begin() ; itr2 != solved.end() ; ++itr2 )
		{
			if( itr2 + 1 != solved.end() )
			{
				printf("%c, ",*itr2);
			}else
			{
				printf("%c]\n",*itr2);
			}
		}
		if( solved.size() == 0 ) printf("]\n");
	}

	return 0;
}

