// GoogleCodeJam_2013_First.cpp : Defines the entry point for the console application.
//
//#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

#include <iomanip>

using namespace std;

enum STATUS{ XWIN = 0, OWIN, DRAW, NOTYET };

char CheckStatus( char a, char b)
{
	char ret;

	ret = b;

	switch (a )
	{
		case 'X' : if ( b == 0 ) ret = 'X'; 
					if ( b == 'O' ) ret = NOTYET;
					break;
		case 'O' : if ( b == 0 ) ret = 'O'; 
					if ( b == 'X' ) ret = NOTYET;
					break;
		case '.' : ret = NOTYET;
					break;
		case 'T' : break;
	}

	return ret;
}


int CheckMap( char * Map )
{
	int i,j;

	char Player;

	// row
	for ( i=0; i<4; i++)
	{
		Player = 0;

		for ( j=0; j<4; j++)
		{
			Player = CheckStatus( Map[i*4+j], Player );			
		}

		if ( Player == 'X' ) return XWIN;
		if ( Player == 'O' ) return OWIN;
	}
	

	// column

	for ( i=0; i<4; i++)
	{
		Player = 0;

		for ( j=0; j<4; j++)
		{
			Player = CheckStatus( Map[j*4+i], Player );			
		}

		if ( Player == 'X' ) return XWIN;
		if ( Player == 'O' ) return OWIN;
	}
	

	// diagonal

	Player = 0;

	for ( j=0; j<4; j++)
	{
		Player = CheckStatus( Map[j*4+j], Player );	

	}

	if ( Player == 'X' ) return XWIN;
	if ( Player == 'O' ) return OWIN;

		Player = 0;

	/*
    0 1 2 3
	4 5 6 7
	8 9 10 11
	12 13 14 15

	3,6,9,12
	*/

	for ( j=0; j<4; j++)
	{
		Player = CheckStatus( Map[3*(j+1)], Player );	

	}

	if ( Player == 'X' ) return XWIN;
	if ( Player == 'O' ) return OWIN;


	for ( i=0;i<16;i++)
		if ( Map[i] == '.' ) return NOTYET;

	return DRAW;
}

int main(int argc, char* argv[])
{
	int iPro, i,j,k;

	char Map[4*4];

	ifstream in;

	
	//in.open("A-small-attempt4.in");
	in.open("A-large.in");

	ofstream out;

	out.open("output_0l.text");

	in >> iPro;

	for ( int k=1;k<=iPro;k++)
	{
		for ( i=0;i<16;i++)
			in >> Map[i];

		out << "Case #" << k << ": " ;

		switch ( CheckMap(Map) )
		{
			case XWIN : out << "X won" << endl; break;
			case OWIN : out << "O won" << endl; break;
			case DRAW : out << "Draw" << endl; break;
			case NOTYET : out << "Game has not completed" << endl; break;
			default: break;
		}
	}	

	return 0;
}

