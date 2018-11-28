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
using namespace std;

char t[]="welcome to code jam";

unsigned long int wii[19*1000];

char a[1000]="welwelwelcome to code jam";
int l = strlen(a);

void fill() {
    int k=0;
    for( int i=0; i<l; i++ ) {
	char c = a[i];
	if( c == t[0] ) {
	    k=(k+1)%10000;
	}

	wii[i] = k;
    }
    k=0;
    for( int j=1; j<19; j++ ) {
	wii[j*1000] = 0;
	unsigned long int taika3=0;
	for( int i=1; i<l; i++ ) {
	    char c = a[i];
	    unsigned long int puu = wii[i+(j-1)*1000];
	    if( c == t[j] ) {
		taika3 = (taika3+puu)%10000;
	    }
	    wii[i+j*1000] = (taika3);
	}
    }
}


int main() {

    std::ifstream ifs( "c-small2.in" );
    int casecount;
    ifs >> casecount >> ws;

    for( int i=0; i<casecount; i++ ) {
	std::string line;
	getline( ifs, line );
	strcpy( a, line.c_str() );
	l = strlen(a);
	fill();

	/*cout << l << "\n";
	for( int j=0; j<19; j++ ) {
	    for( int i=0; i<l; i++ ) {
		cout << "\t" << wii[i+j*1000];
	    }
	    cout << "\n";
	}*/

	unsigned long int v = wii[18*1000+l-1];//%10000;
	cout << "Case #" << (i+1) << ": " << (v<1000?"0":"") << (v<100?"0":"") << (v<10?"0":"") << v << "\n";
    }

}
