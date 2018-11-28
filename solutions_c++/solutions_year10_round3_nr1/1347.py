#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	int t;
	cin >> T;
	t = T;
	while(t--) {
		int N;
		cin >> N;
		int i = N, j;
		vector<pair<int, int> > wires(N, make_pair(0, 0));
		int Ai, Bi;
		while(i) {
			cin >> Ai >> Bi;
			wires[N-i] = make_pair(Ai, Bi);
			i--;
		}
		int counter = 0;
		for(i = 0; i < N; i++) {
			for(j = 0; j < N; j++) {
				if(wires[i].first < wires[j].first && wires[i].second > wires[j].second) counter++;
			}
		}
		cout << "Case #" << (T-t) << ": " << counter << endl;
	}
}