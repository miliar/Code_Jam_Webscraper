#include <iostream>
#include <vector>


using namespace std;


int N, M;
int want[200][20];
vector<int> ret;
int found;
int has[200];


void display(int t) {
	cout << "Case #" << t << ":";
	if (!found) cout << " IMPOSSIBLE" << endl;
	else {
		for (int i = 0; i < ret.size(); i++) {
			cout << " " << ret[i];
		}
		cout << endl;
	}
}


void solve() {
	int states = (1 << N);


	found = 0;
	int bestcounter;
	for (int cur = 0; cur < states; cur++) {
		int counter = 0;
		for (int i = 0; i < M; i++) has[i] = 0;
		
		for (int i = 0; i < N; i++) {
			int malted = (cur & (1 << i)) != 0;
			if (malted) counter++;
			
			for (int j = 0; j < M; j++) {
				int k = want[j][i];
				if (k == 1 && !malted || k == 2 && malted)
					has[j] = 1;
			}
		}

		int ok = 1;
		for (int i = 0; i < M; i++) {
			if (!has[i]) {
				ok = 0;
				break;
			}
		}

		if (ok) {
			if (!found || (counter < bestcounter)) {
				found = 1;
				bestcounter = counter;
				ret.clear();
				for (int i = 0; i < N; i++) {
					int malted = (cur & (1 << i)) != 0;
					ret.push_back(malted);
				}
			}
		}
	}
}


int main() {
	int C;
	cin >> C;
	for (int t = 1; t <= C; t++) {
		cin >> N >> M;

		for (int i = 0; i < M; i++) {
			int T;
			cin >> T;
			
			for (int j = 0; j < N; j++) {
				want[i][j] = 0;
			}
			
			for (int j = 0; j < T; j++) {
				int p1, p2;
				cin >> p1 >> p2;
				p1--;
				p2++;
				want[i][p1] = p2;
			}
		}

		solve();

		display(t);
	}

	return 0;
}

