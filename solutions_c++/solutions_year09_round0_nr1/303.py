#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int L, D, N;

	cin >> L >> D >> N;
	vector<string> a(D);
	int s[26][L];

	for (int i = 0; i < D; ++i) {
		cin >> a[i];
	}
	for (int i = 0; i < N; ++i) {
		string x;
		cin >> x;
		int idx = 0;
		memset(s, 0, sizeof(s) );
		bool inp = false;
		for (int j = 0; j < x.length(); ++j) {
			if (x[j] == '(') {
				inp = true;
				continue;
			} else if (x[j] == ')') {
				inp = false;
				++idx;
				continue;
			} else {
				s[x[j] - 'a'][idx] = 1;
				if (!inp) ++idx;
			}
		}
		int ans = 0;
		bool match = true;
		for (int j = 0; j < D; ++j) {
			match = true;
			for (int k = 0; k < L; ++k) {
				if (s[a[j][k] - 'a'][k] == 0) {
					match = false;
					break;
				}
			}
			if (match) ++ans;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	
	return 0;
}

