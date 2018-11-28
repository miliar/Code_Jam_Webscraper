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
#include <cmath>
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

int main() {


    //std::ifstream ifs( "in.in" );
    //std::ifstream ifs( "A-small-attempt1 (1).in" );
    //std::ifstream ifs( "test.txt" );
    std::ifstream ifs( "A-large (2).in" );
    std::ofstream out( "output.txt");
    int casecount;
    ifs >> casecount >> ws;


    for( int casenum=1; casenum<=casecount; casenum++ ) {
	long snapper_count, snap_count;
	bool on;
	ifs >> snapper_count >> snap_count;
	long first_on = pow(2,snapper_count)-1;
	long cycle = pow(2,snapper_count);
	snap_count -= cycle*(snap_count/cycle);
	on = snap_count == first_on;


	out << "Case #" << casenum << ": " << (on?"ON":"OFF") << "\n";
    }

}
