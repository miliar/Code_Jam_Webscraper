#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int MODD = 100003;

int cas, N, ans;
vector<int> v;

int av[] = {0, 1, 1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 
	5719, 10780, 20388, 38674, 73562, 140268, 268066, 513350, 984911, 
	1892875, 3643570, 7023562, 13557020 };

inline int get(int tar) {
	for (int i = 0; i < v.size(); i ++) {
		if (v[i] == tar)
			return i;
	}
	return -1;
}

inline bool ok () {
	int cur = N;
	while(true) {
		if (cur == 1)
			return true;

		int pos = get(cur);
		if (pos == -1)
			return false;
		cur = pos+1;
	}
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
 	freopen("output.txt", "w", stdout);

	cin >> cas;
	for (int c = 1; c <= cas; c ++) {
		cin >> N;
		cout << "Case #" << c << ": " << av[N]%MODD << endl;
	}

	return 0;
}