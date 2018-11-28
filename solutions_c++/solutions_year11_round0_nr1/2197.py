#define _CRT_SECURE_NO_WARNINGS

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
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cassert>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

#define SZ(x) (int)(x).size()
#define FOR(i, seq, n) for(int i = (seq); i < (n); ++i)
#define FORD(i, seq, n) for(int i = (seq); i >= (n); --i)
#define REP(i, n) for(int i = 0; i < (n); ++i)
#define REPD(i, n) for(int i = (n) - 1; i >= 0; --i)
#define ALL(x) (x).begin(), (x).end()
#define SQR(x) (x)*(x)
typedef unsigned long long u64;
typedef signed long long i64;
typedef pair<int, int> pii;
#define X first
#define Y second
#define pb push_back

int o, b;
int no, nb;
vector<int> os, bs;

void walk(char ch)
{
	if (ch == 'O') {
		if (no < os.size()) {
			if (o < os[no])
				++o;
			else if (o > os[no])
				--o;
		}
	} else {
		if (nb < bs.size()) {
			if (b < bs[nb])
				++b;
			else if (b > bs[nb])
				--b;
		}
	}
}

int main()
{
	int T; cin >> T;
	REP (t, T) {
		int n; cin >> n;
		vector<char> op;
		os.clear(); bs.clear();
		REP (i, n) {
			char ch; int k;
			cin >> ch >> k;
			op.pb(ch);
			ch == 'O' ? os.pb(k) : bs.pb(k);
		}

		o = 1, b = 1;
		no = 0, nb = 0;
		int time = 0;
		for (int i = 0; i < n; ++i) {
			if (op[i] == 'O') {
				while (o != os[no]) {
					walk('O');
					walk('B');
					++time;
				}
				walk('B');
				++no;
			} else {
				while (b != bs[nb]) {
					walk('B');
					walk('O');
					++time;
				}
				walk('O');
				++nb;
			}
			++time;
		}
		cout << "Case #" << (t + 1) << ": " << time << endl;
	}
	return 0;
}
