#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
#include <cstring>
#include <climits>

using namespace std;

int p, n;

priority_queue<pair<int, int> > ekipe;

int cene[1024][1024];
bool used[1024][1024];
int plac[1024][1024];

void turnoff(int d, int pos) {
	if (d < 0) return;
	if (plac[d][pos] == cene[d][pos] * used[d][pos]) {
		used[d][pos] = false;
	} else {
		turnoff(d - 1, pos * 2);
		turnoff(d - 1, pos * 2 + 1);
	}
}

bool optimize() {
	for (int i = 0; i < n; i++)
		plac[0][i] = cene[0][i] * used[0][i];
		
	for (int i = 1; i < p; i++) {
		for (int j = 0; j < (1 << (p - i - 1)); j++) {
			plac[i][j] = max(plac[i - 1][j * 2] + plac[i - 1][j * 2 + 1], cene[i][j] * used[i][j]);
			if (!used[i][j] && plac[i][j] > cene[i][j]) {
				used[i][j] = true;
				turnoff(i - 1, j * 2);
				turnoff(i - 1, j * 2 + 1);
				return true;
			}
		}
	}
	
	return false;
}

long long task() {
	//init
	memset(used, 0, sizeof used);

	//read
	scanf("%d", &p);
	n = 1 << p;
	
	for (int i = 0; i < n; i++) {
		int a; scanf("%d", &a);
		ekipe.push(make_pair(p - a, i / 2));
	}
	
	for (int i = 0; i < p; i++)
		for (int j = 0; j < (1 << (p - i - 1)); j++)
			scanf("%d", &cene[i][j]);
		
	//solve
	while (!ekipe.empty()) {
		int pos = ekipe.top().second, need = ekipe.top().first; ekipe.pop();
		
		for (int i = 0, j = pos; i < p; i++, j /= 2)
			if (used[i][j])
				need--;
				
		for (int i = 0, j = pos; i < p; i++, j /= 2) {
			if (need <= 0) break;
			if (!used[i][j]) {
				used[i][j] = true;
				need--;
			}
		}
	}
	
	while (optimize());
	
	long long r = 0;
	for (int i = 0; i < p; i++)
		for (int j = 0; j < (1 << (p - i - 1)); j++)
			r += cene[i][j] * used[i][j];
	return r;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		printf("%lld\n", task());
		//task();
		fflush(stdout);
	}
}

