#include <iostream>
#include <string>
#include <set>
#include <map>
using namespace std;

void add(char [], int adder, int& );
void multiply(char [], int prod, int&);
void reverse( char [], int );

int main() {
    int T;
    cin >> T;
    for( int casei = 0; casei < T; casei++ ) {
	string symbols;
	cin >> symbols;
	set<char> digits;
	for( int i = 0; i < symbols.size(); i++ ) {
	    digits.insert( symbols[i] );
	}
	//cout << digits.size() << endl;
	int base = digits.size();
	if ( base == 1 ) base = 2;
	map<char, int> digimap;
	int current = 0;
	long sum = 0;
	char cum[500];
	int length = 0;
	if( symbols.size() == 1 ) {
	    cum[0] = '1';
	    cum[1] = 0;
	} else {
	for ( int i = 0; i < symbols.size(); i++ ) {
	    if ( i == 0 ) {
		digimap[ symbols[0] ] = 2;
		current++;
	    } else {
		if ( digimap[ symbols[i] ] == 0 ) {
		    if ( current == 1 ) {
			digimap[ symbols[i] ] = 1;
			current++;
		    } else {
			digimap[ symbols[i] ] = current + 1;
			current++;
		    }
		}
	    }
	    multiply(cum, base, length);
	    add(cum, digimap[ symbols[i] ] - 1, length);
	    //sum = sum * base + digimap[ symbols[i] ] - 1;
	}
	cum[length] = 0;
	reverse(cum, length);
//	cout << cum << endl;
	}
	cout << "Case #" << casei+1 << ": " << cum << endl;

    }
    return 0;
}

void add(char sum[], int adder, int &length) {
    for ( int i = 0; ; i++ ) {
	if ( adder == 0 ) break;
	if ( i >= length ) {
	    sum[i] = '0';
	    length++;
	}
	int buf = adder + sum[i] - '0';
	sum[i] = buf % 10 + '0';
	int carrier = buf / 10;
	adder = carrier;
    }
}

void multiply(char sum[], int prod, int &length) {
    int origlen = length;
    int carrier = 0;
    for ( int i = 0; i < length ; i++ ) {
	int buf = prod * ( sum[i] - '0' ) + carrier;
	sum[i] = buf % 10 + '0';
	carrier = buf / 10;
    }
    for ( int i = length; ; i++ ) {
	if ( carrier == 0 ) break;
	if ( i >= length ) {
	    sum[i] = '0';
	    length++;
	}
	sum[i] = carrier % 10 + '0';
	carrier = carrier / 10;
    }
}

void reverse(char sum[], int length ) {
    char temp[length+1];
    for ( int i = 0; i < length; i++ ) {
	temp[i] = sum[i];
    }
    for ( int i = 0; i < length; i++ ) {
	sum[i] = temp[length - 1 - i];
    }
}
