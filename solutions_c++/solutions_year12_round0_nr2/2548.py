/*
 *  DancingWithTheGooglers.cpp
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
using namespace std;


int main() {
	freopen("/Users/erobeva/Downloads/B-large.in","r",stdin);
	freopen("/Users/erobeva/Downloads/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOut.txt", "w", stdout);
	
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		int N, S, p;
		cin >> N >> S >> p;
		int total = 0;
		for(int j = 0; j < N; ++j){
			int score;
			cin >> score;
			if(score >= 3*p - 2){
				total++;
			} else {
				if(p == 1 && score == 0) {
					continue;
				}
				if(score >= 3*p - 4 && S >= 1){
					total++;
					S--;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << total << endl;
	}
	
}	
