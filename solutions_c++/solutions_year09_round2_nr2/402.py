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
#include <climits>
#include <algorithm>
using namespace std;

int permute( int* orig, int origcount, int a, int b ) {
    int digits[30];
    for( int i=0; i<origcount; i++ )
	digits[i] = orig[i];

    int t = digits[a];
    digits[a] = digits[b];
    digits[b] = t;

    int ans=0;
    for( int i=origcount-1; i>=0; i-- ) {
	ans *= 10;
	ans += digits[i];
    }

    return ans;

}

int zeropermute( int* orig, int origcount, int p ) {
    int digits[30];
    for( int i=0; i<p; i++ )
	digits[i] = orig[origcount-i-1];
    digits[p] = 0;
    for( int i=p+1; i<=origcount; i++ )
       	digits[i] = orig[origcount-i];

    int ans=0;
    for( int i=origcount; i>=0; i-- ) {
	ans *= 10;
	ans += digits[i];
    }

    return ans;

}

int main() {

    std::ifstream ifs( "input2.in" );

    int casecount;
    ifs >> casecount >> ws;

    for( int i=0; i<casecount; i++ ) {
	unsigned long long n;
	ifs >> ws;

	int digits[30];
	for( int j=0; j<30; j++ )
	    digits[j] = 0;
	int digitcount=0;/*
	int digitcount=0;
	long tn = n;
	for( int j=0; j<30; j++ ) {
	    digits[j] = tn%10;
	    tn /= 10;
	    if( tn == 0 ) {
		digitcount = j+1;
		break;
	    }
	}*/

	for( int j=0; j<30; j++ ) {
	    if( !isdigit(ifs.peek()) )
		break;
	    else {
		for( int k=0; k<29; k++ )
		    digits[29-k] = digits[28-k];
		digits[0] = ifs.peek() - '0';
		digitcount++;
		ifs.get();
	    }
	}


	int kek=0;

	for( int j=1; j<digitcount+1; j++ ) {
	    if( digits[j] < digits[j-1] ) {
		kek=j;
		break;
	    }

	}
	int rmin = INT_MAX;
	int rmin_i = -1;

	for( int j=0; j<kek; j++ ) {
	    if( digits[j] > digits[kek] && digits[j] < rmin ) {
		rmin = digits[j];
		rmin_i = j;
	    }
	}


	int t = digits[kek];
	digits[kek] = digits[rmin_i];
	digits[rmin_i] = t;

	sort( digits, digits+kek );
	reverse( digits, digits+kek );



/*
	unsigned long long ans=1000000000000000;

	for( int j=0; j<digitcount; j++ )
	    for( int k=0; k<digitcount; k++ ) {
		unsigned long long v=permute( digits, digitcount, j, k );
		if( v > n && v < ans )
		    ans = v;
	    }

	for( int j=0; j<digitcount; j++ ) {
	    unsigned long long v = zeropermute( digits, digitcount, j );
	    if( v > n && v < ans )
		ans = v;
	}*/



	/*cout << l << "\n";
	for( int j=0; j<19; j++ ) {
	    for( int i=0; i<l; i++ ) {
		cout << "\t" << wii[i+j*1000];
	    }
	    cout << "\n";
	}*/


	cout << "Case #" << (i+1) << ": ";

	if( digits[digitcount] != 0 )
	    cout << digits[digitcount];
	for( int k=digitcount-1; k>=0; k-- ) {
	    cout << digits[k];
	}

	cout << "\n";
    }

}
