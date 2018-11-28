#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using std::cout;
using std::endl;
using std::pair;
using std::string;
using std::vector;

typedef pair<int, int> TestCase;

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
		int A, B;
		fin >> A >> B;
		res.push_back(std::make_pair(A, B));
	}

	fin.close();
	return res;
}

int Factorial(int n) {
	if (n==1) {
		return 1;
	}
	return n*Factorial(n-1);
}

int Combination(int n, int r) {
	if (n < r)
		return 0;

	if (n == r)
		return 1;

	return Factorial(n)/(Factorial(r)*Factorial(n-r));
}

int GetRecycledNumbers(int num, int lb, int ub, vector<bool>& mask) {
	int recycled_number_count = 0;

	std::ostringstream oss(std::ostringstream::out);
	oss << num;
	string num_str = oss.str();

	int digits = num_str.length();
	for (int i = 1; i < digits; ++i) {
		std::rotate(num_str.begin(), num_str.begin()+1, num_str.end());
		if (num_str[0] == '0')
			continue;
		int rotated = atoi(num_str.c_str());
		if (rotated == num)
			break;
		if (rotated >= lb && rotated <= ub) {
			recycled_number_count++;
			mask[rotated - lb] = true;
		}
	}

	return Combination(recycled_number_count + 1, 2);
}

int FindRecycledPairs(int lb, int ub) {
	vector<bool> mask(ub-lb+1, false);

	int res = 0;
	for (int i = lb; i <= ub; ++i) {
		if (mask[i-lb])
			continue;
		mask[i-lb] = true;
		res += GetRecycledNumbers(i, lb, ub, mask);
	}

	return res;
}

int main(int argc, char** argv) {
	vector<TestCase> test_cases = ParseInput(string(argv[1]));
	int num_test_cases = test_cases.size();

	std::ofstream fout;
	fout.open("output.txt",std::ofstream::out);
	if (fout.fail()) {
		cout << "Failed to open output.txt for writing." << endl;
		return 1;
	}

	for (int i = 0; i < num_test_cases; ++i) {
		fout << "Case #" << i+1 << ": " << FindRecycledPairs(test_cases[i].first, test_cases[i].second) << endl;
	}

	fout.close();	
	return 0;
}