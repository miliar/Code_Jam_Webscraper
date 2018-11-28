//============================================================================
// Name        : snapper.cpp
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
using namespace std;

bool main_loop(fstream &in) {
	double n, k;
	in >> n >> k;
	//cout << "n: " << n << " k: "<< k << endl;
	int pown = (int) pow(2,n);
	//if((k % pown) == (pown - 1)) {
	if(fmod(k,pown) == (pown - 1)) {
		return true;
	} else
		return false;
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
			bool count = main_loop(in);
			string tmp = count?"ON":"OFF";
			cout << "Case #" << j+1 << ": " << tmp << endl; //<< count?"On":"OFF" << endl;
			out << "Case #" << j+1 << ": " << tmp << endl;
	}
	in.close();
	out.close();
	return 0;
}
