#include <iostream>
#include <cstdio>

using namespace std;

int ts[110];
char ob[110];

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int n;
		cin >> n;
		for(int i = 0; i < n; ++i) {
			cin >> ob[i] >> ts[i];
			ob[i] = (ob[i] == 'O' ? 0 : 1);
		}
		int res = 0, pos[2] = {1, 1};
		for(int i = 0; i < n; ++i) {
			int np[2] = {-1, -1};
			for(int j = i; j < n; ++j) {
				if(np[ob[j]] == -1) np[ob[j]] = ts[j];
			}
			int dis = abs(pos[ob[i]] - ts[i]) + 1;
			res += dis;
			pos[ob[i]] = ts[i];
			if(np[1 - ob[i]] < pos[1 - ob[i]]) pos[1 - ob[i]] = max(pos[1 - ob[i]] - dis, np[1 - ob[i]]);
			else if(np[1 - ob[i]] > pos[1 - ob[i]]) pos[1 - ob[i]] = min(pos[1 - ob[i]] + dis, np[1 - ob[i]]);
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
