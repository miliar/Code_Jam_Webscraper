#pragma once

#define _CRT_SECURE_NO_DEPRECATE
#include "targetver.h"

#include <windows.h>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <tchar.h>
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

FILE * in, * out;

#define fo(a,b,c) for(int a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

int ri() { int a; fscanf(in, "%d", &a ); return a; }
double rf() { double a; fscanf(in, "%lf", &a ); return a; }
char sbuf[100005]; 
string rstr() 
{
	//fscanf(in, "%lf", sbuf); 
	char c;
	char * b = sbuf;
	while(c = fgetc(in))
	{
		if(c == '\n' || c == 255) break;
		*b++=c;
	}
	*b = 0;
	return sbuf; 
}
long long rll() { long long a; fscanf(in, "%lld", &a ); return a; }

int getSym()
{
	fi(5)
	{
		char c = fgetc(in);
		if(c == '.') return 0;
		if(c == 'O') return 1;
		if(c == 'X') return 2;
		if(c == 'T') return 3;
	}
	return 0;
}
int pole[16];
bool isWiner(int w)
{
	fi(4)
	{
		bool v = true;
		bool h = true;
		fj(4)
		{
			v = v && (pole[i+j*4] == 3 || pole[i+j*4] == w);
			h = h && (pole[i*4+j] == 3 || pole[i*4+j] == w);
		}
		if(v || h) 
			return true;
	}
	bool v = true;
	bool h = true;
	fj(4)
	{
		v = v && (pole[j+j*4] == 3 || pole[j+j*4] == w);
		h = h && (pole[3+j*4-j] == 3 || pole[3+j*4-j] == w);
	}
	return (v || h);
}

string getWinner()
{
	if(isWiner(1)) return "O won";
	if(isWiner(2)) return "X won";
	fi(16) if(pole[i] == 0) return "Game has not completed";
	return "Draw";
}


long _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("A-large.in","rt");
	out	= fopen("large_out.txt","wt");
	
	int T = ri(); 
	for(int i = 0; i<T; i++)
	{
		fj(16) pole[j] = getSym();
		string result = getWinner();

		fprintf(out, "Case #%d: %s\n",i+1, result.c_str());
		printf("Case #%d: %s\n",i+1, result.c_str());
	}

	fclose(in);
	fclose(out);
	return 0;
}

