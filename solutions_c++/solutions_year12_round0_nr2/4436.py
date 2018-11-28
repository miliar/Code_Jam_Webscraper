#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int s;

int count(int m, int p) {
	// if zero
	if (p == 0) {
		return 1;
	}
	// if one
	if (p==1) {
		if (m >= 1) return 1;
		else return 0;
	}
	
	//else 
	if (m >= (3*p-2)) return 1;

	if ((m >= (3*p-4)) && s > 0) {
		s--;
		return 1;
	}
	
	return 0;
}

int main() {
	int x;
	
	ifstream in("a.in");
	ofstream out("a.out");

	
	in >> x;

	for (int i=0; i<x; i++) {
		int n, p;
		in >> n >> s >> p;

		int ammount = 0;

		for (int j=0; j<n; j++) {
			int m;
			in >> m;
			ammount+= count(m, p);
		}
		out << "Case #" << i+1 << ": " << ammount << endl;
	}
}