//============================================================================
// Name        : GCJ200802.cpp
// Author      : liudapeng
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <climits>
using namespace std;

typedef long long  llong;

llong a[1024];
llong b[1024];


inline llong compute(int c) {
	llong t = 0;
	for (int i = 0; i < c; ++i) {
		t += (a[i]*b[i]); 
	}
	
	return t;
}

int main() {
	ifstream in("e:\\is.txt");
	ofstream out("e:\\os.txt");
//	std::greater();
	
	int t, v;
	in >> t;
//	cout << "t:" << t << endl;
	for (int i = 0; i < t; ++i) {
		in >> v;
//		cout << "v:" << v << endl;
		for (int j = 0; j < v; ++j) {
			in >> a[j];
//			cout << a[j] << " ";
		} 
//		cout << endl;
		for (int j = 0; j < v; ++j) {
			in >> b[j];
//			cout << b[j] << " ";
		}
//		cout << endl;
		llong value = INT_MAX;
//		int c = jiecheng(v);
//		for (int p = 0; p < c; ++p) {
//			std::next_permutation(&a[0], &a[v]);
//			for (int q = 0; q < c; ++q) {
//				std::next_permutation(&b[0], &b[v]);
//				int x = compute(v);
//				if(x < value)
//					value = x;
//			}
//		}
		std::sort(&a[0], &a[v], greater<int>());
		std::sort(&b[0], &b[v], less<int>());
//		for (int p = 0; p < v; ++p) {
//			cout << a[p] << " ";
//		}
//		cout << endl;
//		for (int p = 0; p < v; ++p) {
//			cout << b[p] << " ";
//		}
//		cout << endl;
		value = compute(v);
		cout << "Case #" << i + 1 << ": " << value << endl;
		out << "Case #" << i + 1 << ": " << value << endl;
	}
	
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
