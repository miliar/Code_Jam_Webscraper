/*
 TASK:B
 LANG:C++
 Muhammad Magdi Muhammad
 Email: moh_magdi@acm.org
 */
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>

#define all(v)          v.begin(),v.end()
#define allr(v)         v.rbegin(),v.rend()
#define rep(i,m)        for(int i=0;i<(int)m;i++)
#define REP(i,k,m)      for(int i=k;i<(int)m;i++)
#define mem(a,b)        memset(a,b,sizeof(a))
#define mp              make_pair
#define pb              push_back
#define OO ((int)1e9)
#define MAX 100000

typedef long long ll;

int diri[] = { -1, 0, 1, 0, -1, 1, 1, -1 };
int dirj[] = { 0, 1, 0, -1, 1, 1, -1, -1 };
int compare(double d1, double d2) {
	if (fabs(d1 - d2) < 1e-9)
		return 0;
	if (d1 < d2)
		return -1;
	return 1;
}
int I, J;
inline bool valid(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

using namespace std;

#define SMALL
#define LARGE
int T;

int n, p;
int arr[101];
int sv[101][101];
int dp(int i, int s) {
	if (i == n && s == 0)
		return 0;
	if (i >= n || s < 0)
		return -1e9;
	int &x = sv[i][s];
	if (x != -1)
		return x;
	x = 0;
	rep(a,arr[i]+1) {
		REP(b,max(0,a-2),min(arr[i]-a,a+2)+1) {
			int c = arr[i] - a - b;
			if (abs(a - c) > 2 || abs(b - c) > 2 )
				continue;
			bool isSur = (max(abs(a - c), max(abs(a - b), abs(b - c))) == 2);
			int mx = max(a, max(b, c));
			x = max(x, dp(i + 1, s - isSur) + (mx >= p));
		}
	}
	return x;
}
int main() {

	freopen("1.in", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
#endif

	cin >> T;
	int s;
	rep(tt,T) {
		printf("Case #%d: ", tt + 1);
		cin >> n >> s >> p;
		rep(i,n) {
			cin >> arr[i];
		}
		mem(sv, -1);
		printf("%d\n", dp(0, s));
		cerr << tt << endl;
	}
	return 0;
}
//end

