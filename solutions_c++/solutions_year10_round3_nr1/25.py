#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	int testCases;
	cin >> testCases;
	for (int curCase = 1; curCase <= testCases; curCase++) {
		int N;
		cin >> N;
		vector<pair<int, int> > v;
		for (int i = 0; i < N; i++) {
			int a, b;
			cin >> a >> b;
			v.push_back(make_pair(a, b));
		}
		int res = 0;
		for (int i = 0; i < N; i++) {
			for (int j = i + 1; j < N; j++) {
				if ((v[j].first - v[i].first) * (v[j].second - v[i].second) < 0)
					++res;
			}
		}
		cout << "Case #" << curCase << ": " << res << endl;
	}
	return 0;
}