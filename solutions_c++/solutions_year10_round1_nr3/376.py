#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

typedef pair<int, int> Position;
map<Position, bool> win_status;

bool solve(Position pos) {
//	printf("%d %d\n", pos.first, pos.second);
	if (pos.first == 0 || pos.second == 0)
		return true;

	if (pos.first == pos.second)
		return false;

	if (pos.first < pos.second)
		swap(pos.first, pos.second);

	map<Position, bool>::iterator it = win_status.find(pos);
	if (it != win_status.end())
		return it->second;

	for(int k = pos.first / pos.second; k > 0; --k) {
		if (solve(make_pair(pos.first - pos.second * k, pos.second)) == false) {
			win_status[pos] = true;
			return true;
		}
	}
	win_status[pos] = false;
	return false;
}

int main() {
	freopen("f:/downloads/C-small-attempt1.in", "r", stdin);
	freopen("f:/downloads/output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int z = 0; z < T; ++z) {
		int A1, A2, B1, B2;
		int result = 0;

		scanf("%d%d%d%d\n", &A1, &A2, &B1, &B2);

		for(int A = A1; A <= A2; ++A) {
			for(int B = B1; B <= B2; ++B) {
				if (solve(make_pair(A, B)) == true) {
					++result;
				}
			}
		}

		printf("Case #%d: %d\n", z + 1, result);
	}
}
