#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cmath>
#include <stack>
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define mp make_pair
#define foreach(T, x, it) for (T::iterator it = x.begin(); it != x.end(); ++it)
using namespace std;
typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;

bool Test(int x, int p) { return (x >> p) & 1; }

vi Get(const string &s) {
	bool in = false;
	int cur = 0;
	vi r;
	for (int i = 0; i < sz(s); ++i) {

		if (s[i] == '(') {
			assert(!in);
			in = true;		
		}
		else if (s[i] == ')') {
			assert(in);
			in = false;
			r.pb(cur);
			cur = 0;
		}
		else {
			assert(islower(s[i]));
			if (in) {
				cur |= 1 << (s[i] - 'a');
			}
			else {
				r.pb(1 << (s[i] - 'a'));
			}
		}
	}
	assert(!in);
	assert(cur == 0);
	return r;
}

int main() {	
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int L, D, N;
	cin >> L >> D >> N;
	vector<string> words(D, "");
	for (int i = 0; i < D; ++i) {
		cin >> words[i];		
	}


	for (int i = 0; i < N; ++i) {
		string str;
		cin >> str;
		vector<int> fr = Get(str);
		int cnt = 0;
		if (sz(fr) == L) {
			
			for (int j = 0; j < sz(words); ++j) {
				bool ok = true;
				for (int k = 0; ok && k < L; ++k) {
					if (Test(fr[k], words[j][k] - 'a')) {
					}
					else {
						ok = false;
					}
				}
				if (ok) {
					++cnt;
				}
			}
		}
		printf("Case #%d: %d\n", i + 1, cnt);
	}
	return 0;
}

