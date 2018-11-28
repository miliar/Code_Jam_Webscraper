#include <algorithm>
#include <sstream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	string line;

	cin >> line;
	long long N = atoi(line.c_str());

	for (long long i = 0; i < N; ++i) {
		cin >> line;
		long long start = atoi(line.c_str());
		vector<long long> nlist;
		nlist.push_back(0);
		for (long long j = 0; j < line.size(); ++j) {
			long long d = line[j] - '0';
			nlist.push_back(d);
        }
        next_permutation(nlist.begin(), nlist.end());
        cout << "Case #" << i+1 << ": " ;
        bool first_zero = true;
        long long number = 0;
        for (long long j = 0; j < nlist.size(); ++j) {
        	if (first_zero && nlist[j] == 0) continue;
        	first_zero = false;
        	cout << nlist[j];
        }
        cout << endl;
    }

	return 0;
}
