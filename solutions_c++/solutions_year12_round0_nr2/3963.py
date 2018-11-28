#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

int main() {
	int t; scanf("%d", &t);
	for(int tc = 1; tc <= t; tc++) {
		int n, s, p;
		scanf("%d%d%d", &n, &s, &p);
		vector<int> A(n);
		for(int i = 0; i < n; i++) scanf("%d", &A[i]);
		sort(A.begin(), A.end());
		int ans = 0;
		int tmp;
		for(int i = n-1; i >= 0; i--) {
			tmp = A[i]/3;
			if(tmp<p) {
				if(A[i]%3 == 1) {
					if(tmp + 1 >= p) {
						ans++;
					}
				}
				else if(A[i]%3 == 2) {
					if(tmp + 1 >= p) {
						ans++;
					}
					else if(tmp + 2 >= p && s) {
						ans++;
						s--;
					}
				}
				else {
					if(tmp + 1 >= p && s && tmp>0) {
						ans++;
						s--;
					}
				}
			}
			else {
				ans++;
			}
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
