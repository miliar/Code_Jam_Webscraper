#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <sstream>
using namespace std;

typedef pair<long long,long long> PII;
typedef vector<int> VI;
typedef stack<int> STI;
typedef set<int> SI;
typedef queue<int> QI;
typedef vector<PII > VPII;
typedef stack<PII > STPII;
typedef set<PII > SPII;
typedef queue<PII > QPII;

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t) {
		int n;
		long long A,B,C,D,X,Y,M;
		scanf("%d %lld %lld %lld %lld %lld %lld %lld", &n,&A,&B,&C,&D,&X,&Y,&M);
		VPII trees;
		trees.push_back(PII(X,Y));
		for(int i = 0; i < n-1; ++i) {
			X = (A*X+B)%M;
			Y = (C*Y+D)%M;
			trees.push_back(PII(X,Y));
		}

		int count = 0;
		for(int i = 0; i < (int)trees.size(); ++i)
			for(int j = i+1; j < (int)trees.size(); ++j)
				for(int k = j+1; k < (int)trees.size(); ++k)
					if((trees[i].first+trees[j].first+trees[k].first)%3 == 0 && (trees[i].second+trees[j].second+trees[k].second)%3 == 0)
						count++;

		printf("Case #%d: %d\n", t, count);
	}
	return 0;
}
