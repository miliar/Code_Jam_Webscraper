#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define mp make_pair
#define all(a) a.begin(),a.end()

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

int test;

map<int, vi> hor, ver;

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

void solve() {
	hor.clear(); ver.clear();
	
	string S;

	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		string s; int t; cin >> s >> t;
		for (int j = 0; j < t; j++) S += s;
	}
	
	int x, y, d;
	x = y = d = 0;

	for (int i = 0; i < S.length(); i++) {
		if (S[i] == 'F') {
			int x1 = x, y1 = y;
			x += dx[d]; y += dy[d];
			int x2 = x, y2 = y;
			if (x1 > x2) swap(x1, x2);
			if (y1 > y2) swap(y1, y2);
			if (x1 == x2) ver[y1].push_back(x1);
			if (y1 == y2) hor[x1].push_back(y1);
		} 
		if (S[i] == 'L') {
			d =  (d + 3) % 4;
		}
		if (S[i] == 'R') {
			d = (d + 1) % 4;
		}
	}
	
	int res = 0;

	for (int x = -101; x <= 100; x++)
		for (int y = -101; y <= 100; y++) {
			int h = 0, v = 0;
			map<int, vi>::iterator ih = hor.find(x);
			if (ih == hor.end()) continue;
			vi& V = ih->second;
			for (int k = 0; k < V.size(); k++) if (V[k] <= y) h++;
			if (false) continue;

			map<int, vi>::iterator iv = ver.find(y);
			if (iv == ver.end()) continue;
			vi& H = iv->second;
			for (int k = 0; k < H.size(); k++) if (H[k] <= x) v++;
			if ((v == 0 || v == H.size() || (v & 1)) && (h == 0 || h == V.size() || (h & 1))) continue;
			res++;
		}

	cout << "Case #" << test <<": " << res << endl;

}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	cin >> T;
	for (test = 1; test <= T; test++)
		solve();
	return 0;
}