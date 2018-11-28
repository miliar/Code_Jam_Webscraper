// SpeakingInTongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <assert.h>

using namespace std;

// key - Googlerese ABC character
// val - English ABC character
vector<char> g_map ( 26, -1);

void translate (const char* const g_str )
{
	
	const char* g_buf = g_str;

	while ((*g_buf))
	{
		if (' ' != (*g_buf) )
			cout << (char)('a' + g_map [(*g_buf) - 'a']);
		else
			cout << ' ';
		g_buf++;
	}

	cout << endl;
}

void fill_map (const char* const g_str, const char* const en_str){

	const char* g_buf = g_str;
	const char* en_buf = en_str;

	while ((*g_buf)&&(*en_buf))
	{
		if (' ' != (*g_buf) || ' ' != (*en_buf))
			g_map [(*g_buf) - 'a'] = (*en_buf) - 'a';
	
		g_buf++;
		en_buf++;
	}
}

void fill_missing ()
{
	const int check_sum = 325; // sum of integers from 0 to 25
	int sum = 0;
	char key = -1;
	for ( size_t i = 0; i < g_map.size(); i++ )
	{
		if ( -1 == g_map[i] )
		{
			assert (-1==key);
			key = i;
			continue;
		}
		sum += g_map[i];
	}

	char val = check_sum - sum;
	assert(val<26);

	g_map[key]=val;
}

int _tmain(int argc, _TCHAR* argv[])
{
	fill_map ("y qee","a zoo");
	fill_map ("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand");
	fill_map ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities");
	fill_map ("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up");
	fill_missing ();
	//translate ("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	//translate ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	//translate ("de kr kd eoya kw aej tysr re ujdr lkgc jv");

	string line;
	ifstream myfile ("c:\\temp\\g\\QR\\A-small-attempt5.in");

	if (myfile.is_open())
	{
		if ( !myfile.good() )
			throw "Invalid input format";

		int N = 0; // the number of cases
		getline (myfile,line);
		N = atoi ( line.data() );
		for ( int n_case = 0; n_case < N; n_case++ )
		{
			getline (myfile,line);
			cout << "Case #" << n_case+1 << ": ";
			translate ( (char*)line.data() );
		}
	}

	getchar();
	return 0;
}

