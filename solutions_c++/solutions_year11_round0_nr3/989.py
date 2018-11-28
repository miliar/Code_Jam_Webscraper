/*
 *  File: CandySplitting.cpp
 *  ------------------
 *
 *  Created by Elina Robeva on 5/7/11.
 *
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <vector>
using namespace std;


int main() {
	freopen("/Users/erobeva/Downloads/C-large (1).in","r",stdin);
	freopen("/Users/erobeva/Downloads/AAAAAAAAAAAAAAAAAAAAAAAAAOut.txt", "w", stdout);
	
	int T;
	cin >> T;
	for(int i = 0 ; i < T; ++i) {
		int N;
		cin >> N;
		vector <int> piles(N);
		int total = 0;
		for(int j = 0; j <  N; ++j) {
			cin >> piles[j];
			total = total ^ piles[j];
		}
		if(total == 0) {
			int min = piles[0];
			for(int j = 1; j < N; ++j) {
				if(piles[j] < min) {
					min = piles[j];
				}
			}
			int result = 0;
			for(int j = 0; j < N; ++j) {
				result += piles[j];
			}
			result -= min;
			cout << "Case #" << i + 1 << ": " << result << endl;
		} else {
			cout << "Case #" << i + 1 << ": NO" << endl;
		}
		
		
	}
	
	
	
	
	
	
		
	 
	
	return 0;
}
