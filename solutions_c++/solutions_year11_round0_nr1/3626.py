#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
 
using namespace std;

int main() {
	int T;
	freopen("c:\\A-large.in", "r", stdin);
	freopen("c:\\A-large.out", "w", stdout);
	scanf("%d", &T);

	for (int testCase = 1; testCase <= T; ++testCase) {
		int n;
		scanf("%d", &n);
		vector<int> but = vector<int>();
		vector<int> rob = vector<int>();

		for (int i = 0; i < n; ++i) {
			char s[5];
			int b;
			scanf("%s%d", &s, &b);
			but.push_back(b);
			rob.push_back(s[0] == 'O' ? 0 : 1);
		}

		int p1 = 1, p2 = 1;

		int time = 0;
		for (int i = 0; i < but.size(); ++i) {
			if (rob[i] == 0) {
				int next = p2;
				for (int j = i + 1; j < but.size(); ++j) {
					if (rob[j] == 1) {
						next = but[j];
						break;
					}
				}
				int tc = abs(but[i] - p1) + 1;
				p1 = but[i];

				time += tc;

				int tn = min(abs(next - p2), tc);

				if (p2 < next) {
					p2 += tn;
				} else {
					p2 -= tn;
				}
			} else {
				int next = p1;
				for (int j = i + 1; j < but.size(); ++j) {
					if (rob[j] == 0) {
						next = but[j];
						break;
					}
				}

				int tc = abs(but[i] - p2) + 1;
				p2 = but[i];

				time += tc;
				int tn = min(abs(next - p1), tc);

				if (p1 < next) {
					p1 += tn;
				} else {
					p1 -= tn;
				}				
			}
		}
		printf("Case #%d: %d\n", testCase, time); 
	}

	return 0;
}