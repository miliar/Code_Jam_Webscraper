#include "fstream"
#include "vector"
#include "algorithm"

using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

void solve(int test) {
	int N;
	fin >> N;
	vector<int> dist(N), length(N);
	for (int i = 0; i < N; i++) {
		fin >> dist[i] >> length[i];
	}
	int D;
	fin >> D;

	vector<int> active(N);
	active[0] = dist[0];
	bool possible = false;
	for (int i = 0; i < N && !possible; i++) {
		for (int j = i + 1; j < N && active[i] + dist[i] >= dist[j]; j++) {
			active[j] = max(active[j], min(min(active[i], length[j]), dist[j] - dist[i]));
		}
		possible |= active[i] + dist[i] >= D;
	}

	if (possible) {
		fout << "Case #" << test << ": YES\n";
	}
	else {
		fout << "Case #" << test << ": NO\n";
	}
}

int main() {

	int T;
	fin >> T;
	for (int i = 1; i <= T; i++) {
		solve(i);
	}

	return 0;
}
