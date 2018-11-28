#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

template <class A, class B> void CONV(A& x, B& y) { stringstream s; s << x; s >> y; }
typedef long long LL;
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define FORU(i, a) for (int i = a; ; ++i)
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

int main() {
	int t;
	cin >> t;
	cin.get();
	FOR(i, 0, t) {
		string s;
		getline(cin, s);
		if (next_permutation(s.begin(), s.end())) cout << "Case #" << i+1 << ": " << s << endl;
		else {
			SORT(s);
			FORU(j, 0) {
				if (s[j] != '0') {
					string temp = string(s.begin(), s.begin()+j);
					temp += '0';
					s.erase(s.begin(), s.begin()+j);
					s.insert(1, temp);
					cout << "Case #" << i+1 << ": " << s << endl;
					break;
				}
			}
		}
	}
}
