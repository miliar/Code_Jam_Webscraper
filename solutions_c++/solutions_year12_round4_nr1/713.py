#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <stack>
#include <vector>

#define mp make_pair
#define pb push_back

#define REP(i,n) for(int i=0; i < (n); ++i)

using namespace std;

typedef long long ll;
typedef pair<int, int> pi;

int n;
int D;
int d[11000];
int l[11000];

int dy[11000];

void solve()
{
	cin >> n;
	REP(i,n) {
		cin >> d[i] >> l[i];
	}
	cin >> D;

	REP(i,n) dy[i] = -1;

	dy[0] = 0;

	REP(i,n) {
		if(dy[i] == -1) continue;

		int max_root = d[i] - dy[i];
		if(max_root > l[i]) max_root = l[i];

		max_root += d[i];

		if(max_root >= D) {
			cout << "YES" << endl;
			return;
		}

		for(int j = i+1; j < n; ++j) {
			if(d[j] > max_root) break;
			else {
				if(dy[j] == -1 || dy[j] > d[i]) dy[j] = d[i];
			}
		}
	}
	cout << "NO" << endl;

}

int main(int argc, char *argv[])
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

