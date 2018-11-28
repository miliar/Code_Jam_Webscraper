#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <cctype>
#include <functional>
#include <numeric>
using namespace std;

typedef pair<int, int> PII;

const int N = 1024, M = 1<<20;

int n, c[N], vst[M];

int go(int* c, int n, int t)
{
	int xsum = 0;
	for(int i = 0; i < n; i++) xsum ^= c[i];
	if(xsum != 0) return -1;
	
	priority_queue< PII, vector<PII>, greater<PII> > Q;
	Q.push(PII(0, 0));
	while(!Q.empty()) {
		PII p = Q.top(); Q.pop();
		int val = p.first, id = p.second;
		
		if(vst[id] == t) continue;
		if(val != 0) vst[id] = t;
		if(val != 0 && (id^id) == 0) return val;
		
		for(int i = 0; i < n; i++) {
			int nxt = id ^ c[i];
			if(vst[nxt] == t) continue;
			Q.push(PII(val+c[i], nxt));
		}
	}
	
	return -1;
}

int main()
{
	freopen("G:\\C-large.in", "r", stdin);
	freopen("G:\\C.out", "w", stdout);
	
	memset(vst, -1, sizeof(vst));
	
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		scanf("%d", &n);
		for(int i = 0; i < n; i++) {
			scanf("%d", &c[i]);
		}
		int sum = accumulate(c, c+n, 0);
		int other = go(c, n, t);
		printf("Case #%d: ", t+1);
		if(other < 0) printf("NO\n");
		else printf("%d\n", sum-other);
	}
	
	return 0;
}
