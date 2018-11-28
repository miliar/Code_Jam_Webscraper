#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <list>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <bitset>

#define ulong unsigned long

using namespace std;

unsigned char combine[ 8 ];
unsigned char opposed[ 8 ];
unsigned char combineMap[ 8 ][ 8 ]; 
unsigned char presentBases[ 8 ]; 
unsigned char toIndex[ 26 ];


void clearCase( void )
{
	memset( opposed , 0, sizeof( opposed ) ); 
	memset( combine , 0, sizeof( combine ) ); 
	memset( presentBases, 0, sizeof( presentBases )); 
	memset( combineMap, 0,  8 * 8 );
} 

void processCase( int nCase, istream &in, ostream &out )
{
	clearCase();
	string s, a, b; 
	unsigned char ca,cb,cc;
	int n;

	getline( in, s );
	stringstream ss( s );
	ss >> n; 

	// save combines
	int i;
	for( i = 0; i < n; ++i ){	
		ss >> a; 
		ca = toIndex[ a[ 0 ] ]; 
		cb = toIndex[ a[ 1 ] ]; 
		combineMap[ ca ][ cb ] = combineMap[ cb ][ ca ] = a[2];
		combine[ ca ] = combine[ ca ] | 1 << cb;
		combine[ cb ] = combine[ cb ] | 1 << ca; 
	}

	// save opposed
	ss >> n; 
	
	for( i = 0; i < n; ++i ){	
		ss >> a; 	
		ca = toIndex[ a[ 0 ] ]; 
		cb = toIndex[ a[ 1 ] ]; 
		opposed[ ca ] = opposed[ ca ] | 1 << cb;
		opposed[ cb ] = opposed[ cb ] | 1 << ca; 
	}

	// process the string 
	ss >> n; 
	ss >> a;
	
	if( n == 1 ){
		out << "Case #" << nCase << ": [" << a[ 0 ] << "]" << endl; 
	}else{
		unsigned int prevIdx = toIndex[ a[ 0 ] ];
		unsigned int prevMask = 1 << prevIdx;
		unsigned int mask = 0; 
		unsigned int curIdx; 
		vector< unsigned char > outv; 

		outv.push_back( a[ 0 ] );
		
		for( i = 1; i < n; ++i ){
			curIdx = toIndex[ a[ i ] ];
			if( prevMask != 0 && combineMap[ prevIdx ][ curIdx ] != 0 ){
				// if the previous one is a base and has a combination
				unsigned ch = combineMap[ prevIdx ][ curIdx ];
				outv[ outv.size() - 1 ] = ch; 
				prevIdx = 0xff;
				prevMask = 0; 
			}else{
				if( (opposed[ curIdx ] & (mask | prevMask) ) != 0 ){
					// if the new one makes cancel the current string
					outv.clear(); 
					prevMask = mask = 0; 
					prevIdx = 0xff; 
				}else{
					outv.push_back( a[i] ); 
					mask = mask | prevMask;
					prevIdx = curIdx;
					prevMask = 1 << prevIdx; 
				}
			}
		}

		// output the result
		
		out << "Case #" << nCase << ": [";
		int len = outv.size(); 
		if( len > 0 ){
			out << outv[0];
			for( i = 1; i < len; ++i ){
				out << ", " << outv[i];
			}
		}
		out << "]" << endl; 
	}
}

void main_B( istream &in, ostream &out )
{
	int numCases, i;
	in >> numCases; 
	string s; 
	getline( in, s );

	memset( toIndex, 0xff, sizeof( toIndex ) );
	toIndex[ 'F' ] = 0;
	toIndex[ 'D' ] = 1;
	toIndex[ 'S' ] = 2;
	toIndex[ 'A' ] = 3;
	toIndex[ 'R' ] = 4;
	toIndex[ 'E' ] = 5;
	toIndex[ 'W' ] = 6;
	toIndex[ 'Q' ] = 7;

	for( i = 0; i < numCases; ++i )
	{
		processCase( i + 1, in, out ); 
	}
	return;
}

