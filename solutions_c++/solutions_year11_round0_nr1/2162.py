#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <ctime>
#define MAXN 103
using namespace std;
const int INF=0x3f3f3f3f;
const double eps=1e-9;
typedef long long LL;
typedef pair<int, int> pii;

pair<bool, int> data[MAXN];
int n;

int bfs() {
	vector<int> a, b;
	for(int i=0; i<n; ++i) {
		if(data[i].first)
			a.push_back( data[i].second );
		else
			b.push_back( data[i].second );
	}

	int pa=0, pb=0, p=0, ca=1, cb=1, key=0;
	while(p<n) {
		++key;
		if(data[p].first) {
			if(pa!=(int)a.size()) {
				if(ca==a[pa]) {
					++p;
					++pa;
				} else if(ca<a[pa])
					++ca;
				else if(ca>a[pa])
					--ca;
			}

			if(pb!=(int)b.size()) {
				if(cb<b[pb])
					++cb;
				else if(cb>b[pb])
					--cb;
			}
		} else {
			if(pb!=(int)b.size()) {
				if(cb==b[pb]) {
					++p;
					++pb;
				} else if(cb<b[pb])
					++cb;
				else if(cb>b[pb])
					--cb;
			}

			if(pa!=(int)a.size()) {
				if(ca<a[pa])
					++ca;
				else if(ca>a[pa])
					--ca;
			}
		}
	}
	return key;
}

int main() {
#ifndef ONLINE_JUDGE
//    freopen("in", "r", stdin);
//    freopen("out", "w", stdout);
#endif

    int dataset;
    char c;
    int pos;

    scanf("%d", &dataset);
    for(int cas=1; cas<=dataset; ++cas) {
    	scanf("%d", &n);
    	for(int i=0; i<n; ++i) {
    		scanf(" %c %d", &c, &pos);
    		data[i]=make_pair(c=='B', pos);
    	}
    	printf("Case #%d: %d\n", cas, bfs());
    }

    return 0;
}
