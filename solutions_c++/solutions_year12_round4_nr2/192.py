#define _CRT_SECURE_NO_DEPRECATE
#define _ASSERTE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin,a.end()
#define ll long long
#define INF 1e9
#define EPS 1e-8

int d[10345], l[10345];
int can[10345];

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	
	forn(tt, t){
		int n, W, L;
		
		cin >> n >> W >> L;
		pii r[1234], p[1234];
		forn(i, n){
			cin >> r[i].first;
			r[i].second = i;
		}
		sort(r, r + n);
		reverse(r, r + n);

cout << "Case #" << (tt + 1) << ":";
int x = r[0].first;

if (L > W) {
	int y = 0;
	int get = r[0].first;
	int st = 0;
	p[r[0].second] = mp (0, y);
	fore(i, 1, n) {
		int ii = r[i].second;
		if (get + r[i].first > W) {
			y += r[st].first + r[i].first;
			st = i;
			get = r[st].first;
			p[ii] = mp(0, y);
		}else {
			p[ii] = mp(get + r[i].first, y);
			get += 2 * r[i].first;
		}
	}
}else{
	int x = 0;
	int get = r[0].first;
	int st = 0;
	p[r[0].second] = mp (x, 0);
	fore(i, 1, n) {
		int ii = r[i].second;
		if (get + r[i].first > L) {
			x += r[st].first + r[i].first;
			st = i;
			get = r[st].first;
			p[ii] = mp(x, 0);
		}else {
			p[ii] = mp(x, get + r[i].first);
			get += 2 * r[i].first;
		}
	}
}

/*
if (L > W) {
	int y = 0;
	forn(i, n) {
		if (i == 0){
			p[r[i].second] = mp(0, 0);continue;
		}
		if (x + r[i].first > L){
			x = L + r[i].first;
			y = W;
		}
		if (y == W){
			p[r[i].second] = mp(y, x - r[i].first);
			x -= 2 * r[i].first;
		}else{
			p[r[i].second] = mp(y, x + r[i].first);
			x += 2 * r[i].first;
		}
	}
}else{
	forn(i, n) {
		int y = 0;
		if (i == 0){
			p[r[i].second] = mp(0, 0);continue;
		}
		if (x + r[i].first > W){
			x = W + r[i].first;
			y = L;
		}
		if (y == L){
			p[r[i].second] = mp(x - r[i].first, y);
			x -= 2 * r[i].first;
		}else{
			p[r[i].second] = mp(x + r[i].first, y);
			x += 2 * r[i].first;
		}
	}
}
*/

forn(i, n)
cout << " " << p[i].first << " " << p[i].second;


/*
forn(i, n) {
	forn(j, i) {
		int jj = r[j].second;
		int ii = r[i].second;

		if (hypot(p[ii].first - p[jj].first, p[ii].second - p[jj].second) + 0.001 < r[i].first + r[j].first) {
			cerr << hypot(p[ii].first - p[jj].first, p[ii].second - p[jj].second) << " " << 
				r[i].first + r[j].first << " " << "Test " << (tt + 1) << 
				": error in " << (ii+1) << " and " << (jj+1) << endl;
		}
	}
}
*/

puts("");
/*
		cerr << tt + 1 << endl;
			
		int n;
		cin >> n;
		forn(i, n)
			scanf("%d %d", &d[i], &l[i]);

		memset(can, 0, sizeof can);

		can[0] = d[0];
		l[n] = 1;
		scanf("%d", &d[n]);
		forn(i, n) {
			if (can[i]) {
				for(int j = i + 1; j <= n; j++) {
					if (d[j] - d[i] > can[i]) break;
					can[j] = max(can[j], min(l[j], d[j] - d[i]));
				}
			}
		}

		cout << "Case #" << (tt + 1) << ": " << (can[n] ? "YES\n" : "NO\n");
*/		
	}
	
	return 0;
}