#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
using namespace std;


void magic(int p, int c, char *cDD, int d, char *dDD, int n, char *nD);

int main(int argc, char *argv[]) {
	ifstream in;
	if ( argc >=1 )
		in.open(argv[1]);
	else
		in.open("B-small.in");

	if (!in) {
		cout << "file open failed";
		exit(1);
	}
	
	int problems = 0;

	in >> problems;

	int c;
	char cD[40][3];
	char cDD[200000];
	int d;
	char dD[30][2];
	char dDD[200000];
	int n;
	char nD[110];
	int j, ii, jj;

	for ( int i = 1; i <= problems; i++ ) {
		for ( long int jjj = 0; jjj < 200000; jjj++ ) {
			cDD[jjj] = 0;
			dDD[jjj] = 0;
		}
		in >> c;
		for ( j = 1; j <= c; j++ ) {
			in >> cD[j];
			cDD[int(cD[j][0])*1000+int(cD[j][1])] = cD[j][2];
			cDD[int(cD[j][1])*1000+int(cD[j][0])] = cD[j][2];
		}
		in >> d;
		for ( j = 1; j <= d; j++ ) {
			in >> dD[j];
			dDD[int(dD[j][0])*1000+int(dD[j][1])] = 1;
			dDD[int(dD[j][1])*1000+int(dD[j][0])] = 1;
		}
		in >> n;
		in >> nD;
		magic(i,c,cDD,d,dDD,n,nD);
	}
}

void magic(int p, int c, char *cDD, int d, char *dDD, int n, char *nD) {
	char l[500] = { 0 };
	l[0] = ' ';
	int ll = 0;
	long int s, ss;

	//cout << n << " " << *nD << endl;

	for ( int i = 0; i < n; i++ ) {
		if ( ll > 0 ) {
			s = int(l[ll])*1000+int(nD[i]);
			ss = int(l[ll])+int(nD[i])*1000;
			if ( cDD[s] != 0 ) {
				l[ll] = cDD[s];
			} else if ( cDD[ss] != 0 ) {
				l[ll] = cDD[ss];
			} else {
				for ( int j = 1; j <= ll; j++ ) {
					s = int(l[j])*1000+int(nD[i]);
					ss = int(l[j])+int(nD[i])*1000;
					if ( dDD[s] == 1 || dDD[ss] == 1 ) {
						ll = 0;
					}
				}
				if ( ll != 0 ) {
				ll++;
				l[ll] = nD[i];
				}
			}
		} else {
			ll++;
			l[ll] = nD[i];
		}
	}
	cout << "Case #" << p << ": [";
	for ( int i = 1; i < ll; i++ )
		cout << l[i] << ", ";
	if ( ll > 0 )
		cout << l[ll];
	cout << "]" << endl;
}
