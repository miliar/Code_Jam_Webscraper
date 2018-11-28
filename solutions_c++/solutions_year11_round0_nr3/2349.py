#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char **argv) {
	int cases;
	cin >> cases;
	for(int i = 0; i < cases; ++i) {
		vector<int> candies;
		
		int candycount;
		cin >> candycount;
		for(int j = 0; j < candycount; ++j) {
			int number;
			cin >> number;

			candies.push_back(number);
		}
		
		sort(candies.begin(), candies.end());
		int bestmatch = 0;
		
		for(int rightstart = 1; rightstart < candycount; ++rightstart) {
			int left_p = 0, left_s = 0, right_p = 0, right_s = 0;
			for(int left = 0; left < rightstart; ++left) {
				left_p ^= candies[left];
				left_s += candies[left];
			}
			
			for(int right = rightstart; right < candycount; ++right) {
				right_p ^= candies[right];
				right_s += candies[right];
			}
			
			//printf("Pile split at %d, lp = %d ls = %d rp = %d rs = %d\n", rightstart, left_p, left_s, right_p, right_s);
			
			if(left_p == right_p) {
				//printf("This is a match!\n");
				int seanspile = (left_s > right_s) ? left_s : right_s;
				if(seanspile > bestmatch) {
					bestmatch = seanspile;
				}
			}
		}
		
		cout << "Case #" << (i + 1) << ": ";
		if(bestmatch == 0) {
			cout << "NO" << endl;
		}
		else {
			cout << bestmatch << endl;
		}
	}
}
