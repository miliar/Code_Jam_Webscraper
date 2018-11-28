#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

bool harmony(int a, int b) {
	if (a%b==0 || b%a == 0)
		return true;
	return false;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, L, H;
		cin >> N >> L >> H;
		int *F = new int[N];
		for (int k = 0; k < N; k++)
			cin >> F[k];
		bool found = false;
		int f;
		for (f = L; f <= H; f++) {
			int j = 0;
			for (; j < N; j++) {
				if (!harmony(f, F[j]))
					break;
			}
			if (j == N) {
				found = true;
				break;
			}
		}
		if (found) {
			cout << "Case #"<< i+1<<": "<< f<< endl;
		} else {
			cout << "Case #"<< i+1<<": "<< "NO" << endl;
		}
	}
}

