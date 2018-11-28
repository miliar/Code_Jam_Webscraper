#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#define out(v) cout << #v << ": " << (v) << endl
using namespace std;
typedef long long LL;

int T, C, D, N;
string combine[40];
string opposed[30];
string invoke;

void adj(char &x, char &y) {
	if (x > y) swap(x, y);
}
void com(string &v) {	
	int k = v.size();
	if (k >= 2) {
		string t = v.substr(k - 2, 2);
		adj(t[0], t[1]);
		for (int i = 0; i < C; ++i)
			if (combine[i].substr(0, 2) == t) {
				v = v.substr(0, k - 2) + combine[i][2];
				return;
			}
	}
}
void opp(string &v) {
	int k = v.size();
	for (int i = 0; i < k; ++i)
		for (int j = i + 1; j < k; ++j) {
			string t = string(1, v[i]) + v[j];
			adj(t[0], t[1]);
			for (int f = 0; f < D; ++f)
				if (opposed[f] == t) {
					v.clear();
					return;
				}
		}
}

int main() {
	cin >> T;
	for (int id = 1; id <= T; ++id) {
		cin >> C;
		for (int i = 0; i < C; ++i)	{
			cin >> combine[i];
			adj(combine[i][0], combine[i][1]);
		}
		cin >> D;
		for (int i = 0; i < D; ++i) {
			cin >> opposed[i];
			adj(opposed[i][0], opposed[i][1]);
		}
		cin >> N;
		cin >> invoke;
		string v;
		for (int i = 0; i < N; ++i) {
			v += invoke[i];
			com(v);
			opp(v);
		}
		cout << "Case #" << id << ": [";
		for (int i = 0; i < v.size(); ++i)
			cout << (i == 0 ? "" : ", ") << v[i];
		cout << "]" << endl;
	}
	return 0;
}
