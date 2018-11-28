#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

class Point {
public:
	int origPos;
	int curPos;
	int left;
	int right;
	Point() { }
	Point(int o, int c, int l, int r) : origPos(o), curPos(c), left(l), right(r) { }
};

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int D, C;
		cin >> C >> D;
		vector<pair<int,int> > stands;
		for (int c = 0; c < C; c++) {
			// stands
			int P; int V;
			cin >> P >> V;
			stands.push_back(make_pair(P,V));
		}
		sort(stands.begin(),stands.end());
		long long curDist = 0;
		long long longestTime = 0;
		long long totNum = 0;
		double lo = 0; double hi = 1e9;
		int iter = 0;
#define ITER 150
		int atleast = 0;
		while (lo <= hi && iter < ITER) {
			double mid = (lo + hi) / 2.0;
			// test
			bool ok = true;
			double avail = stands[0].first - mid;
			//cout << "avail start: " << avail << "\n";
			for (int i = 0; i < stands.size(); i++) {
				long long len = (stands[i].second-1) * D;
				//cout << "len: " << len << "\n";
				if (stands[i].first - mid > avail) {
					// xxxx ... yyyy case
					avail = stands[i].first - mid + stands[i].second * D;
					if (stands[i].first + mid < avail - D) {
						//cout << "died case 1: " << i << "\n";
						ok = false;
						break;
					}
					//cout << "case 1 avail: " << avail << "\n";
				} else {
					// xxxxyyy case
					avail = avail + stands[i].second * D;
					if (stands[i].first + mid < avail - D) {
						//cout << "died case 2: " << i << "\n";
						ok = false;
						break;
					}
					//cout << "case 2 avail: " << avail << "\n";
				}
			}
			if (ok) {
				hi = mid;
				atleast++;
			} else {
				lo = mid;
			}
			//cout << "L: " << lo << " H: " << hi << " M: " << mid << " OK: " << ok << "\n";
			iter++;
		}
		cout << "Case #" << (t+1) << ": " << lo << "\n";
	}
	return 0;
}