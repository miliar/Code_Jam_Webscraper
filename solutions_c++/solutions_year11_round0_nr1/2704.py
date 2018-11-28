// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

int a[1000], t[1000], n;
string s;

void read(){
	char c; int i;
	cin >> n;
	for (i=0; i<n; i++){
		c = ' ';
		while (c == ' ') cin >> c;
		cin >> a[i];
		if (c == 'O') t[i] = 1; else t[i] = 2;
	}
	getline (cin, s);
}

int main(){
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int nn, ii, cur1 = 1, cur2 = 1, i, t1, t2;
	cin >> nn;
	getline (cin, s);
	for (ii=0; ii<nn; ii++){
		read();
		cur1 = 1; cur2 = 1; t1 = 0; t2 = 0;
		int res = 0, g;
		for (i=0; i<n; i++)
			if (t[i] == 1){
				res = max (res, t1 + abs(a[i] - cur1)) + 1;
				t1 = res; cur1 = a[i];
			} else {
				res = max (res, t2 + abs(a[i] - cur2)) + 1;
				t2 = res; cur2 = a[i];
			}
		cout << "Case #" << ii+1 << ": " << res << endl;
	}
}