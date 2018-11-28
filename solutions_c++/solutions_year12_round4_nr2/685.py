#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const int INF = 2000000000;
const double EPS = 0.000000001;

double dist(double x1, double y1, double x2, double y2) {
	return sqrt((x1 - x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int n, H, W;
		cin >> n >> W >> H;
		vector <pair <int, int> > R(n);
		for(int i = 0; i < n; ++i) {
			cin >> R[i].first;
			R[i].second = i;
		}
		sort(R.begin(), R.end());
		reverse(R.begin(), R.end());
		vector <pair <int, int> > ans(n);
		ans[R[0].second] = make_pair(0, 0);
		int curx = 0, cury = 0;
		bool up = true, right = false, down = false, left = false;
		for(int i = 1; i < n; ++i) {
			if(up) {
				if(W - (curx + R[i-1].first + R[i].first) >= 0) {
					curx += R[i-1].first + R[i].first;
					ans[R[i].second] = make_pair(curx, 0);
				}
				else {
					up = false;
					right = true;
					--i;
				}
			}
			else if(right) {
				if(H - (cury + R[i - 1].first + R[i].first) >= 0) {
					cury += R[i - 1].first + R[i].first;
					ans[R[i].second] = make_pair(W, cury);
				}
				else {
					right = false;
					down = true;
					--i;
				}
			}
			else if(down) {
				if(curx - R[i-1].first - R[i].first >= 0) {
					curx -= R[i-1].first + R[i].first;
					ans[R[i].second] = make_pair(curx, H);
				}
				else {
					down = false;
					left = true;
					--i;
				}
			}
			else if(left) {
					cury -= R[i - 1].first + R[i].first;
					ans[R[i].second] = make_pair(0, cury);
			}
		}
		cout << "Case #" << t << ":";
		for(int i = 0; i < n; ++i)
			printf(" %d %d", ans[i].first, ans[i].second);
		cout << endl;
	}

    return 0;
}