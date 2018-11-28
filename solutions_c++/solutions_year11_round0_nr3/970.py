#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

vector<int> v;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N;
		cin >> N;
		v.clear();
		for (int j = 0; j < N; j++) {
			int C;
			cin >> C;
			v.push_back(C);
		}
		sort(v.begin(), v.end());
		
		int vxor = 0;
		ll sum = 0;
		for (int j = 1; j < N; j++) {
			vxor ^= v[j];
			sum += v[j];
		}
		if (vxor == v[0]) cout << "Case #" << (i + 1) << ": " << sum << endl;
		else cout << "Case #" << (i + 1) << ": NO" << endl;
	}
	return 0;
}

