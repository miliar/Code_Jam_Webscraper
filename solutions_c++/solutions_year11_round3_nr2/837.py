#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int l, t, n, c;
int dis[1001001];

int a[1100001];

int main() {
	freopen("bbb.in", "r", stdin);
	freopen("out1.txt", "w", stdout);
	
	int tt, i, j, k, ii;
	int d;
	double result;
	scanf ("%d", &tt);
	
	for (ii = 1; ii <= tt; ++ii) {

		if (ii >= 1) {

			vector<int> dis2;
			result = 0;
			scanf ("%d%d%d%d", &l, &t, &n, &c);
			
			for (i = 0; i < c; ++i) {
			
				scanf ("%d", &d);
				for (k = 0; k * c + i + 1<= n; ++k) {
					dis[k * c + i + 1] = d;
				}
			}
			
			
			int tmp = 0;
			for (i = 1; i <= n; ++i) {
				tmp += dis[i] * 2;
				if (tmp >= t) {
					break;
				}
			}
			
			if (tmp < t) {
				for (i = 1; i <= n; ++i)
					result += dis[i] * 2;
			}
			
			else {
				result = t;
				
				dis[i] = (tmp - t) / 2;
				
				for (j = i; j <= n; ++j) {
					dis2.push_back(dis[j]);
				}
				
				sort(dis2.begin(), dis2.end());
				int len = dis2.size();
				
				for (i = 0; i < len - l; ++i) {
					result += dis2[i] * 2;
				}
				
				for (i = len - l; i < len; ++i) {
					result += dis2[i];
				}
			}
			printf("Case #%d: %.0lf\n", ii, result);
		}
	}
	return 0;
}

