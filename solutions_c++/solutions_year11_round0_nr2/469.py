#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#define pb push_back
#define mp make_pair
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T a) {return a > 0 ? a : (-a); }
template<class T> T sqr(T a) {return a * a; }

using namespace std;

void solve(int testnum) {
	int c, d;
	cin >> c;
	vector<string> combine, oppose;
	for (int i = 0; i < c; ++i) {
		string s;           
		cin >> s;
		combine.push_back(s);
		swap(s[0], s[1]);
		combine.push_back(s);
	}
	c = sz(combine);
	cin >> d;
	for (int i = 0; i < d; ++i) {
		string s;           
		cin >> s;
		oppose.push_back(s);
		swap(s[0], s[1]);
		oppose.push_back(s);
	}
	d = sz(oppose);
	int n;
	cin >> n;
	vector<char> stack;
	for (int www = 0; www < n; ++www) {
		char ch;
		cin >> ch;
		stack.pb(ch);
		while (sz(stack) >= 2) {
			char a = stack[sz(stack) - 1];
			char b = stack[sz(stack) - 2];
			bool done = false;
			for (int i = 0; i < sz(combine); ++i)
				if (combine[i][0] == a && combine[i][1] == b) {
					stack.pop_back();
					stack.pop_back();
					stack.push_back(combine[i][2]);
					done = true;
					break;
				}
			if (!done) break;
		}
		for (int i = 0; i < sz(stack); ++i)
			for (int j = 0; j < sz(stack); ++j) if (i != j) {
				for (int k = 0; k < sz(oppose); ++k)
					if (oppose[k][0] == stack[i] && oppose[k][1] == stack[j]) {
						stack.clear();
						break;
					}
			}
	}
	cout << "Case #" << testnum << ": [";
	for (int i = 0; i < sz(stack); ++i) {
		if (i != 0) cout << ", ";
		cout << stack[i];
	}
	cout << "]\n";
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) solve(i + 1);
}
