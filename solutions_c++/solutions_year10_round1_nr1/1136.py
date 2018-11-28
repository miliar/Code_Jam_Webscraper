/*
 * main.cpp
 *
 *  Created on: 2010-5-22
 *      Author: haying
 */

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i, b, e) for (int i = (b), _e = e; i < _e; i ++)
#define REP(i, n) FOR(i, 0, (n))
#define FOR_REV(i, rb, b) for (int i = (rb), _b = (b); i >= _b; i --)

#define sz size()
template<class T> inline int size(const T &c) { return c.sz; }
#define FOR_EACH(i, c) REP(i, size(c))

#define itype(c) __typeof((c).begin())
#define ITER(it, c) for(itype(c) it = (c).begin(); it != (c).end(); it ++)

#define pb push_back
#define pf push_front
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define REVERSE(c) reverse(all(c))

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i >> x; return x; }
template <class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define PI acos(-1.)
#define EPS 1e-308
#define INT_INF static_cast<int>((1LL << (sizeof(int) * 8 - 1)) - 1)

char board2[51][51];

int main() {
	int T, case_num = 0;
	cin >> T;
	while (T != case_num ++) {
		cout << "Case #" << case_num << ": ";
		int N, K;
		cin >> N >> K;
		vector<string> board;
		board.resize(N);
		REP(i, N) {
			string line;
			cin >> line;
			board[i] = "";
			ITER(lit, line) {
				if (*lit == '.') {
					continue;
				}
				else {
					board[i] += *lit;
				}
			}
		}
		FOR_EACH(i, board) {
			strncpy(board2[i], string(N, '.').c_str(), N - board[i].sz);
			strcpy(board2[i] + N - board[i].sz, board[i].c_str());
		}
		bool is_r = false, is_b = false;
		string r_str(K, 'R');
		string b_str(K, 'B');
		ITER(bit, board) {
			if (bit->find(r_str) != string::npos) {
				is_r = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
			if (bit->find(b_str) != string::npos) {
				is_b = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
		}
		REP(i, N) {
			string src = "";
			REP(j, N) {
				src += board2[j][i];
			}
			if (src.find(r_str) != string::npos) {
				is_r = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
			if (src.find(b_str) != string::npos) {
				is_b = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
		}

		REP(i, N) {
			string src = "";
			FOR(j, i, N) {
				src += board2[j][j + i];
			}
			if (src.find(r_str) != string::npos) {
				is_r = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
			if (src.find(b_str) != string::npos) {
				is_b = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
		}
		FOR(i, 1, N) {
			string src = "";
			FOR(j, i, N) {
				src += board2[j][j - i];
			}
			if (src.find(r_str) != string::npos) {
				is_r = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
			if (src.find(b_str) != string::npos) {
				is_b = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
		}

		REP(i, N) {
			string src = "";
			FOR_REV(j, i, 0) {
				src += board2[j][i - j];
			}
			if (src.find(r_str) != string::npos) {
				is_r = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
			if (src.find(b_str) != string::npos) {
				is_b = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
		}
		FOR(i, N, 2 * N - 1) {
			string src = "";
			FOR_REV(j, N - 1, i - N + 1) {
				src += board2[j][i - j];
			}
			if (src.find(r_str) != string::npos) {
				is_r = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
			if (src.find(b_str) != string::npos) {
				is_b = true;
				if (is_r && is_b) {
					goto FINISH;
				}
			}
		}
FINISH:
		if (is_r && is_b) {
			cout << "Both\n";
		}
		else if (!is_r && is_b) {
			cout << "Blue\n";
		}
		else if (is_r && !is_b) {
			cout << "Red\n";
		}
		else {
			cout << "Neither\n";
		}
	}
	return 0;
}
