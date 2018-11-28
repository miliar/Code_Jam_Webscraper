#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
using namespace std;


void bot(int p, int c, char *b, int *n);

int main(int argc, char *argv[]) {
	ifstream in;
	if ( argc >=1 )
		in.open(argv[1]);
	else
		in.open("A-small.in");

	if (!in) {
		cout << "file open failed";
		exit(1);
	}
	
	int problems = 0;

	in >> problems;

	char b[101];
	int n[101];
	int c;

	for ( int i = 1; i <= problems; i++ ) {
		in >> c;
		for ( int j = 1; j <= c; j++ ) {
			in >> b[j];
			in >> n[j];
		}
		bot(i,c,b,n);
	}
}

int botnext(char bs, int i, int c, char *b, int *n) {
	for ( i; i <= c; i++ ) {
		if ( bs == b[i] )
			return i;
	}
	return -1;
}

void bot(int p, int c, char *b, int *n) {
	int steps = 0;

	int pos_b = 1;
	int pos_o = 1;

	int next_b = 0;
	int next_o = 0;
	char cur = 'x';
	int i = 1;

	while ( next_b != -1 || next_o != -1 ) {
		if ( next_b == 0 )
			next_b = botnext('B',i,c,b,n);
		if ( next_o == 0 )
			next_o = botnext('O',i,c,b,n);

		if ( next_b > 0 && ! ( next_o > 0 ) )
			cur = 'B';
		else if ( next_o > 0 && ! ( next_b > 0 ) )
			cur = 'O';
		else if ( next_b > 0 && next_o > 0 ) {
			if ( next_b < next_o ) cur = 'B'; else cur = 'O';
		}

		if ( next_b > 0 || next_o > 0 )
			steps++;
		//cout << "b " << next_b << " " << pos_b << " " << n[next_b] << endl;
		//cout << "o " << next_o << " " << pos_o << " " << n[next_o] << endl;
		if ( next_b > 0 ) {
			if ( pos_b > n[next_b] )
				pos_b--;
			else if ( pos_b < n[next_b] )
				pos_b++;
			else if ( cur == 'B' ) {
				next_b = 0;
				i++;
			}
		}
		if ( next_o > 0 ) {
			if ( pos_o > n[next_o] )
				pos_o--;
			else if ( pos_o < n[next_o] )
				pos_o++;
			else if ( cur == 'O' ) {
				next_o = 0;
				i++;
			}
		}
	}

	cout << "Case #" << p << ": " << steps << endl;
}
