#include <cstdio>
#include <cstdlib>
#include <string>
#include <set>
#include <queue>
#include <stack>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <memory.h>
#include <vector>
using namespace std;

class vine {
public:
	int pos;
	int len;
};
vector<vine> v;
int dd[110][110];
int solve(int idx, int cat) {
	if(dd[idx][cat] != -1) return dd[idx][cat];
	int sw = v[cat].pos - v[idx].pos;
	int ret = 0;
	if(sw > v[cat].len) sw = v[cat].len;
	for(int i=cat+1;i<v.size();i++) {
		if(v[i].pos - v[cat].pos > sw) break;
		if(i == v.size()-1) {
			ret = 1;
			break;
		}
		ret = solve(cat, i);
		if(ret) break;
	}
	dd[idx][cat] = ret;
	return ret;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int q=1;q<=T;q++ ) {
		int n;
		scanf("%d", &n);
		memset(dd, -1, sizeof(dd));
		v.clear();
		vine tt;
		tt.pos = 0;
		tt.len = 0;
		v.push_back(tt);
		for(int i=0;i<n;i++) {
			int d, l;
			scanf("%d %d", &d, &l);
			vine temp;
			temp.pos = d;
			temp.len = l;
			v.push_back(temp);
		}
		int dd;
		scanf("%d", &dd);
		if(v[1].pos > v[1].len) {
			printf("NO\n");
			continue;
		}
		printf("Case #%d: ", q);
		tt.pos = dd;
		v.push_back(tt);
		int ret = solve(0, 1);
		if(ret) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
