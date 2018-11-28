/*
 *  problemB.cpp
 *  Codejam
 *
 *  Created by Michelangelo Partipilo on 5/8/10.
 *  Copyright 2010. All rights reserved.
 *
 */

#include <iostream>
#include <vector>

using namespace std;

/*
template<class T>
void printVector(T v)
{
	for (T::iterator it=v.begin(); it!=v.end(); it++) {
		cout << *it << " ";
	}
	cout << endl;
}
 */

int main (int argc, char * const argv[]) {
	long int k; // capacity
	long int R; // runs in a day
	long int N; // number of groups
	int T; // test cases
	
	cin >> T;
	
	for (int C=1; C<=T; C++) {
		cin >> R;
		cin >> k;
		cin >> N;
		
		vector<long int> groups(N, 0);
		vector< pair<long long int, long int> > sumCache(N, make_pair(0, 0));
		
		for (long int i=0; i<N; i++) {
			cin >> groups[i];
		}
		
		// Precalculate sums
		for (long int i=0; i<N; i++)
		{
			sumCache[i].second = i + 1;
			for (long int j=i, l=0; l<N; j=(j+1)%N, l++) {
				if (sumCache[i].first + groups[j] > k) break;
				sumCache[i].first += groups[j];
				sumCache[i].second = (j+1) % N;
			}
		}
		
		long long int sum = 0;
		long int currentIdx = 0;
		
		for (long int i=0; i<R; i++) {
			sum += sumCache[currentIdx].first;
			currentIdx = sumCache[currentIdx].second;
		}
		
		cout << "Case #" << C << ": "<< sum << endl;
	}
	
    return 0;
}
