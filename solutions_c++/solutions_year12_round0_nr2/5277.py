// Topcoder.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ofstream ofs("C:\\Users\\v-hioiwa\\Desktop\\result.txt");

	int T;
	cin >> T;

	for (int t = 0; t < T; ++t) {
		stringstream ss;
		ss << "Case #" << t+1 << ": ";
		ofs << ss.str();

		int N, S, p;
		vector<int> scores;
		cin >> N >> S >> p;

		for (int n = 0; n < N; ++n) {
			int score;
			cin >> score;
			scores.push_back(score);
		}

		if (p == 0) {
			ofs << scores.size() << endl;
			continue;
		} else if (p == 1) {
			int result = 0;
			for (int i = 0; i < (int)scores.size(); ++i) {
				if (scores[i] >= 1) {
					++result;
				}
			}
			ofs << result << endl;
			continue;
		}


		sort(scores.begin(), scores.end(), greater<int>());

		int result = 0;
		int great_score = p * 3 - 2;
		int lower_score = p * 3 - 4;
		for (int id = 0; id < (int)scores.size(); ++id) {
			if (scores[id] >= great_score) {
				++result;
			} else if (scores[id] >= lower_score) {
				if (S > 0) {
					--S; ++result;
				} else {
					break;
				}
			} else {
				break;
			}
		}
		ofs << result << endl;
	}


	return 0;
}

