#include <cstdio>
#include <iostream>
#include <vector>
#include <fstream>
#include <cassert>
#include <string>
#include <algorithm>
#include <iomanip>
#include <functional>
#include <map>
#include <set>
#include <list>
#include <deque>
using namespace std;

#include <math.h>




void FilterWords(list<string> & t, int pos,const string & letters)
{
	for( list<string>::iterator iter = t.begin(); iter != t.end();  )
	{
		string & word = *iter;
		bool have = false;
		for( size_t j = 0; j < letters.size(); ++j )
		{
			if( word[pos] == letters[j] )
			{
				have = true;
				break;
			}
		}
		if( ! have )
		{
			t.erase(iter++);
		}
		else
			++iter;
	}

}

int GetMatches(const list<string> & words, const string & pattern)
{
	list<string> t(words);

	bool start = false;

	string letters;
	int pos = 0;
	for( size_t i = 0; i < pattern.size(); ++i )
	{
		if( pattern[i] == '(')
		{
			start = true;
		}
		else if( pattern[i] == ')' )
		{
			FilterWords(t,pos,letters);
			pos++;
			letters.clear();
			start = false;
		}
		else
		{
			letters.push_back(pattern[i]);
			if( !start )
			{
				FilterWords(t,pos,letters);
				pos++;
				letters.clear();
			}
		}
	}

	return t.size();
}


int main(int argc, char* argv[])
{

	if ( argc < 3 )
	{
		cout << "Round1 inputfile outputfile" << endl;
		return 1;
	}

	ifstream in(argv[1],ios::in);
	ofstream out(argv[2]);
	if( !in )
	{
		cout << "can't open input file" << endl;
		return 1;
	}

	if( !out )
	{
		cout << "can't open output file" << endl;
		return 1;
	}
	
	int L,D,N;
	in >> L >> D >> N;

	list<string> words;
	for( int i = 0; i < D; ++i )
	{
		string s;
		in >> s;
		words.push_back(s);
	}

	for( int  i = 0; i < N; ++i )
	{
		string pattern;
		in >> pattern;
		out << "Case #" << i+1 << ": " << GetMatches(words,pattern) << "\n";
	}
	return 0;
}

