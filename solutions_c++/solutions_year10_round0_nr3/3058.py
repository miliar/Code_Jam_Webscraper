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
long money;

long buf1[1000];
long buf2[1000];
long buf3[1000];
bool buf[1000];

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
	    //cout << "Jeh " << i%N << " " << k_+g[i%N] << " " << k_ << "\n";
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
		//cout << i << " " << i%N << " " << roundmoney << " " << roundtrips << " " << rounds << "\n";
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
    //std::ifstream ifs( "A-small-attempt1 (1).in" );
    std::ifstream ifs( "C-small-attempt0 (2).in" );
    //std::ifstream ifs( "A-small-attempt1 (1).in" );
    std::ofstream out( "output.txt");
    long casecount;
    ifs >> casecount >> ws;


    for( long casenum=1; casenum<=casecount; casenum++ ) {
	ifs >> R >> k >> N;
	for( long i=0; i<N; i++ ) {
	    ifs>>g[i];
	}
	money=0;

	calcMoney();

	out << "Case #" << casenum << ": " << money << "\n";
    }

}
