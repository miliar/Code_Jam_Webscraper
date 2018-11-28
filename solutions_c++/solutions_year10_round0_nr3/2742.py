//============================================================================
// Name        : coaster.cpp
// Author      : goktan
// Version     :
// Copyright   : 
// Description : Hello World in C, Ansi-style
//============================================================================


#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

int main_loop(fstream &in) {
	queue <unsigned long int> q;
	unsigned long int r, k, n;
	in >> r >> k >> n;
	cout <<"k: "<< k <<" n: " << n << endl;
	for(unsigned long int i = 0; i < n; ++i) {
		unsigned long int tmp;
		in>>tmp;
		q.push(tmp);
		cout << tmp << endl;
	}
	unsigned long int roundg = q.size();
	unsigned long int m = 0;
	unsigned long int t = 0;
	for (unsigned long int i=0; i < r ;++i) {
		while(1) {
			unsigned long int a = q.front();
			if( (t+a) > k || roundg == 0) break;
			t = t+a;
			q.pop();
			q.push(a);
			roundg --;
		}
		m += t;
		t = 0;
		roundg = q.size();
	}
	return m;
}

int main(void) {
	fstream in("input", ios::in);
	fstream out("output", ios::out | ios::trunc);
	if(!in.is_open() || !out.is_open()) {
		cerr << "unable to open files"<< endl;
		return -1;
	}
	int testcase = 0;
	in>>testcase;
	for(int j = 0; j < testcase; ++j) {
			int count = main_loop(in);
			cout << "Case #" << j+1 << ": " << count << endl; //<< count?"On":"OFF" << endl;
			out << "Case #" << j+1 << ": " << count << endl;
	}
	in.close();
	out.close();
	return 0;
}
