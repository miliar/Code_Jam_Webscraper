/*
 *  C.cpp
 *  
 *
 *  Created by Sameep Bagadia on 14/04/12.
 *  Copyright 2012 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int shift (int n) {
	stringstream ss;//create a stringstream
	ss << n;//add number to the stream
	string str = ss.str();//return a string with the contents of the stream
	int k;
	int l = str.length();
	for (int i = l-1; i >= 0; i--) {
		if (str[i] != '0') {
			k = i;
			break;
		}
	}
	string out = str.substr(k,l-k) + str.substr(0, k);
	return atoi(out.c_str());
}

int main() {
	
	int n;
	int a ,b;
	cin>>n;
	for (int i = 0; i < n; i++) {
		cin>>a>>b;
		int count = 0;
		for (int n = a; n <= b; n++) {
			
			int m = shift(n);
			while (m != n) {
				//cout << "m:"<<m<<endl;
				if ((m > n) && (m <= b)) {
					count++;
				}
				m = shift(m);
			}
		}
		cout << "Case #"<<(i + 1)<<": "<<count<<endl;
	}
	return 0;
}
