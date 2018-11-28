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

void doit(int &cur_moment, int &O_rest, int &O_place, int &next_pos, int &B_rest, int &B_place) {
	int tmp = abs(O_place - next_pos);
//	cerr << "tmp = " << tmp << endl;
	while (tmp) {
		if (O_rest > 0) {
			--tmp;
			--O_rest;
		}
		else {
			++cur_moment;
			--tmp;
			++B_rest;
		}
	}
	O_place = next_pos;
	++cur_moment;
	O_rest = 0;
	++B_rest;
}

void solve(int testnum) {
	int n;
	cin >> n;
	int cur_moment = 0;
	int O_rest = 0;
	int B_rest = 0;
	int O_place = 1;
	int B_place = 1;
	for (int i = 0; i < n; ++i) {
//		cerr << "CM = " << cur_moment << endl;
		char color;
		int next_pos;
		cin >> color >> next_pos;
		if (color == 'O')
			doit(cur_moment, O_rest, O_place, next_pos, B_rest, B_place);
		else
			doit(cur_moment, B_rest, B_place, next_pos, O_rest, O_place);
	}
	cout << "Case #" << testnum << ": " << cur_moment << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) solve(i + 1);
}
