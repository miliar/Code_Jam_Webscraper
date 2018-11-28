#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;
#define inf 1000000000
#define ll long long
#define eps 1e-9
#define VI vector<int>
#define pb push_back
#define L(s) (int)((s).size())
#define all(s) (s).begin(), (s).end()
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
pair<pair<int, double>, int> a[1111];
int n, t;
inline bool by(const pair<pair<int, double>, int> &a, const pair<pair<int, double>, int> &b) {
	double v1 = ((1 - a.x.y) * (1 - b.x.y) * (a.x.x + b.x.x) + (1 - a.x.y) * b.x.y * a.x.x) / (1 - a.x.y - (1 - a.x.y) * b.x.y);
//	double v1 = a.x.x / (1. - a.x.y);
//	double v2 = b.x.x / (1. - b.x.y);
	double v2 = ((1 - a.x.y) * (1 - b.x.y) * (a.x.x + b.x.x) + (1 - b.x.y) * a.x.y * b.x.x) / (1 - b.x.y - (1 - b.x.y) * a.x.y);
	if (abs(v1 - v2) < 1e-9) {
		return a.y < b.y;
	} else return v1 < v2;
}
int main() {
	freopen("A-small-attempt1.in", "r", stdin);
//	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tn = 1; tn <= t; ++tn) {
		cin >> n;
		for(int i = 0; i < n; ++i) {
			cin >> a[i].x.x;
			a[i].y = i;
		}
		for(int i = 0; i < n; ++i) {
			cin >> a[i].x.y;
			a[i].x.y /= 100.;
		}
		sort(a, a + n, by);
		cout << "Case #" << tn << ":";
		for(int i = 0; i < n; ++i) cout << " " << a[i].y;
		cout << endl;
	}
}