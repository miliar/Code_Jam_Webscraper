#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
#define sz 10010

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };

bool isCycle(int N, int M) {
	stringstream ss1, ss2;
	ss1 << N;
	ss2 << M;
	string n, m;
	ss1 >> n;
	ss2 >> m;
	if (n.size() != m.size())
		return false;
	for (int i = 0; i < (int) n.size(); ++i) {
		if (n[i] == m[0]) {
			if (n.substr(i) + n.substr(0, i) == m)
				return true;
		}
	}
	return false;
}

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int T, a, b;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> a >> b;
		int numC = 0;
		for (int i = a; i <= b; ++i) {
			for (int j = i + 1; j <= b; ++j) {
				numC += isCycle(i, j);
			}
		}
		printf("Case #%d: %d\n", t + 1, numC);
	}

	return 0;
}
