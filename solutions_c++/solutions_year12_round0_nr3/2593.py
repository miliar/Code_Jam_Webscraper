/*
 *  RecycledNumbers.cpp
 *  GoogleCodeJamPractice
 *
 *  Created by Elina Robeva on 4/14/12.
 *  Copyright 2012 Stanford University. All rights reserved.
 *
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <math.h>
using namespace std;


int main() {
	freopen("/Users/erobeva/Downloads/C-large.in","r",stdin);
	freopen("/Users/erobeva/Downloads/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOut.txt", "w", stdout);
	
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		long long A, B;
		cin >> A >> B;
		long long total = 0;
		for(long long n = A; n <= B; ++n) {
			long long n1 = n;
			int len = 0;
			while(n1!=0){
				len++;
				n1 /= 10;
			}
			n1 = n;
			for(int j = 0; ; ++j){
				int m = (n1%10)*pow(10, len-1) + n1/10;
				if(m >= A && m <= B && n < m) {
					total++;
					
				}
				n1 = m;
				if(n1 == n){
					break;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << total << endl;

	}
	
}	
