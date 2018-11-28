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

int n;
double sum;
int v[201];

int canFit(double sharePoint) {
	double cnt = 0.0;
	for (int i = 0; i < n; i++) {
		if (sharePoint > v[i])
			cnt += (sharePoint - v[i]) / sum;
	}
	if (cnt >= 1.0)
		return false;
	return true;
}

double BS(double st, double en) {
	if (fabs(st - en) < 1e-9)
		return st;
	double mid = (st + en) / 2.0;
	if (canFit(mid))
		return BS(mid, en);
	return BS(st, mid);
}

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> n;
		sum = 0;
		for (int i = 0; i < n; ++i) {
			cin >> v[i];
			sum += v[i];
		}
		double sharePoint = BS(0.0, 20001.0);
		printf("Case #%i:",t+1);
		for (int i = 0; i < n; i++) {
			if (sharePoint > v[i])
				printf(" %f", (100.0 * (sharePoint - v[i]) / sum));
			else
				printf(" %f", 0.0);
		}
		printf("\n");
	}
	return 0;
}
