/*
 *  File: Program3.cpp
 *  ------------------
 *
 *  Created by Elina Robeva on 5/7/10.
 *
 */

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int T;

struct tup {
	int cost;
	int next;
};

int main() {
	freopen("/Users/erobeva/Downloads/C-large.in","r",stdin);
	freopen("/Users/erobeva/Downloads/AAAout.txt", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; ++i) {
		int R, k, N;
		cin >> R >> k >> N;
		int groups[1000];
		for(int j = 0; j < N; ++j) {
			cin >> groups[j];
			
		}
		
		tup trans[1000];
		for(int j = 0; j < N; ++j) {
			int s = j;
			int people = groups[s];
			
			long long cost = 0;
			while(people <= k) { 
				
				cost += groups[s];
				if(s < N-1) {
					s++;
				} else {
					s = 0;
				}
				people += groups[s];
				if(s == j) {
					break;
				}
			}
			trans[j].cost = cost;
			trans[j].next = s;
		}
		long long total = 0;
		int cur = 0;
		for(int l = 0; l < R; ++l) {
			total += trans[cur].cost;
			cur = trans[cur].next;
		}
		cout << "Case #" << i + 1 << ": " << total << endl; 
		
	}

	
	return 0;
	
}
