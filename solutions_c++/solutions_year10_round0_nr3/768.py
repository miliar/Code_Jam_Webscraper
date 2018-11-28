#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;

#define D(x)

template <class T>
ostream& operator<<(ostream& os, const vector<T>& v) {
	os << "[";
	for (int i = 0; i < v.size(); i++) {
		if (i > 0) os << ", ";
		os << v[i];
	}
	os << "]";
	return os;
}

int main() {
	int T;
	cin >> T;

	for (int caseNum = 1; caseNum <= T; caseNum++) {
		int R, k, N;
		cin >> R >> k >> N;
		D(cerr << "R=" << R << " k=" << k << " N=" << N);

		vector<int> g(N);
		for (int i = 0; i < N; i++) cin >> g[i];
		D(cerr << " g=" << g << endl);

		vector<int> groupSize(N), next(N);
		for (int i = 0; i < N; i++) {
			int count = 0, j;
			for (j = 0; j < N; j++) {
				int newCount = count + g[(i+j)%N];
				if (newCount > k) break;
				count = newCount;
			}
			groupSize[i] = count;
			next[i] = (i+j)%N;
		}
		D(cerr << "groupSize=" << groupSize << " next=" << next << endl);

		vector<int> positions;
		vector<bool> visited(N);

		int offset = 0;
		long long total = 0;

		while (R > 0) {
			if (visited[offset]) break;
			visited[offset] = true;
			positions.push_back(offset);


			total += groupSize[offset];
			D(cerr << "visiting offset " << offset << " with " << groupSize[offset]);
			D(cerr << ", total=" << total << endl);
			offset = next[offset];
			R--;
		}
		D(cerr << "positions=" << positions << endl);

		if (R > 0) {
			int cycleStart = find(positions.begin(), positions.end(), offset) - positions.begin();
			int cycleLength = positions.size() - cycleStart;
			long long cycleSize = 0;
			for (int i = cycleStart; i < positions.size(); i++) {
				cycleSize += groupSize[positions[i]];
			}
			D(cerr << "cycle at " << cycleStart << ", size=" << cycleSize << ", length="
					<< cycleLength << endl);

			D(cerr << "running " << (R / cycleLength) << " times plus " << (R % cycleLength) << endl);
			total += (R / cycleLength) * cycleSize;
			for (int i = 0; i < R % cycleLength; i++) {
				total += groupSize[positions[cycleStart + i]];
			}
		}

		cout << "Case #" << caseNum << ": " << total << endl;
	}
}
