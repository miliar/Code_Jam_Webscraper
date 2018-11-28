#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

pair<int, int> r[2000];
int x[2000];
int y[2000];

int main(){
	int tc, tcn, n, W, H;
	scanf("%d", &tcn);
	for(tc=0; tc<tcn; ++tc){
		scanf("%d %d %d", &n, &W, &H);
		for(int i=0; i<n; ++i){
			scanf("%d", &r[i].first);
			r[i].second = i;
		}
		sort(r, r+n);
		reverse(r, r+n);

		x[r[0].second] = y[r[0].second] = 0;

		int bX = r[0].first;
		int lX = r[0].first;
		int cX = 0;
		int l = 0;
		int nl = r[0].first;
		
		for(int i=1; i<n; ++i){
			if(l + r[i].first <= H && lX + 2*r[i].first <= bX && lX + r[i].first < W){
				y[r[i].second] = l + r[i].first;
				x[r[i].second] = lX + r[i].first;
				lX += 2*r[i].first;
			} else if(nl + r[i].first <= H){
				l = nl;
				nl = l + 2*r[i].first;
				y[r[i].second] = l + r[i].first;
				x[r[i].second] = cX;
				lX = cX + r[i].first;
			} else {
				cX = bX + r[i].first;
				l = 0;
				nl = r[i].first;
				bX = cX + r[i].first;
				lX = bX;
				y[r[i].second] = 0;
				x[r[i].second] = cX;
			}
		}
		printf("Case #%d:", tc+1);
		for(int i=0; i<n; ++i){
			printf(" %d %d", x[i], y[i]);
			if(x[i] > W)
				fprintf(stderr, "grr X %d\n", tc+1);
			if(y[i] > H)
				fprintf(stderr, "grr Y %d\n", tc+1);
		}
		puts("");
	}
}
