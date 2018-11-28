/*
ID: zinking1
PROG: Snapper chain
LANG: C++
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef  long long int64;
typedef  vector<int64> VI;




struct Block{
	int64 capacity;
	VI sequence;

	bool equal( Block& rhs ){
		if( this->sequence.size() != rhs.sequence.size() ) return false;
		for( int i=0; i<this->sequence.size(); i++ )
			if( sequence[i] != rhs.sequence[i] ) return false;
		return true;
	}
};

typedef vector<Block> VB;

int findBlock(  VB& vb, Block& b ){
	for( int i=0; i<vb.size(); i++ ){
		if ( vb[i].equal(b) ) return i;
	}
	return -1;
}

int64 calcRevenue( VI group, int64 C, int64 R ){
	VB seq;
	int i=0;
	int index = 0;
	int GN = group.size();
	int pidnex = -1;
	int counter = 0;
	do{
		int64 cw = 0;
		Block b;
		while( cw + group[index] <= C && ( GN - b.sequence.size() ) > 0 ){
			cw += group[index];
			b.sequence.push_back( group[index] );
			index = (index+1)%GN;
			counter ++ ;
		}
		b.capacity = cw;
		pidnex = findBlock( seq, b );
		if( pidnex == -1  || counter <= GN){
			seq.push_back( Block(b) );
		}
		else{
			break;
		}
	}while( true );

	int64 hsize = pidnex;
	int64 psize = seq.size() - pidnex;

	int64 hsum = 0, psum = 0;
	//hsum = accumulate( seq.begin(), seq.begin() + hsize, hsum );
	//psum = accumulate( seq.begin()+hsize, seq.end(), psum );
	for( i=0; i<hsize; i++ ) hsum += seq[i].capacity;
	for( i=hsize; i<seq.size(); i++ ) psum += seq[i].capacity;

	int64 sum = 0;
	if( R<=hsize ){
		for(  i=0; i<R; i++ ) sum += seq[i].capacity;
		//return sum;
	}
	else{
		int64 rpsize = (R-hsize)/psize;
		int64 rpmod = ( R-hsize) % psize;
		sum += hsum;
		sum += rpsize * psum;
		for(  i=0; i<rpmod; i++ ) sum+=seq[hsize+i].capacity;
		//return sum
	}

	return sum;
}

int64 calcRevenueV( VI group, int64 C, int64 R ){
	int i=0,j=0;
	int64 sum = 0;
	int index = 0;
	int GN = group.size();
	while ( i<R ){
		int cw = 0;
		int n = 0;//on roller;
		while( cw + group[index] <= C && (GN - n ) > 0 ){
			cw += group[index];
			index = (index + 1)%GN;
			n++;
		}
		sum += cw;
		i++;
	}
	return sum;
}

int main(){
	ifstream ifile("C-small-attempt2.in");
	ofstream ofile("C-small-attempt2.out");

	int64 T=0;
	ifile >> T;
	int64 i = 0;
	while( i < T ){
		int64 R,K,N;
		VI g;
		ifile >> R >> K >> N;
		int64 gi;
		for( int64 j=0; j<N; j++ ){
			ifile >> gi;
			g.push_back( gi );
		}
		ofile <<"Case #" << i+1 << ": "<< calcRevenueV( g,K,R) << endl;
		i++; 
	}

	return 0;

}
