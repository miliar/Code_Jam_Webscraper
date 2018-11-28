/*
 * 1.cpp
 *
 *  Created on: May 8, 2010
 *      Author: Justin Li
 */
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <bitset>
#include <queue>
#include <stack>
#include <fstream>
using namespace std;

int main() {
	ifstream in;
	in.open("A-small.in");
	ofstream out;
	out.open("file.out");
	
	int t, n, k, i, j, casen=0;
	in >> t;

	for (i=0; i<t; i++) {
		casen++;
		out << "Case #" << casen << ": ";
		in >> n >> k;
		j = (int)pow(2, (double)n) - 1;
		while (k>j) k-=j+1;
		if (k==j) out << "ON" << endl;
		else out << "OFF" << endl;
	}

	in.close();
	out.close();
	return 0;
}
