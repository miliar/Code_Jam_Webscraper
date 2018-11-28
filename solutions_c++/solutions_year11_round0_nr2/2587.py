// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

int n, c, d, a[1000][4], b[1000][3];
char r[1000], nr;
string s, x;
char q;

void read(){
	cin >> c;
	int i;
	for (i=0; i<c; i++){
		cin >> q;
		a[i][0] = q;
		cin >> q;
		a[i][1] = q;
		cin >> q;
		a[i][2] = q;
	}
	cin >> d;
	for (i=0; i<d; i++){
		cin >> q;
		b[i][0] = q;
		cin >> q;
		b[i][1] = q;
	}
	cin >> n;
	cin >> s;
	getline (cin, x);
}

bool check(){
	int i;
	if (nr == 0) return false;
	for (i=0; i<c; i++)
		if ( (a[i][0] == r[nr] && a[i][1] == r[nr-1]) || (a[i][1] == r[nr] && a[i][0] == r[nr-1]) )
		{ nr--; r[nr] = a[i][2]; return true; }
	return false;
}

void dest(){
	int i, j, k;
	for (i=0; i<nr; i++)
		for (j=0; j<d; j++)
			if ( (b[j][0] == r[nr] && b[j][1] == r[i]) || (b[j][1] == r[nr] && b[j][0] == r[i]) ){
				nr = -1; return;
			}
}

int main(){
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int nn, ii, i;
	cin >> nn;
	for (ii=0; ii<nn; ii++){
		read();
		nr = 0;
		s += ' ';
		r[0] = s[0]; 
		for (i=1; i<=n; i++){
			nr++; r[nr] = s[i];
			check();
			dest();
		}
		cout << "Case #" << ii+1 << ": [";
		if (r[0] == ' ') cout << "]" << endl; else 
		{
			cout << r[0];
			for (i=1; i<nr; i++)
				cout << ", " << r[i];
			cout << "]" << endl;
		}
	}
}