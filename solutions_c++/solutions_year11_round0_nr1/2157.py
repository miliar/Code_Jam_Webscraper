#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>
using namespace std;

int T;
int N;
char p;
int x, res;
vector<pair<int, int> > o, b;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	for (int j = 1; j <= T; j++) {
		o.clear();
		b.clear();
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> p >> x;
			if (p == 'O') {
				o.push_back(make_pair(x, i));
			} else {
				b.push_back(make_pair(x, i));
			}
		}

		res = 0;
		int po = 0, pb = 0;
		int poso = 1, posb = 1;
		while (po < o.size() || pb < b.size()) {
			if (po != o.size() && pb != b.size()) {
				if (o[po].second < b[pb].second) {
					if (o[po].first == poso) {
						po++;
					} else {
						if (o[po].first < poso) poso--;
						else poso++;
					}

					if (b[pb].first != posb) {
						if (b[pb].first < posb) posb--;
						else posb++;
					}
				} else {
					if (b[pb].first == posb) {
						pb++;
					} else {
						if (b[pb].first < posb) posb--;
						else posb++;
					}

					if (o[po].first != poso) {
						if (o[po].first < poso) poso--;
						else poso++;
					}
				}
			} else {
				if (po != o.size()) {
					if (o[po].first == poso) {
						po++;
					} else {
						if (o[po].first < poso) poso--;
						else poso++;
					}	
				} else {
					if (b[pb].first == posb) {
						pb++;
					} else {
						if (b[pb].first < posb) posb--;
						else posb++;
					}
				}
			}
			res++;			
		}
		cout << "Case #" << j << ": " << res << endl;
	}
}