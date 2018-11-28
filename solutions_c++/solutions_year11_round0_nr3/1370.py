//============================================================================
// Name        : GCJ3.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <cstring>
#include <cassert>
#include <map>
#include <iomanip>
#include <string>
#include <vector>
#include <sstream>
using namespace std;



template< typename T, int max_size >
class queue {
public:
    T arr[max_size];
    int first, last;
    queue()
	:first(0), last(0) {

    }
    void push( const T& arg ) {
	if( first%max_size == last%max_size && last > first )
	    throw;
	arr[last%max_size] = arg;
	last++;
    }
    T& top() {
	return arr[first%max_size];
    }
    T& pop() {
	if( first == last )
	    throw;
	return arr[(first++)%max_size];
    }
    bool empty() {
	return first == last;
    }
};

long R, k, N;
long g[1000];
unsigned long long money;

long long buf1[1000];
long long buf2[1000];
long long buf3[1000];
bool buf[1000];

bool buf_[1000];
long bufk_[1000];


void calcMoney() {
    long j=R;
    long k_=k;
    int i=0;
    int h=0;

    for( int i=0;i<1000; i++ ) {
	buf[i] = false;
    }
    buf2[0] = money;
    buf3[0] = j;
    buf[0] = true;



    while(true) {
	if( ( g[i%N] <= k_ ) && ( h==i || h%N != i%N ) ) {
	    k_ -= g[i%N];
	    money += g[i%N];

	    i++;
	}
	else {
	    h=i;
	    k_=k;
	    j--;
	    if( j==0 ) {
		return;
	    }
	    if( buf[i%N] ) {
		long roundmoney = money - buf2[i%N];
		long roundtrips = buf3[i%N] - j;
		int rounds = j/roundtrips;
		j -= rounds*roundtrips;
		money += rounds*roundmoney;
	    }
	    if( j==0 ) {
		return;
	    }
	    buf[i%N] = true;
	    buf2[i%N] = money;
	    buf3[i%N] = j;
	}
    }
}

int main() {


    //std::ifstream ifs( "in.in" );
    std::ifstream ifs( "C-large.in" );
    //std::ifstream ifs( "C-large (1).in" );
    //std::ifstream ifs( "A-small-attempt1 (1).in" );
    std::ofstream out( "output.txt");
    long casecount;
    ifs >> casecount >> ws;


    for( long casenum=1; casenum<=casecount; casenum++ ) {
	int candycount;
	ifs >> candycount;

	int bitcount[32];
	for( int i=0; i<32; i++ ) {
	    bitcount[i] = 0;
	}

	long smallest_candy = 10000000;

	for( int candynum=0; candynum<candycount; candynum++ ) {
	    long candy;
	    ifs >> candy;

	    if( smallest_candy > candy )
		smallest_candy = candy;

	    for( int i=0; i<32; i++ ) {
		if( candy&1 )
		    bitcount[i]++;
		candy >>= 1;
	    }
	}

	bool failure=false;
	long win=0;
	for( int i=0; i<32; i++ ) {

	    //cout << i << " " << bitcount[i] << "\n";
	    if( bitcount[i] % 2 == 1 )
		failure=true;
	    if( bitcount[i] != 0 )
		win += (bitcount[i])*(1<<i);
	}

	for( int i=0; i<32; i++ ) {
	    if( ( smallest_candy >> i ) & 1 )
		win -= (1<<i);
	}


	if( failure )
	out << "Case #" << casenum << ": NO\n";
	else
	out << "Case #" << casenum << ": " << win << "\n";
    }

}
