/*
 * http://code.google.com/codejam/contest/1460488/dashboard#s=p1
 * Problem B. Dancing With the Googlers
 */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <assert.h>

using namespace std;

int solve()
{
	int N, S, p;
	cin >> N >> S >> p;

	vector<int> t(N);
	for (int i=0; i<N; i++)
		cin >> t[i];

	vector<vector<int>> all;
	vector<int> score(t);	//tmp
	sort(score.begin(), score.end());

	do {
		all.push_back(score);
	} while (next_permutation(score.begin(), score.end()));

	int answer = 0;
	for (vector<vector<int>>::const_iterator it = all.begin(); it != all.end(); ++it) {
		int ans = 0;
		int suprise = S;
		for (int i=0; i<it->size(); i++) {
			int div = (*it)[i] / 3;
			int mod = (*it)[i] % 3;
			switch (mod) {
			case 0:
				if (suprise > 0) {
					suprise--;
					if (div >= 1 && div+1 <= 10 && div+1 >= p)
						ans++;
				} else if (div >= p)
					ans++;
				break;
			case 1:
				if (suprise > 0) {
					suprise--;
					if (div >= 1 && div+1 <= 10 && div+1 >= p)
						ans++;
				} else if (div + 1 >= p)
					ans++;
				break;
			case 2:
				if (suprise > 0) {
					suprise--;
					if (div >= 0 && div+2 <= 10 && div+2 >= p)
						ans++;
				} else if (div + 1 >= p)
					ans++;
				break;
			default:
				break;
			}
		}
		answer = max(ans, answer);
	}

	return answer;
}

int main()
{
	int T;
	cin >> T;
	for (int i=1; i<=T; i++) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}