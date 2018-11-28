#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
const int N = 50;
int n, a[N];
int main() {
	int cas, cass = 0;
	freopen("output.txt", "w", stdout);
	for (scanf("%d", &cas); cas--;) {
		scanf("%d", &n);
		for (int i=0; i<n; ++i) {
			char s[N];
			scanf("%s", s);
			a[i] = -1;
			for (int j=n-1; j>=0; --j) {
				if (s[j]=='1') {
					a[i] = j;
					break;
				}
			}
		}
		int res = 0;
		for (int i=0; i<n; ++i) {
			if (a[i]>i) {
				for (int j=i+1; j<n; ++j) {
					if (a[j]<=i) {
						for (int k=j; k>i; --k) {
							swap(a[k], a[k-1]);
							++res;
						}
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n", ++cass, res);
	}
	return 0;
}