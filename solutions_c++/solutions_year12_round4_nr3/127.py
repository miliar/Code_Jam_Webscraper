#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll;
int peak[2011];
double ans[2011];

ll denom = 1;
ll gcd(ll a, ll b) {
	while (a && b) a %= b, swap(a, b);
	return a? a: b;
}
ll lcm(ll a, ll b) {
	return a / gcd(a, b) * b;
}

bool fail = false;
void go(int st, int end, double maxs, int cpx, int cpy) {
	if (st >= end) return;
	// we need to be lower than mdy / mdx
	// but also make sure we override the current peak
	for (int i = st+1; i < peak[st]; i++) {
		if (peak[i] > peak[st]) {
			fail = true;
			return;
		}
	}
	double mins = double(cpy - ans[st]) / (cpx - st);
	int md = (cpx-st) / gcd(cpy-ans[st], cpx-st);
	double mid = mins;
	if (mins < 0) {
		mid = 0;
		md = 1;
	}
	if (peak[st] > end) {
		ans[st+1] = ans[st] - 1;
		go(st+1, end, 1, cpx, cpy);
	} else {
		ans[st+1] = ans[st] - 1;
		ans[peak[st]] = ans[st] + (peak[st] - st) * mid;
		denom = lcm(denom, md/gcd(peak[st]-st, md));
		go(st+1, peak[st]-1, 1, peak[st], ans[peak[st]]);
		go(peak[st], end, mid, cpx, cpy);
	}
}

int main()
{
	int T; cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		int N; cin >> N;
		for (int i = 0; i < N-1; i++) {
			cin >> peak[i], peak[i]--;
		}

		fail = false;
		ans[0] = 0;
		go(0, N-1, 1, N+1, 0);
		printf("Case #%d:", ti);
		if (fail) {
			puts(" Impossible");
		} else {
			double m = 0;
			for (int i = 0; i < N; i++) {
				m = min(m, ans[i]);
			}
			for (int i = 0; i < N; i++) {
				cout << " " <<  (ans[i]-m+1) * denom;
			}
			cout << endl;
		}
	}
}
