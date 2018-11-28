#include <iostream>
#include <vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		int N;
		cin >> N;
		vector<pair<int, int> > wires (N);
		for (int i = 0; i < N ;++i) {
			cin >> wires[i].first >> wires[i].second;
		}
		int intersections = 0;
		for (int i = 0; i < N; ++i) {
			for (int j = i +1; j< N;++j) {
				if (wires[i].first < wires[j].first) {
					if (wires[i].second > wires[j].second) ++intersections;
				}
				else {
					if (wires[j].second > wires[i].second) ++intersections;
				}
			}
		}
		cout << "Case #" << cas << ": " << intersections << endl;
	}
}