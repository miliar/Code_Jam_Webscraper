/*
 *  File: Program6.cpp
 *  ------------------
 *
 *  Created by Elina Robeva on 5/21/10.
 *
 */
 
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

//int res[31][31];

/*
void fillin() {
	for(int i = 1; i < 31; ++i) {
		for(int j = i; j < 31; ++j) {
			res
		}
	}
}*/

int win(int a, int b) {
	//cout << a << " " << b << endl;
	int k = a / b;
	int r = a % b;
	if(r == 0) {
		if(a == b) return 0;
		else return 1;
	}
	if(k == 1) {
		return 1 - win(b, r);
	} else {
		//return 1 - win(b + r, b);
		return 1;
	}
}


int main() {
	freopen("/Users/erobeva/Downloads/C-small-attempt0(2).in","r",stdin);
	freopen("/Users/erobeva/Downloads/AAAout.txt", "w", stdout);
	
	int T;
	cin >> T;
	
	for(int i = 0; i < T; ++i) {
		int A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;
		int w = 0;
		for(int j = A1; j <= A2; ++j) {
			for(int k = B1; k <= B2; ++k) {
				//cout << j << " " << k << " ";
				if(j <= k) {
					w += win(k, j);
					//cout << w << endl;
				} else {
					w += win(j, k);
					//cout << w << endl;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << w << endl;
		
	}
	
	
	return 0;
}