/*
 * main.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: greenvirag
 */

#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;



unsigned int iTestCase = 0;
unsigned int maxTestCase = 0;

ofstream file;


void print(int result) {
	file << "Case #" << iTestCase << ": " << result << endl;
}

int convertToInt (string s) {
	int r = 0;
	for (unsigned int i = 0; i < s.size(); i++) {
		r = 10 * r + (s.at(i)-'0');
	}
	return r;
}

string convertToString (int i) {
	stringstream ss;
	ss << i;
	string s = ss.str();
	return s;
}

int calculate (int A, int B) {

	if (A == B) {
		return 0;
	}

	if (B <= 10 ) {
		return 0;
	}


	int result = 0;

	string n = "", m = "";
	string sTemp = ""; int iTemp = 0;

	set<pair<int, int> > set;

	for (int i = A; i < B; i++) {
		n = convertToString(i);
		sTemp = n + n;

		for (unsigned int j = 0; j < n.size(); j++) {
			m = sTemp.substr(j, n.size());
			iTemp = convertToInt(m);
			if (i < iTemp && iTemp <= B) {
				pair<int, int> p = make_pair(i, iTemp);
				if (set.find(p) == set.end()) {
					set.insert(p);
				}
			}
		}
	}

	result = set.size();
	return result;
}

void read() {
	cin >> maxTestCase;
	for (unsigned int i = 0; i < maxTestCase; i++) {
		iTestCase++;
		int a = 0, b = 0;
		cin >> a;
		cin >> b;
		print(calculate(a, b));
	}
}


int main () {

	file.open("result.txt");
	read();
	file.close();

	cout << "OK\n";

	return 0;
}


