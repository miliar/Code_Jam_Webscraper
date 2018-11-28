#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;

const int maxn = 500;

int n, maxx, maxy, total;
bool s[maxn][maxn];

void init() {
	cin >> n;
	int x1, x2, y1, y2;	
	maxx = maxy = 0;
	total = 0;
	for (int i = 0; i < n; i++) {
		 cin >> x1 >> y1 >> x2 >> y2;
		 for (int i = x1; i <= x2; i++)
			 for (int j = y1; j <= y2; j++) {
				s[i][j] = true;
				total++;
			}
		if (x2 > maxx) maxx = x2;
		if (y2 > maxy) maxy = y2;
	}		 			
}

int work() {
	int res = 0;
	for (res = 0; total > 0; res++) {
		total = 0;
		if (maxx == maxn) cout << "Error " << maxx << endl;
		for (int i = maxx+1; i > 0; i--) {
			for (int j = maxy+1; j > 0; j--) {
				int now = s[i-1][j] + s[i][j-1];
				if (s[i][j] && now == 0) s[i][j] = false;
				if (!s[i][j] && now == 2) s[i][j] = true;
				if (s[i][j]) {
					if (i > maxx) maxx = i;
					if (j > maxy) maxy = j;
					total++;
				}				
			}
		}	
	}
	return res;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		init();
		cout << "Case #" << t + 1 << ": " << work() << endl;
	}
	return 0;
}
