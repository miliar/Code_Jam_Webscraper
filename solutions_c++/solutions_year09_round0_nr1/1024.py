#include <iostream>
#include <string>
#include <cassert>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <algorithm>
#include <fstream>
#include <cmath>
using namespace std;

bool words[16][26];
string dic[5000];
int L, D, N;

void buildMap( string str )
{
	memset( words, false, sizeof(words) );
	int len = str.length();
	int pos = 0;
	int deep = -1;
	bool finished = true;

    while ( pos < len )
    {
		if( str[pos] == ')' )
		{
			pos++;
			finished = true;
			continue;
		}
		if ( str[pos] == '(' )
		{
			deep++;
			pos++;
			finished = false;
			continue;
		}
		if ( finished )
		{
			deep++;
		}
		int idx = str[pos]-'a';
		words[deep][idx] = true;
		pos++;
    }
}

bool isMatch( string str )
{
	int len = str.length();
	for ( int i = 0; i < len; i++ )
	{
		if ( !words[i][str[i]-'a'] )return false;
	}
	return true;
}

int getMatchedNum()
{
	int res = 0;
	for ( int i = 0; i < D; i++ )
	{
		if ( isMatch(dic[i]) )
		{
			res++;
		}
	}
	return res;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin >> L >> D >> N;
	
	for ( int i= 0; i < D; i++ )
	{
		fin >> dic[i];
	}

	string str;
	for ( int i = 1; i <= N; i++ )
	{
		fin >> str;
		buildMap( str );
		int res = getMatchedNum();
		fout << "Case #" << i << ": " << res << endl;
	}

	return 0;
}
