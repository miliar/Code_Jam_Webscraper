#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin >> T;
	int N, S, p;
	for (int t=1; t<=T; t++) {
		cin >> N >> S >> p;
		vector<int> score(N);
		for (int i=0; i<N; i++) {
			cin >> score[i];
		}
		//N people      S surprising score    has at least a p
		// 6 people 29 20 8 18 18 21
		// 2 surprising score
		//has a 8
		sort(score.begin(), score.end());
		int ans = 0;
		for (int i=N-1; i>=0; i--) {
			if (score[i] >= 3*p-2) {
				ans++;
			}
			else if (score[i] >= 3*p-4) {
				if (p>=2) {
					if (S > 0) {
						S--;
						ans++;
					}
					else {
						break;
					}
				}
				else {
					if (p == 1) {
						if (score[i] >= 1) {
							if (S > 0) {
								S--;
								ans++;
							}
							else {
								break;
							}
						}
					}
					else {//p == 0
						if (score[i] >= 0) {
							if (S > 0) {
								S--;
								ans++;
							}
							else {
								break;
							}
						}
					}
				}
			}
			else {
				break;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}