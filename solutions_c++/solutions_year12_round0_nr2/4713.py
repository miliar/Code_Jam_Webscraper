#include <map>
#include <cmath>
#include <queue>
#include <ctime>
#include <string>
#include <vector>
#include <fstream>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

struct triple {
	int a; int b; int c;
	triple(int _a, int _b, int _c): a(_a), b(_b), c(_c) {}
};

bool surprising(int a, int b, int c) {
	return ((abs(a - b) == 2 || abs(a - c) == 2 || abs(b - c) == 2) && abs(a - c) <= 2 && abs(a - b) <= 2);
}

bool pls(int a, int b, int c) {
	return (a >= 0 && a <= 10 && b >= 0 && b <= 10 && c <= 10 && c >= 0);
}

int main(int argc, char **argv) {

    ios::sync_with_stdio(false);

	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
	
	int t, n, s, p, k;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cin >> n >> s >> p;
		vector<triple> tr1, tr2;
		for(int j = 0; j < n; ++j) {
			cin >> k;
			bool was = false;
			for(int r = p; r - ((k - r) >> 1) < 3 && !was; ++r) {
				for(int b = r - 1; b < r + 2; ++b) {
					int ost = k - b - r;
					if((ost == b || ost == r || ost == r + 1 || ost == b + 1 || ost == r - 1 || ost == b - 1) && !surprising(r, b, ost) && pls(r, b, ost)) {
						tr1.push_back(triple(r, b, ost));
						was = true;
						break;
					}
				}
			}
			if(!was) {
				for(int r = p; r - ((k - r) >> 1) < 3 && !was; ++r) {
					for(int b = r - 2; b < r + 3; ++b) {
						int ost = k - r - b;
						if(surprising(r, b, ost) && pls(r, b, ost)) {
							tr2.push_back(triple(r, b, ost));
							break;
						}
					}
				}
			}
		}
		cout << "Case #" << i << ": ";
		int ans = min(s, (int)tr2.size());
		cout << ans + tr1.size() << endl;
	}

    return 0;
}