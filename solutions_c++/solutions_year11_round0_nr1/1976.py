#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iostream>
#include <cassert>

using namespace std;

queue<int> instructions[2];
vector<int> turns;

int solve() {
	int result = 0;
	int index = 0;
	int pos[2];
	pos[0] = 1;
	pos[1] = 1;
	while (!instructions[0].empty() || !instructions[1].empty()) {
		int moved = 0;
		for (int r = 0; r < 2; ++r) {
			if (instructions[r].empty()) {
				continue;
			}
			int next = instructions[r].front();
			if (pos[r] < next) {
				++pos[r];
			}
			else if (pos[r] > next) {
				--pos[r];
			}
			else {
				if (turns[index] == r) {
					moved = 1;
					instructions[r].pop();
				}
			}
		}
		index += moved;
		++result;
	}
	return result;
}

int main() {
	int T, N;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	scanf("%d", &T);
	int k = 0;
	while (k < T) {
		scanf("%d", &N);
		turns.resize(N);
		for (size_t inst_ind = 0; inst_ind < N; ++inst_ind) {
			char robot;
			int pos;
			cin >> robot >> pos;
			if (robot == 'O') {
				instructions[0].push(pos);	
				turns[inst_ind] = 0;
			}
			else if (robot == 'B') {
				instructions[1].push(pos);
				turns[inst_ind] = 1;
			}
			else {
				assert(false);
			}
		}
		printf("Case #%d: %d\n", k + 1, solve());
		++k;		
	}
	return 0;
}

