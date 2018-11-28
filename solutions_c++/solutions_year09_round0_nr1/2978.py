#include <iostream>
#include <set>
#include <vector> 
#include <string>
#include <algorithm>
#include <cassert>

namespace
{
	using namespace std;
	vector<string> S ;
}

struct T
{
	char v[26] ;
	int count ;
	bool find ( char c )const
	{
		int cnt = 0 ;
		while ( cnt < count )
			if ( v[cnt++] == c ) return true ;
		return false ;
	}
} ;

bool match ( std::string s, const std::vector<T>& v )
{
	bool match =true ;
	for ( int i = 0 ; i < s.size() ; ++i )
	{
		const char *begin = v[i].v, *end = v[i].v + v[i].count ;
		if ( !v[i].find(s[i]) )
		{
			match = false ;
			break ;
		}
	}
	return match ;
}

int main()
{
	int L, D, N ;
	std::cin >> L >> D >> N ;
	std::string s ;

	for ( int i = 0 ; i < D ; ++i )
	{
		std::cin >> s ;
		S.push_back ( s ) ;
	}
	
	for ( int i = 0 ; i < N ; ++i )
	{
		std::string input ;
		std::cin >> input ;
		std::vector<T> v ;
		int size = input.size( ) ;
		int count = 0 ;
		while ( count < size )
		{			
			T t ;
			t.count = 0 ;
			if ( 'a' <= input[count] and input[count] <= 'z' )
			{
				t.v[t.count++] = input[count] ;
			}
			else if ( input[count] == '(' )
			{
				++count ;
				while ( input[count] != ')' )
				{
					t.v[t.count++] = input[count++] ;
				}
			}
			++count ;
			v.push_back(t) ;
		}

		count = 0 ;
		for ( int i = 0 ; i < D ; ++i )
		{
			if ( match ( S[i], v ) )
				++count ;
		}
		std::cout << "Case #" << i+1 << ": " << count << "\n" ;		
	}
}
