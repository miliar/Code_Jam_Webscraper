//#define _CRT_SECURE_NO_DEPRECATE
//#pragma comment (linker, "/STACK:100000000")
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <cmath>

using namespace std;

//const int INF = 1000000000;
const int INF = 2147483647;
const double eps = 0.000000000001;
const double PI = 3.1415926535897932384626433832795;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) for (int i = 0; i < (int)v.size(); ++i)
#define pb push_back
#define mp make_pair
#define VI vector <int>

int n, na, nb, t;

struct eventt {
	int t, type;
};

eventt mev(int t, int type) {
	eventt tmp;
	tmp.t = t;
	tmp.type = type;
	return tmp;
}

bool operator < (eventt a, eventt b) {
	if (a.t != b.t) return a.t < b.t;
	return a.type < b.type;
}

vector <eventt> a;


int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	
	
	cin >> n;
	forn(i, n) {
		scanf("%d%d%d\n", &t, &na, &nb);
		a.clear();
		char ti1[10], ti2[10];
		forn(j, na) {
			scanf("%s %s\n", ti1, ti2);
			int vr1 = ((int)ti1[0] - '0') * 10 + ti1[1] - '0';
			vr1 *= 60;
			vr1 += ((int)ti1[3] - '0') * 10 + ti1[4] - '0';
			
			int vr2 = ((int)ti2[0] - '0') * 10 + ti2[1] - '0';
			vr2 *= 60;
			vr2 += ((int)ti2[3] - '0') * 10 + ti2[4] - '0';
			
			a.pb(mev(vr2 + t, 1));
			a.pb(mev(vr1, 2));
		}

		forn(j, nb) {
			scanf("%s %s\n", ti1, ti2);
			int vr1 = ((int)ti1[0] - '0') * 10 + ti1[1] - '0';
			vr1 *= 60;
			vr1 += ((int)ti1[3] - '0') * 10 + ti1[4] - '0';
			
			int vr2 = ((int)ti2[0] - '0') * 10 + ti2[1] - '0';
			vr2 *= 60;
			vr2 += ((int)ti2[3] - '0') * 10 + ti2[4] - '0';
			
			a.pb(mev(vr2 + t, 0));
			a.pb(mev(vr1, 3));
		}

		sort(a.begin(), a.end());

		int curA = 0, curB = 0;
		int ansA = 0, ansB = 0;
		forn(j, a.size()) {
			if (a[j].type == 0) curA++;
			if (a[j].type == 1) curB++;
			if (a[j].type == 2) {
				if (curA > 0) curA--; else ansA++;
			}
			if (a[j].type == 3) {
				if (curB > 0) curB--; else ansB++;
			}
		}
		
		
		printf("Case #%d: %d %d\n", i + 1, ansA, ansB);
	}


	return 0;
}

 
