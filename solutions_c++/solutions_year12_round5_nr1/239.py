#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


struct pp {
	int prob;
	int id;
};

vector<pp> pps;

bool cmpp(pp a, pp b) {
	return a.prob == b.prob ? a.id < b.id : a.prob > b.prob;
}

int main() {
	int t, n, l, p;
	cin >> t;
	for(int tt = 1; tt <= t; tt++) {
		cin >> n;
		pps.resize(n);

		for(int j = 0; j < n; j++) {
			cin >> pps[j].prob;
			pps[j].id = j;
		}

		for(int j = 0; j < n; j++)
			cin >> pps[j].prob;

		sort(pps.begin(), pps.end(), cmpp);

		cout << "Case #" << tt << ": ";
		for(int i = 0; i < n; i++)
			cout << pps[i].id << " ";
		cout << endl;
	}
}