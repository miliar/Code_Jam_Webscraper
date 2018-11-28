#include <iostream>
#include <string>
#include <map> 
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>


using namespace std;

#define sqr(x) ((x)*(x))
#define PB(a) push_back(a)
#define MP(a) make_pair(a)
#define ll long long

int gcd(int a, int b) {
	while (b) b^=a^=b^=a%=b;
	return a;
}

const int maxn=100100;

int n,w,l;
pair<int,int> r[maxn];
pair<int,int> ans[maxn];

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	//cout.precision(1);
	//cout << fixed;

	int tests;
	cin >> tests;
	for (int test=0; test<tests; test++) {
		cin >> n >> w >> l;
		for (int i=0; i<n; i++) {
			cin >> r[i].first;
			r[i].second=i;
		}
		sort(r,r+n);
		reverse(r,r+n);

		int cury=0,curx=0,curr=r[0].first;
		for (int i=0; i<n; i++) {
			if (cury!=0) cury+=r[i].first;
			if (cury>l) {
				curx+=curr+r[i].first;
				cury=0;
				curr=r[i].first;
			}
			ans[r[i].second]=make_pair(curx,cury);
			cury+=r[i].first;
		}

		cout << "Case #" << test+1 << ": ";
		for (int i=0; i<n; i++) cout << ans[i].first << ' ' << ans[i].second << ' ';
		cout << endl;
	}

	return 0;
}