#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <list>
using namespace std;

typedef long long lint;
typedef long long ulint;

unsigned RLE(vector<unsigned> &permutation, string &S) {
	string O = S;
	unsigned k = permutation.size();
	for (unsigned i = 0; i < S.size(); i++) {
		O[i] = S[i / k * k + permutation[i % k]];
	}
	unsigned streaks = 1;
	for (unsigned i = 1; i < O.size(); i++) {
		if (O[i - 1] != O[i]) {
			streaks++;
		}
	}
	return streaks;
}

int main(int argc, char const *argv[]) {
	unsigned nCases;
	cin >> nCases;
	for (unsigned N = 1; N <= nCases; N++) {
		unsigned k;
		string S;
		cin >> k >> S;
		
		vector<unsigned> permutation;
		for (unsigned i = 0; i < k; i++) {
			permutation.push_back(i);
		}
		unsigned best = RLE(permutation, S);
		while (next_permutation(permutation.begin(), permutation.end())) {
			best = min(best, RLE(permutation, S));
		}
		
		cout << "Case #" << N << ": "
		     << best << endl;
	}
	
	return 0;
}