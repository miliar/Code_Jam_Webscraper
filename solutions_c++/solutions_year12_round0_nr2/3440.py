#include <algorithm>
#include <iostream>
#include <iterator>
#include <fstream>
#include <map>
#include <set>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::pair;
using std::set;
using std::string;
using std::vector;

typedef pair<int, int> Metadata;
typedef pair<Metadata, vector<int> > TestCase;

vector<TestCase> ParseInput(const string& filename) {
	vector<TestCase> res;

	std::ifstream fin;
	fin.open(filename.c_str(), std::ifstream::in);
	if (fin.fail()) {
		cout << "Failed to open " << filename << endl;
		return res;
	}

	int num_test_cases;
	fin >> num_test_cases;
	for (int i = 0; i < num_test_cases; ++i) {
		int num_googlers, num_surprsing, best_result;
		fin >> num_googlers >> num_surprsing >> best_result;
		Metadata metadata = std::make_pair(num_surprsing, best_result);
		vector<int> scores;
		for (int j = 0; j < num_googlers; ++j) {
			int score;
			fin >> score;
			scores.push_back(score);
		}
		res.push_back(std::make_pair(metadata, scores));
	}

	fin.close();
	return res;
}

bool CanSplitNormal(int score, int base) {
	int target = base;
	int ub = score / 3 + 1;

	while (target <= ub) {
		int remain = score - target;
		if (remain < 0)
			break;

		int lower = target - 1 < 0 ? 0 : target - 1;
		int upper = target + 1 > 10 ? 10 : target + 1;
		for (int i = lower; i <= upper; ++i) {
			if (remain - i < 0)
				break;

			if (abs(remain - i - i) < 2 && abs(remain - i - target) < 2) {
				return true;
			}
		}
		target++;
	}

	return false;
}

bool CanSplitSurpise(int score, int base) {
	int target = base;
	int ub = score / 3 + 2;

	while (target <= ub) {
		int remain = score - target;
		if (remain < 0)
			break;

		int lower = target - 2 < 0 ? 0 : target - 2;
		int upper = target + 2 > 10 ? 10 : target + 2;
		for (int i = lower; i <= upper; ++i) {
			if (remain - i < 0)
				break;

			if (abs(remain - i - i) < 3 && abs(remain - i - target) < 3) {
				return true;
			}
		}
		target++;
	}
	return false;
}

bool IsTrue(int flag) {
	return flag;
}

bool IsFalse(int flag) {
	return !flag;
}

int AnalyzeScore(const TestCase& test_case) {
	int target = test_case.first.second;
	int surprises = test_case.first.first;
	int num_scores = test_case.second.size();
	int count = 0;
	vector<bool> normal(num_scores, false);
	vector<bool> surprise(num_scores, false);
	for (int i = 0; i < num_scores; ++i) {
		if (CanSplitNormal(test_case.second[i], target)) {
			count++;
			continue;
		}
		
		if (CanSplitSurpise(test_case.second[i], target)) {
			if (surprises > 0) {
				surprises--;
				count++;
			}
		}		
	}

	return count;
}

int main(int argc, char** argv) {

	vector<TestCase> input_lines = ParseInput(string(argv[1]));
	int num_lines = input_lines.size();

	std::ofstream fout;
	fout.open("output.txt",std::ofstream::out);
	if (fout.fail()) {
		cout << "Failed to open output.txt for writing." << endl;
		return 1;
	}

	for (int i = 0; i < num_lines; ++i) {
		int res = AnalyzeScore(input_lines[i]);
		fout << "Case #" << i+1 << ": " << res << endl;
	}

	fout.close();
	return 0;
}