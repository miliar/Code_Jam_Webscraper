#include <cmath>
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int N;
int M;
int V;

int tree[10000];
int change[10000];

int best[10000][2];

int and(int x, int y) {
	return x * y;
}

int or(int x, int y) {
	if (x + y > 0) {
		return 1;
	}
	return 0;
}

bool hasChildren(int x) {
	if (2*x + 1 >= M) {
		return false;
	} else {
		return true;
	}
}

int findBest(int x, int val) {
	if (best[x][val] != -1) {
		return best[x][val];
	} if (!hasChildren(x)) {
		if (tree[x]==val) {
			return 0;
		} else {
			return M + 1000;
		}
	} else {
	//	if (hasChildren(2*x + 1)) {
	//		if (hasChildren(2*x + 2)) {
				int cost00, cost01,cost11;
				cost00 = findBest(2*x + 1, 0) + findBest(2*x + 2, 0);
				cost01 = findBest(2*x + 1, 0) + findBest(2*x + 2, 1);
				if (findBest(2*x + 1, 1) + findBest(2*x + 2, 0) < cost01) {
					cost01 = findBest(2*x + 1, 1) + findBest(2*x + 2, 0);
				}
				cost11 = findBest(2*x + 1, 1) + findBest(2*x + 2, 1);
				if (tree[x] == 1) {
					if (val == 1) {
						if (change[x]) {
							cost01++;
						} else {
							cost01 += M + 1000;
						}
						cost00+= M + 1000;
					} else {
						cost11+= M + 1000;
					}
				} else if (tree[x]==0) {
					if (val == 1) {
						cost00+= M + 1000;
					} else {
						cost11+= M + 1000;
						if (change[x]) {
							cost01++;
						} else {
							cost01 += M + 1000;
						}
					}
				}
				int sol = cost00;
				if (cost01 < sol) {
					sol = cost01;
				}
				if(cost11 < sol) {
					sol = cost11;
				}
				best[x][val] = sol;
				return best[x][val];
	/*		} else {
				int cost00, cost01,cost11;
				cost00 = findBest(2*x + 1, 0) + findBest(2*x + 2, 0);
				cost01 = findBest(2*x + 1, 0) + findBest(2*x + 2, 1);
				if (findBest(2*x + 1, 1) + findBest(2*x + 2, 0) < cost01) {
					cost01 = findBest(2*x + 1, 1) + findBest(2*x + 2, 0);
				}
				cost11 = findBest(2*x + 1, 1) + findBest(2*x + 2, 1);
				if (tree[x] == 1) {
					if (val == 1) {
						cost01++;
						cost00+= M + 1000;
					} else {
						cost11+= M + 1000;
					}
				} else if (tree[x]==0) {
					if (val == 1) {
						cost00+= M + 1000;
					} else {
						cost11+= M + 1000;
						cost01++;
					}
				}
				int sol = cost00;
				if (cost01 < sol) {
					sol = cost01;
				}
				if(cost11 < sol) {
					sol = cost11;
				}
				best[x][val] = sol;
				return best[x][val];
			}
		} else {
			int andVal = and(tree[2*x + 1], tree[2*x + 2]);
			int orVal = or(tree[2*x + 1], tree[2*x + 2]);
			if (tree[x] == 1) {
				if (andVal == val) {
					best[x][val] = 0;
				} else if (orVal == val) {
					best[x][val] = 1;
				} else {
					best[x][val] = M + 1000;
				}
				return best[x][val];
			} else if (tree[x] == 0) {
				if (orVal == val) {
					best[x][val] = 0;
				} else if (andVal == val) {
					best[x][val] = 1;
				} else {
					best[x][val] = M + 1000;
				}
				return best[x][val];
			}
		}*/
	}
}

int main() {
	fstream in;
	fstream out;
	in.open("prob1.in", fstream::in);
	out.open("prob1.out",fstream::out);

	in >> N;

	for (int a = 0; a < N; a++) {
		in >> M;
		in >> V;
		for (int b = 0; b < M; b++) {
			in >> tree[b];
			if (b < (M-1)/2) {
				in >> change[b];
			}
		}

		for (int c = 0; c < M; c++) {
			for (int cc = 0; cc < 2; cc++) {
				best[c][cc] = -1;
			}
		}
		findBest(0,V);
		out << "Case #" << a + 1 << ": ";
		if (best[0][V] > M) {
			out << "IMPOSSIBLE" << endl;
		} else {
			out << best[0][V] << endl;
		}
	}
	
	in.close();
	out.close();
	return 0;
}