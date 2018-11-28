#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define FILEIO

const int MAXN = 10005;
int N;
int d[MAXN], l[MAXN], D;
int len[MAXN];
bool vst[MAXN];

bool solve(){
	priority_queue<pair<int, int> > pq;
	for(int i = 0;i < N; ++i) vst[i] = false;
	for(int i = 0;i < N; ++i){
		if(d[i] <= l[i] && i == 0) len[i] = d[i];
		else len[i] = 0;
		if(len[i] > 0){
			pq.push(make_pair(len[i],i));
			//printf("(%d, %d)\n", len[i], i);
			if(d[i] + len[i] >= D) return true;
		}
	}
	while(!pq.empty()){
		pair<int, int> cur = pq.top();
		pq.pop();
		int curlen = cur.first;
		int curv = cur.second;

		if(vst[curv]) continue;
		vst[curv] = true;
		
		int stpos = lower_bound(d, d + N, d[curv] - curlen) - d;
		int endpos = upper_bound(d, d + N, d[curv] + curlen) - d;
		//printf("%d - %d\n", stpos, endpos);
		for(int i = stpos; i < endpos; ++i){
			int nextlen = min(abs(d[curv] - d[i]), l[i]);
			if(nextlen > len[i]){
				len[i] = nextlen;
				pq.push(make_pair(nextlen, i));
				//printf("(%d, %d)\n", nextlen, i);
				if(d[i] + nextlen >= D) return true;
			}
		}
	}
	return false;
}
int main(){
#ifdef FILEIO
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int TT;
	scanf("%d", &TT);
	for(int cas = 1; cas <= TT; ++cas){
		scanf("%d", &N);
		for(int i = 0;i < N; ++i) scanf("%d %d", d + i, l + i);
		scanf("%d", &D);
		bool ans = solve();
		printf("Case #%d: %s\n", cas, (ans ? "YES": "NO"));
	}
	return 0;
}
