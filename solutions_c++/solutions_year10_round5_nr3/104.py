#include<iostream>
#include<cstring>
#include<vector>
#include<set>
#include<algorithm>
#include<vector>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef set<int> si;
typedef si::iterator sitr;

int C, N;

ii data[300];
ll ans;

const int RNG = 1000000;
const int OFF = RNG;
int hold[4*RNG+1];

// inv prev[i].second < prev[i+1].first
vector<ii> prev;

void debug() {
	for(int i = 0; i < prev.size(); ++i) {
		cout << "(" << prev[i].first << "," << prev[i].second << ") ";
	}
	cout << endl;
}

void run(const int& x) {
	if(prev.size() == 0) {
		prev.push_back(ii(x, x));
		return;
	}
	ii& b = prev.back();
	if(b.second + 1 == x) {
		b.second = x;
		return;
	}
	if(b.second < x) {
		prev.push_back(ii(x, x));
		return;
	}
	if(b.second == x) {
		ii tmp = b;
		prev.pop_back();
		run(tmp.first - 1);
		ans += tmp.second - tmp.first + 1;
		if(prev.back().second == tmp.first) {
			cerr << "should not reach here" << endl;
		}
		if(prev.back().second == tmp.first + 1) {
			prev.back().second = tmp.second + 1;
		} else {
			tmp.first += 1;
			tmp.second += 1;
			prev.push_back(tmp);
		}
		return;
	}
	cerr << "ERROR: should never reach here!" << endl;
}

int main() {
	int T; cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		prev.clear();
		cin >> C;
		ans = 0;
		N = 0;
		memset(hold, 0, sizeof(hold));
		for(int c = 0; c < C; ++c) {
			int p, v;
			cin >> p >> v;
			N += v;
			data[c] = ii(p, v);
			hold[p+OFF] = v;
		}
		sort(data, data + C);
		for(int x = -RNG; x <= 2*RNG; ++x) {
			if(hold[x+OFF] == 0) continue;
			//cout << " x=" << x << " ans=" << ans << endl;
			for(int k = 0; k < hold[x+OFF]; ++k) {
				run(x);
				if (prev.size() > 0 && prev.back().second > x) {
					if(prev.back().first == prev.back().second) {
						prev.pop_back();
					} else {
						prev.back().second--;
					}
					++hold[x+1+OFF];
				}
				//debug();
			}
		}
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}

