/*
 * Author ahfyth
*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

typedef struct robot
{
	char color;
	unsigned int pos;
}robot;

inline unsigned int fabs( int a )
{
	return (a >= 0) ? a : -a ;
}

int getNext( vector<robot> &r, vector<robot>::iterator itrb, char color )
{
	vector<robot> :: iterator it = itrb;
	for( ; it!=r.end(); ++it )
	{
		if( it->color == color )return it->pos;
	}
	return -1;
}

unsigned int solve( vector<robot> &r )
{
//	cerr << "Solve\n";
	unsigned int currb, curro;	// current blue / orange
	currb = 1;
	curro = 1;
	unsigned int count = 0;
	vector<robot> :: iterator it;
	int mov, next;
	for( it=r.begin(); it!=r.end(); ++it )
	{
//		cerr << "Count : " << count << ", B:" << currb << ", O:" << curro << endl;
		if( it->color == 'O' )
		{
			mov = fabs(it->pos - curro) + 1;
			count += mov;
			curro = it->pos;
			next = getNext( r, it,'B' );
			if( next != -1 )
			{
				if( next > currb )
				{
					currb += mov;
					if( currb > next )currb = next;
				}
				else if( next < currb )
				{
					currb -= mov;
					if( currb < next )currb = next;
				}
			}
		}
		else
		{
			mov = fabs(it->pos - currb) + 1;
			count += mov;
			currb = it->pos;
			next = getNext( r, it, 'O' );
			if( next != -1 )
			{
				if( next > curro )
				{
					curro += mov;
					if( curro > next )curro = next;
				}
				else if( next < curro )
				{
					curro -= mov;
					if( curro < next )curro = next;
				}
			}
		}
	}
	return count;
}


int main( int argc, char *argv[] )
{
	if( argc < 2 )
	{
		cerr << "Usage : " << argv[0] << " <file>\n";
		cerr << "This program is designed to \n";
		exit( 1 );
	}
	ifstream fin;
	fin.open( argv[1], ios::in );
	if( fin.fail() )
	{
		cerr << "Error : open file failed!\n";
		return 2;
	}
	unsigned int TOTAL;
	fin >> TOTAL;
//	cerr << "Total : " << TOTAL << endl;

	unsigned int i, j;
	unsigned int N;
	char type;
	unsigned int pos;
	vector<robot> r;
	robot rb;
	for( i=1; i<=TOTAL; ++i )
	{
		fin >> N;
//		cerr << "N : " << N << endl;
		r.clear();
		for( j=0; j<N; ++j )
		{
			fin >> rb.color;
			fin >> rb.pos;

			r.push_back( rb );
		}
		/*
		for( j=0; i<orange.size(); ++j )
			cerr << orange[j] << ",";
		cerr << "\n";
		*/
		j = solve( r );
		cout << "Case #" << i << ": " << j << endl;
	}

	fin.close();

	return 0;
}



