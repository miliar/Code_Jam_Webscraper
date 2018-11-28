#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, K;

typedef long long ll;

int price[100][25];
bool inter[100][100];
int color[100];
int best = 100;

void solve(int in, int co) {
	int i;
	bool col[co+1];
	if (in == N) {
		if (best > co+1) best = co+1;
		return;
	}
	for (i=0; i<=co; i++) col[i] = 0;
	for (i=0; i<in; i++) {
		if (inter[in][i]) {
			col[color[i]] = 1;
		}
	}
	bool good = 0;
	for (i=0; i<=co; i++) {
		if (!col[i]) {
			good = 1;
			color[in] = i;
			solve(in+1, co);
			color[in] = -1;
		}
	}
	if (!good) {
		color[in] = co+1;
		solve(in+1, co+1);
		color[in] = -1;
	}
}

vector<pair<int, int> > v;

int main () {
	int T, i, j, k, cse=0;
	cin >> T;
	while (T--) {
		cin >> N >> K;
		best = 100;
		v.clear();
		for (i=0; i<N; i++) {
			for (j=0; j<K; j++) {
				cin >> price[i][j];
			}
			v.push_back(make_pair(price[i][0], i));
		}
		sort(v.begin(), v.end());
		for (i=0; i<N; i++) {
			color[i] = -1;
			for (j=0; j<N; j++) {
				inter[i][j] = inter[j][i]= 0;
				ll t = price[v[i].second][0] - price[v[j].second][0];
				for (k=1; k<K; k++) {
					ll s = price[v[i].second][k] - price[v[j].second][k];	
					if (t * s <= 0) {
						inter[i][j] = inter[j][i]= 1;
						break;
					}
				}
			}
		}
		solve(0, 0);
		cerr << cse << endl;
		cout << "Case #" << ++cse << ": " << best << endl;
	}
	return 0;
}
