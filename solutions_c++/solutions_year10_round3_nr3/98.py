/*
 * main.cpp
 *
 *  Created on: 2010-5-23
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

int main() {
	int T, case_num = 0;
	cin >> T;
	string LINE = "";
	REP(i, 256) {
		LINE += "01";
	}
	while (T != case_num ++) {
		int M, N, K = 0, max_len;
		cin >> M >> N;
		max_len = (M > N ? N : M);
		VI ans(max_len + 1, 0);
		ans[1] = M * N;
		VS board(M, "");
		REP(i, M) {
			string buf;
			cin >> buf;
			FOR_EACH(j, buf) {
				switch (buf[j]) {
				case '0': board[i] += "0000"; break;
				case '1': board[i] += "0001"; break;
				case '2': board[i] += "0010"; break;
				case '3': board[i] += "0011"; break;
				case '4': board[i] += "0100"; break;
				case '5': board[i] += "0101"; break;
				case '6': board[i] += "0110"; break;
				case '7': board[i] += "0111"; break;
				case '8': board[i] += "1000"; break;
				case '9': board[i] += "1001"; break;
				case 'A': board[i] += "1010"; break;
				case 'B': board[i] += "1011"; break;
				case 'C': board[i] += "1100"; break;
				case 'D': board[i] += "1101"; break;
				case 'E': board[i] += "1110"; break;
				case 'F': board[i] += "1111"; break;
				}
			}
		}
		FOR_REV(i, max_len, 2) {
			FOR(y0, 0, M - i + 1) {
				FOR(x0, 0, N - i + 1) {
					int first = -1;
					if (board[y0].substr(x0).find(LINE.substr(0, i)) == 0) {
						first = 0;
					}
					else if (board[y0].substr(x0).find(LINE.substr(1, i)) == 0) {
						first = 1;
					}
					else {
						continue;
					}
					bool valid = true;
					FOR(y, y0 + 1, y0 + i) {
						first = 1- first;
						if (board[y].substr(x0).find(LINE.substr(first, i)) != 0) {
							valid = false;
							break;
						}
					}
					if (valid) {
						FOR(y, y0, y0 + i) {
							FOR(x, x0, x0 + i) {
								board[y][x] = ' ';
							}
						}
						if (ans[i] == 0) {
							K ++;
						}
						ans[i] ++;
						ans[1] -= i * i;
					}
				}
			}
		}
		if (ans[1] != 0) {
			K ++;
		}
		cout << "Case #" << case_num << ": " << K << "\n";
		FOR_REV(i, max_len, 1) {
			if (ans[i] != 0) {
				cout << i << " " << ans[i] << "\n";
			}
		}
	}
	return 0;
}
