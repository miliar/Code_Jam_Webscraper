#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		int k;
		string S;
		cin >> k;
		cin >> S;
		int Nmin = S.size();
		vector <int> p;
		p.clear();
		for (int j = 0; j < k; j++) p.push_back(j);
		do {
			int N = 0;
			char last = '_';
			for (int j = 0; j < S.size(); j++) {
				int a = j / k;
				char c = S[a * k + p[j % k]];
				if (c != last) N++;
				last = c;
			}
			if (N < Nmin) Nmin = N;
		} while (next_permutation(p.begin(), p.end()));
		printf("Case #%d: %d\n", i, Nmin);
	}
}

