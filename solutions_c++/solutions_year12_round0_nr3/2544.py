#include <iostream>
#include <map>
#include <set>
#include <fstream>
#include <math.h>
//#include "all.h"
using namespace std;

int recyle(int a, int b) {
	int d = 0;
	int c = a;
	while (c > 0) {
		c = c/10;
		d++;
	}
	cout << d << endl;
	int p[d];
	p[0] = 1;
	for (int i=1; i<d; i++) {
		p[i] = 10*p[i-1];
	}

	c = 0;
	for (int n=a; n<=b; n++){
		set<int> nc;
		for (int i = 1; i<d; i++){
			int m = p[d-i] * (n % p[i]) + n/p[i];

			if (m>n && m <= b) {
				nc.insert(m);
			}
		}
		c += nc.size();
	}
	return c;
}

int main(){
	string file = "in.in";
	freopen(file.c_str(), "r", stdin);
	int t;
	cin >> t;
	ofstream of;
	of.open("out.txt");

	int a, b;
	for (int i=0; i<t;i++) {
		cin >> a >> b;

		of << "Case #"<< i + 1 << ": " << recyle(a, b) << endl;
	}
	of.close();
	return 0;
}
