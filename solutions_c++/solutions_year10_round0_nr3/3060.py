//============================================================================
// Name        : theme_park.cpp
// Author      : shailesh
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <deque>
using namespace std;

int total_roller_coaster_money(int R, int k, int N, deque<int>& group_sizes) {
	int res = 0;
	for (int i = 0; i < R; i++) {
		int iter_sum = 0;
		for (int j = 0; j < N; j++) {
			int start_elem = group_sizes.front();
			iter_sum = iter_sum + start_elem;
			if (iter_sum <= k) {
				group_sizes.pop_front();
				group_sizes.push_back(start_elem);
			} else {
				iter_sum = iter_sum - start_elem;
				break;
			}
		}

		res = res + iter_sum;
	}
	return res;
}

int main() {
	int num_of_tests = 0;
	int R;
	int k;
	int N;

	deque<int> group_sizes;
	string line;
	ifstream myfile("C-small-attempt0.in");
	//	ifstream myfile("A-large.in");
	ofstream out_file("C-small-attempt0.out");
	myfile >> num_of_tests;
	int i = 0;
	while (i < num_of_tests) {
		myfile >> R;
		myfile >> k;
		myfile >> N;
		group_sizes.clear();
		for (int j = 0; j < N; j++) {
			int elem;
			myfile >> elem;
			group_sizes.push_back(elem);
		}
		int count = total_roller_coaster_money(R, k, N, group_sizes);
		out_file << "Case #" << (i + 1) << ": " << count << endl;
		//		cout << "CASE #" << (i + 1) << ": " << count << endl;
		i++;
	}
	return 0;
}
