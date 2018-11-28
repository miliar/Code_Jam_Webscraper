// GoogleCodeJam2012-1.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifs( "A-small-attempt1.in" );
	ofstream ofs( "1.txt" );
	string str;
	int cnt = 1;
	getline(ifs, str);

	while( getline(ifs, str) )
	{
		for(int i = 0; i < str.size(); ++i )
		{
			switch( str[i] )
			{
			case 'a': str[i] = 'y'; break;
			case 'b': str[i] = 'h'; break;
			case 'c': str[i] = 'e'; break;
			case 'd': str[i] = 's'; break;
			case 'e': str[i] = 'o'; break;
			case 'f': str[i] = 'c'; break;
			case 'g': str[i] = 'v'; break;
			case 'h': str[i] = 'x'; break;
			case 'i': str[i] = 'd'; break;
			case 'j': str[i] = 'u'; break;
			case 'k': str[i] = 'i'; break;
			case 'l': str[i] = 'g'; break;
			case 'm': str[i] = 'l'; break;
			case 'n': str[i] = 'b'; break;
			case 'o': str[i] = 'k'; break;
			case 'p': str[i] = 'r'; break;
			case 'q': str[i] = 'z'; break;
			case 'r': str[i] = 't'; break;
			case 's': str[i] = 'n'; break;
			case 't': str[i] = 'w'; break;
			case 'u': str[i] = 'j'; break;
			case 'v': str[i] = 'p'; break;
			case 'w': str[i] = 'f'; break;
			case 'x': str[i] = 'm'; break;
			case 'y': str[i] = 'a'; break;
			case 'z': str[i] = 'q'; break;
			default: break;
			}
		}

		ofs << "Case #" << cnt++ << ": " << str << endl;
	}

	return 0;
}

