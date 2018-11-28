#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <cctype>
#include <functional>
using namespace std;

typedef pair<int, int> PII;

int main()
{
	freopen("G:\\A-large.in", "r", stdin);
	freopen("G:\\A-large.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		int n;
		scanf("%d", &n);
		vector<PII> button;
		button.push_back(PII(0, 0));
		for(int i = 0; i < n; i++) {
			char c;
			int pos;
			scanf("\n%c %d", &c, &pos);
			button.push_back(PII(pos-1, c == 'O' ? 1 : -1));
		}
		
		int time = 0, btime = 0, rtime = 0;
		int bi = 0, oi = 0;
		for(int i = 1; i < button.size(); i++) {
			if(button[i].second > 0) {
				// orange
				int dis = abs( button[oi].first - button[i].first );
				time = rtime = max(rtime + dis, time) + 1;
				oi = i;
			} else {
				// blue
				int dis = abs( button[bi].first - button[i].first );
				time = btime = max(btime + dis, time) + 1;
				bi = i;
			}
		}
		printf("Case #%d: %d\n", t+1, time);
	}
	
	return 0;
}
