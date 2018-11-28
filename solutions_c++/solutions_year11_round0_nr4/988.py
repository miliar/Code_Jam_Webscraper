/*
 *  File: GoroSort.cpp
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
	freopen("/Users/erobeva/Downloads/D-large (1).in","r",stdin);
	freopen("/Users/erobeva/Downloads/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOut.txt", "w", stdout);
	
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		int N;
		cin >> N;
		vector <int> initial(N);
		vector <int> sorted(N);
		for(int j = 0; j < N; ++j) {
			cin >> initial[j];
			sorted[j] = initial[j];
		}
		sort(sorted.begin(), sorted.end());
		int equal = 0;
		for(int j= 0; j < N; ++j) {
			if(initial[j] == sorted[j]) {
				equal++;
			}
		}
		cout << "Case #" << i + 1 << ": " << N - equal << endl;		
	}




	return 0;
}
