#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#define out(v) cout << #v << ": " << (v) << endl
using namespace std;
typedef long long LL;
typedef pair<char, int> pr;

int T, N;
pr move[105];

int main() {
	cin >> T;
	for (int id = 1; id <= T; ++id) {
		cin >> N;
		for (int i = 0; i < N; ++i) cin >> move[i].first >> move[i].second;
		int O = 1, lastO = 0, B = 1, lastB = 0, now = 0;
		for (int i = 0; i < N; ++i)
			if (move[i].first == 'O') {
				int cost = abs(move[i].second - O);
				lastO = now = max(now, lastO + cost) + 1;
				O = move[i].second;
			} else {
				int cost = abs(move[i].second - B);
				lastB = now = max(now, lastB + cost) + 1;
				B = move[i].second;
			}
		cout << "Case #" << id << ": " << now << endl;
	}	
	return 0;
}
