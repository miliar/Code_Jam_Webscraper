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

int N;
string str;
const string pattern = "welcome to code jam";
int vals[20][501];

int getNum()
{
	memset( vals, 0, sizeof(vals) );
	int len = str.length();
	for ( int i = 0; i < len; i++ )
	{
		vals[0][i] = 1;
	}

	for ( int i = 0; i <= 18; i++ )
	{
		for ( int j = 0; j < len; j++ )
		{
			vals[i+1][j+1] = vals[i+1][j];
			
			if( pattern[i] == str[j] )
			{
				vals[i+1][j+1] += vals[i][j];
				vals[i+1][j+1] %= 10000;
			}
		}
	}
	return vals[19][len];
}

string intToStr( int num )
{
	string res = "";
	res += '0' + num/1000;
	num %= 1000;
	res += '0' + num/100;
	num %= 100;
	res += '0' + num/10;
	num %= 10;
	res += '0' + num;
	return res;
}

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	fin >> N;
	getline( fin, str );
	for ( int i = 1; i <= N; i++ )
	{
		getline( fin, str );
		int num = getNum();
		fout << "Case #" << i << ": " << intToStr(num) << endl;
	}

	return 0;
}
