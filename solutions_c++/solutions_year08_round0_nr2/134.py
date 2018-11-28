#include <cstdio>
#include <cassert>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

typedef pair<int,int> pii;

int main() {
	int N;
	scanf("%d", &N);
	for (int z=1;z<=N;++z) {
		int T;
		scanf("%d", &T);
		int NA,NB;
		scanf("%d %d", &NA, &NB);
		vector<pair<pii,int> > events;
		for (int i=0;i<NA;++i) {
			int hs,ms,he,me;
			scanf("%d:%d %d:%d", &hs, &ms, &he, &me);
			int start = hs*60 + ms;
			int end =   he*60 + me + T;
			assert(start<end);
			events.push_back(make_pair(pii(start,end),0));
		}
		for (int i=0;i<NB;++i) {
			int hs,ms,he,me;
			scanf("%d:%d %d:%d", &hs, &ms, &he, &me);
			int start = hs*60 + ms;
			int end =   he*60 + me + T;
			assert(start<end);
			events.push_back(make_pair(pii(start,end),1));
		}
		sort(events.begin(),events.end());
		int ansA=0,ansB=0;
		priority_queue<int,vector<int>, greater<int> > pA,pB;
		for (int i=0;i<events.size();++i) {
			int start = events[i].first.first;
			int end = events[i].first.second;
			if (events[i].second==0) { // Departure from A
				if (!pA.empty() && pA.top()<=start) pA.pop();
				else ++ansA;
				pB.push(end);
			}
			else { // Departure from B
				if (!pB.empty() && pB.top()<=start) pB.pop();
				else ++ansB;
				pA.push(end);
			}
		}
		printf("Case #%d: %d %d\n", z, ansA, ansB);
	}
}
