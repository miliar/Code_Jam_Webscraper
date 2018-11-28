#include "stdafx.h"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const int MAX = 200 + 2;

bool A[MAX][MAX];
bool B[MAX][MAX];

int R;

int main()
{
//	ifstream input("C-small.in"); ofstream output("C-small.out", ios::out);
	ifstream input("C-small-attempt0.in"); ofstream output("C-small-attempt0.out", ios::out);
//	ifstream input("C-large.in"); ofstream output("C-large.out", ios::out);

	int C;

	input >> C;

	for (int t = 1; t <= C; t++) {
		input >> R;

		memset(A, false, sizeof(A));
		memset(B, false, sizeof(B));

		for (int i = 0; i < R; i++) {
			int x1, y1, x2, y2;

			input >> x1 >> y1 >> x2 >> y2;

			for (int x = x1; x <= x2; x++) {
				for (int y = y1; y <= y2; y++) {
					A[x][y] = true;
				}
			}
		}

		int ret = 0;

		while (true) {
			bool allDie = true;

			for (int x = 1; x < MAX; x++) {
				for (int y = 1; y < MAX; y++) {
					if (A[x][y]) {
						allDie = false;
						break;
					}
				}
			}

			if (allDie) {
				break;
			}

			memcpy(B, A, sizeof(B));

			for (int x = 1; x < MAX; x++) {
				for (int y = 1; y < MAX; y++) {
					if (A[x][y]) {
						int nx = x - 1;
						int ny = y;

						int wx = x;
						int wy = y - 1;

						if (nx >= 0 && nx < MAX && ny >= 0 && ny < MAX && wx >= 0 && wx < MAX && wy >= 0 && wy < MAX) {
							if (!A[nx][ny] && !A[wx][wy]) {
								B[x][y] = false;
							}
						}
					} else {
						int nx = x - 1;
						int ny = y;

						int wx = x;
						int wy = y - 1;

						if (nx >= 0 && nx < MAX && ny >= 0 && ny < MAX && wx >= 0 && wx < MAX && wy >= 0 && wy < MAX) {
							if (A[nx][ny] && A[wx][wy]) {
								B[x][y] = true;
							}
						}
					}
				}
			}

			memcpy(A, B, sizeof(A));
			ret++;
		}

		cout << "Case #" << t << ": " << ret << endl;
		output << "Case #" << t << ": " << ret << endl;
	}
}
