#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <string>
#include <vector>

using namespace std;
   
int a[1024];
int cost[1024];
int next[1024];

int main(){	
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int ktest;
	
	scanf("%d", &ktest);
	
	for (int itest=0; itest<ktest; ++itest){
		printf("Case #%d: ", itest+1);
		int r, k, n;
		scanf("%d%d%d", &r, &k, &n);
		for (int i=0; i<n; ++i){
			scanf("%d", &a[i]);		
			cost[i] = 0;
		}
		for (int i=0; i<n; ++i){
			int s = k, t = 0;
			for (int j=i; ; ++j){
				++t;
				if (t == n+1){
					next[i] = i;
					break;
				}
				if (j >= n)
					j -= n;
				if (s >= a[j]){
					s -= a[j];
					cost[i] += a[j];
				}
				else{
					next[i] = j;
					break;
				}
			}		
		}
		
		int cur = 0;
		__int64 ans = 0;
		for (int i=0; i<r; ++i){
			ans += cost[cur];
			cur = next[cur];	
		}

		printf("%lld\n", ans);
	}	

    return 0;
}