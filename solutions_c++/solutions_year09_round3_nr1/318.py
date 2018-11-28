#include <iostream>

using namespace std;

long long V [100];
int N;
long long used [100];
int maxV;
int main () {
	int T;
	cin >> T;
	for (int x = 1; x <= T; ++x) {
		string v;
		cin >> v;
		cout << "Case #" << x << ": ";
		N = v.length();
		memset(used, 0, sizeof(used));
		maxV = -1;
		for (int i = 0; i < N; ++i) {
			if (v [i] != ' ') {
				int j = 0;
				if (i == 0) j = 1;
				while (used [j]) ++j;
				if (maxV < j) maxV = j;
				V [i] = j;
				for (int k = i + 1; k < N; ++k)
					if (v [k] == v [i]) {
						V [k] = j;
						v [k] = ' ';
					}
				v [i] = ' ';
				used [j] = 1;
			}
		}
		long long val = 0;
		long long B = maxV + 1;
		for (int i = 0; i < N; ++i) {
			val = val * B + V [i];
		}
		cout << val << endl;
	}
}
