#include<cstdio>
#include<iostream>
using namespace std;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t, n, s, p, i, j, cnt, p1, p2;
	int ti;
	cin >> t;
	for(i = 1; i <= t; i++) {
		cnt = 0;
		cin >> n >> s >> p;
		for(j = 0; j < n; j++) {
			cin >> ti;
			p1 = 2 * (p - 1) + p;
			p2 = 2 * (p - 2) + p;
			if(p1 < 0) p1 = 0;
			if(p2 < 0) p2 = 0;
			if(ti >= p1) cnt++;
			else{
				if(ti >= p2 && s != 0 && ti != 0 && ti != 1){
					cnt++;
					s--;
				}
			}
		}
		cout << "Case #" << i << ": " << cnt << endl;
	}
	return 0;
}