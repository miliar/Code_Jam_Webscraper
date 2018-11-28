#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz size()
#define iss istringstream
#define oss ostringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vs vector<string>

using namespace std;

vi R[6001], C[6001];
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

void solveCase(int Case) {
	fr(i, 6001) R[i].clear();
	fr(i, 6001) C[i].clear();
	int A;
	string s = "";
	cin >> A;
	fr(i, A) {
		int T;
		string ss;
		cin >> ss >> T;
		fr(j, T) s += ss;
	}
	int k = 0;
	int x = 3000, y = 3000;
	fr(i, s.sz) {
		if(s[i] == 'L') k = (k + 1)%4;
		if(s[i] == 'R') k = (k + 3)%4;
		if(s[i] == 'F') {
			int xn = x + dx[k], yn = y + dy[k];
			if(xn == x) {
				R[min(yn, y)].pb(x);
		//		cout << min(yn, y) << ' ' << x << endl;
			}
			else {
				C[min(xn, x)].pb(y);
			}
			x = xn, y = yn;
		}
	}
//	cout << s << endl;
	fr(i, 6001) sort(R[i].begin(), R[i].end());
	fr(i, 6001) sort(C[i].begin(), C[i].end());
	vector<pii> L;
//	cout << "cia" << endl;
	fr(i, 6001) {
		for(int j = 1; j < (int)R[i].sz - 1; j+=2) {
			
			for(int x = R[i][j]; x < R[i][j + 1]; x++) L.pb(mp(x, i));
		}
	}
//	cout << "xia" << endl;
	fr(i, 6001) {
		for(int j = 1; j < (int)C[i].sz - 1; j+=2) {
			for(int y = C[i][j]; y < C[i][j + 1]; y++) L.pb(mp(i, y));
		}
	}
	sort(L.begin(), L.end());
	L.resize(unique(L.begin(), L.end()) - L.begin());
	cout << "Case #" << Case << ": " << L.sz << endl;	
}

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int tests;
	cin >> tests;
	for(int test = 1; test <= tests; test++) solveCase(test);	
	return 0;
}
