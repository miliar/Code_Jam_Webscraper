/*
 *  
 */

#include <iostream>
#include "snapper.h"
#include <fstream>
#include <vector>
using namespace std;

int main() {

	ifstream in;
	in.open("test.txt");
	ofstream out;
	out.open("output.txt");
	int t;
	in >> t;
	for (int i = 0; i < t; ++i) {
		int n, k;
		in >> n;
		in >> k;
		Snapper* list;
		list = new Snapper[n];
		list->power = 1;
		for (int j = 0; j < k; ++j) {
			for (int x = 0; x < n; ++x) {
				list[x].snap();
			}
			for (int x = 0; x < n-1; ++x) {
				if (list[x].power && list[x].status)
					list[x+1].power = 1;
				else
					list[x+1].power = 0;
			}
		}
		out << "Case #" << i+1 << ": ";
		if (list[n-1].power && list[n-1].status)
			out << "ON\n";
		else
			out << "OFF\n";
		delete list;
	}
	in.close();
	out.close();
	return 0;
} 

