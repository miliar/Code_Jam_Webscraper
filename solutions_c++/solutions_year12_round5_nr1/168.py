#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <string>

using namespace std;

int ps[1010], ls[1010];
int ss[1010];

int comp(int a, int b) {
	if(ps[b] * ls[a] < ps[a] * ls[b]) return 1;
	if(ps[b] * ls[a] == ps[a] * ls[b]) return a < b;
	return 0;
}

int main() {
	int T;
	cin >> T;
	for(int c = 1; c <= T; ++c) {
		int n;
		cin >> n;
		for(int i = 0; i < n; ++i) {
			cin >> ls[i];
			ss[i] = i;
		}
		for(int i = 0; i < n; ++i) {
			cin >> ps[i];
		}
		sort(ss, ss + n, comp);
		printf("Case #%d:", c);
		for(int i = 0; i < n; ++i) {
			printf(" %d", ss[i]);
		}
		cout << endl;
	}
	return 0;
}
