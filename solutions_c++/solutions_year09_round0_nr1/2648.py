// CodeJam.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include <tchar.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
using namespace std;


int L , D , N;


class CharElem
{
public:
	bool Match(char c)
	{
		if ( vals.find( c ) != vals.end() )
			return true;
		else
			return false;
	}

	set<char> vals;
};
typedef vector<CharElem> CharElemAry;

vector<string> words;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifs("C:\\ws\\Codejam\\A-small-attempt1.in");
	ofstream ofs("C:\\ws\\Codejam\\OUT.out");

	ifs >> L >> D >> N;

	words.resize(D);
	for( size_t i = 0 ; i < D ; ++i )
	{
		ifs >> words[i];
	}

	for( size_t i = 0 ; i < N ; ++i )
	{
		CharElemAry elems;
		elems.reserve(L);

		string s;
		ifs >> s;
		//getline( ifs , s );
		bool in_mult = false;
		for( size_t j = 0 ; j < s.size() ; ++j )
		{
			char c = s[j];
			if( c == '(' )
			{
				in_mult = true;
				elems.push_back( CharElem() );
				continue;
			}
			if( c == ')' )
			{
				in_mult = false;
				continue;
			}

			if( in_mult )
			{
				elems.back().vals.insert( c );
			}
			else
			{
				elems.push_back( CharElem() );
				elems.back().vals.insert( c );
			}
		}

		int num_matched = 0;
		for( size_t j = 0 ; j < D ; ++j )
		{
			string& w = words[j];
			int addr = 1;
			for( size_t k = 0 ; k < w.size() ; ++k )
			{
				if( elems[k].Match( w[k] ) == false )
				{				
					addr = 0;
					break;
				}
			}
			num_matched += addr;
		}

		ofs << "Case #" << (i+1) << ": " << num_matched << endl;
		cout << "Case #" << (i+1) << ": " << num_matched << endl;
	}

	cout << "end" << endl;
	return 0;
}

