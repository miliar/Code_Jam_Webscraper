#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <sstream>
using namespace std;

char maze[111][111];
int win[111] , tot[111];
double wp[111] , owp[111] , oowp[111];
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas = 1 ; cas <= T ; cas ++) {
		int n;
		scanf("%d",&n);
		for (int i = 0 ; i < n ; i ++) {
			scanf("%s",maze[i]);
		}
		for (int i = 0 ; i < n ; i ++) {
			win[i] = tot[i] = 0;
			for (int j = 0 ; j < n ; j ++) {
				if (maze[i][j] == '.') continue;
				tot[i] ++;
				if (maze[i][j] == '1') win[i] ++;
			}
			if (tot[i] == 0) wp[i] = 0;
			else wp[i] = win[i] * 1.0 / tot[i];
		}
		for (int i = 0 ; i < n ; i ++) {
			owp[i] = 0;
			for (int j = 0 ; j < n ; j ++) {
				if (maze[j][i] == '0') {
					int tt = tot[j] - 1;
					int ww = win[j];
					if (tt == 0) owp[i] += 0;
					else owp[i] += ww * 1.0 / tt;
				} else if (maze[j][i] == '1') {
					int tt = tot[j] - 1;
					int ww = win[j] - 1;
					if (tt == 0) owp[i] += 0;
					else owp[i] += ww * 1.0 / tt;
				}
			}
			if (tot[i] != 0) owp[i] /= tot[i];
		}
		for (int i = 0 ; i < n ; i ++) {
			oowp[i] = 0;
			for (int j = 0 ; j < n ; j ++) {
				if (maze[i][j] != '.') {
					oowp[i] += owp[j];
				}
			}
			if (tot[i] != 0) oowp[i] /= tot[i];
		}
		printf("Case #%d:\n",cas);
		for (int i = 0 ; i < n ; i ++) {
			printf("%.10lf\n",0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}