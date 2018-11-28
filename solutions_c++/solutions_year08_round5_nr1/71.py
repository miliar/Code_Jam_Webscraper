#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int getArea(vector <pair<int, int> > P) {
	long long ret = 0;
	for (int i = 0; i < P.size() - 1; ++i) {
		ret += P[i].first * P[i + 1].second - P[i].second * P[i + 1].first;
	}
	ret /= 2;
	return (ret > 0) ? ret : -ret;
}

char table[6010][6010];

void fill(int x, int y) {
	table[x][y] = 1;
	queue<pair<int, int> > Q;
	
	Q.push(make_pair(x, y));
	while (!Q.empty()) {
		pair<int, int> now = Q.front(), next; Q.pop();		
		for (int i = 0; i < 4; ++i) {
			next.first = now.first + dx[i];
			next.second = now.second + dy[i];
			if (next.first < 0 || next.first == 420) continue;
			if (next.second < 0 || next.second == 420) continue;
			if (table[next.first][next.second] == 0) {
				table[next.first][next.second] = 1;
				Q.push(next);
			}
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int cn = 1; cn <= T; ++cn) {
		printf("Case #%d: ", cn);
		int L, N;
		
		string S;
		cin >> L;

		int head = 0, x = 0, y = 0;
		vector <pair<int, int> > P;

		P.push_back(make_pair(x, y));

		for (int i = 0; i < L; ++i) {
			cin >> S >> N;
			for (int j = 0; j < N; ++j) {
				for (int k = 0; k < S.size(); ++k) {
					if (S[k] == 'F') {
						x += dx[head];
						y += dy[head];
						P.push_back(make_pair(x, y));
					}
					if (S[k] == 'R') head = (head + 1) % 4;
					if (S[k] == 'L') head = (head + 3) % 4;
				}
			}
		}

		int ret = -getArea(P);

		int minx[6001], miny[6001], maxx[6001], maxy[6001];
		for (int i = 0; i <= 6000; ++i) {
			minx[i] = miny[i] = 99999;
			maxx[i] = maxy[i] = -99999;
		}
		for (int i = 0; i < P.size() - 1; ++i) {
			if (P[i].first == P[i + 1].first) {
				miny[3000 + min(P[i].second, P[i + 1].second)] <?= 3000 + P[i].first;
				maxy[3000 + min(P[i].second, P[i + 1].second)] >?= 3000 + P[i].first;
			} else {
				minx[3000 + min(P[i].first, P[i + 1].first)] <?= 3000 + P[i].second;
				maxx[3000 + min(P[i].first, P[i + 1].first)] >?= 3000 + P[i].second;
			}
		}

		for (int i = 0; i <= 6000; ++i) {
			for (int j = 0; j <= 6000; ++j) {
				int ct = 0;
				if (miny[j] <= i) ct++;
				if (i < maxy[j]) ct++;
				if (minx[i] <= j) ct++;
				if (j < maxx[i]) ct++;
				if (ct >= 3) ret++;
			}
		}
		cout << ret << endl;
	}
}


