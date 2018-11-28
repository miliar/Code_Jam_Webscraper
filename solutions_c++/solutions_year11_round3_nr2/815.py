#include <iostream>
#include <string>
#include <map>
#include <set>
#include <list>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <bitset>
#include <vector>

#define ulong unsigned long
/*
#define INFILE "B-test.in"
#define OUTFILE "B-test.out"


#define INFILE "B-small.in"
#define OUTFILE "B-small.out"
*/
#define INFILE "B-large.in" 
#define OUTFILE "B-large.out"


using namespace std; 

string dummyString;
#define FCR getline( in , dummyString )
#define FULLCHARMASK 0x3FFFFFF 

unsigned long long circd[ 1000 ];

void processCase( istream &in, ostream &out, int nC )
{
	unsigned long long L, t, N, C, ii, xx, tB, accumT;
	in >> L; 
	in >> t; 
	in >> N;
	in >> C; 

	for( ii = 0; ii < C; ++ii ){
		in >> xx; 
		circd[ ii ] = xx << 1; 
	}

	tB = 0; 
	accumT = 0;
	multiset< unsigned long long > boostableD; 
	unsigned long long totalBoostable = 0; 
	for( ii = 0; ii < N; ++ii )
	{
		tB += circd[ ii % C ];  
		if( tB >= t )
		{
			if( tB != t ){
				boostableD.insert( tB - t );
				totalBoostable = tB - t; 
				accumT = t; 
			}else{
				accumT = tB;
			}
			++ii;
			break; 
		}
	}
	
	if( ii == N && accumT == 0 )
	{
		out << "Case #" << nC << ": " << tB << endl;
		return; 
	}

	for( ; ii < N; ++ii ){
		totalBoostable += circd[ ii % C ]; 
		boostableD.insert( circd[ ii % C ] );
	}

	multiset< unsigned long long >::reverse_iterator it = boostableD.rbegin(); 
	for( ; L > 0 && it != boostableD.rend(); ++it ){
		--L;
		accumT += ( *it / 2 );
		totalBoostable -= ( *it  );
	}
	accumT += totalBoostable; 

	out << "Case #" << nC << ": " << accumT << endl;  
}

void myMain( istream &in, ostream &out )
{
	int nCases, ii;
	
	in >> nCases;
	FCR;
	for( ii = 0; ii < nCases; ++ii )
	{
		processCase( in, out , ii + 1 ); 
	}	
}

int main( int argc, char* argv[] )
{
	ofstream out; 
	ifstream in; 

	out.open( OUTFILE , ios::out | ios::trunc ); 
	in.open( INFILE );
	myMain( in, out ); 
	in.close();
	out.close();
}
