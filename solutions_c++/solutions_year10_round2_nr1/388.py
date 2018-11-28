#include <iostream>
#include <vector>
#include <string>
using namespace std;
char key[1024];
int min(int a, int b) {
	return a<b?a:b;
}
vector<vector<string> > v;
int main() {
	int T;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d",&T);
	int b;
	vector<string> x;
	for (b = 1; b <= T; ++b) {
		int N,M;
		scanf("%d%d",&N, &M);
		int i,j,k;
		v.clear();
		x.clear();
		for (i=0;i<N;++i) {
			scanf("%s",key);
			string tp;
			tp.erase();
			for (j=0;key[j] !='\0';++j) {
				if (key[j] != '/') {
					tp = tp + key[j];
				} else {
					if (!tp.empty()) {
						x.push_back(tp);
					}
					tp.erase();
				}
			}
			if (!tp.empty()) {
				x.push_back(tp);
				tp.erase();
			}
			if (!x.empty()) {
				v.push_back(x);
			}
			x.clear();
		}

		x.clear();
		int ans = 0;
		for (i=0;i<M; ++i) {
			scanf("%s",key);
			string tp;
			for (j=0;key[j] !='\0';++j) {
				if (key[j] != '/') {
					tp = tp + key[j];
				} else {
					if (!tp.empty()) {
						x.push_back(tp);
					}
					tp.erase();
				}
			}
			if (!tp.empty()) {
				x.push_back(tp);
				tp.erase();
			}
			
			int ret = x.size();
			for (j = 0;j < v.size(); ++j) {
				for (k=0;k<v[j].size() && k<x.size();++k) {
					if (x[k] != v[j][k]) {
						break;
					}
				}
				ret = min(ret, x.size() - k);
			}
			if (ret != 0) {
				v.push_back(x);
			}
			ans+=ret;
			x.clear();
		}
		printf("Case #%d: ", b);
		printf("%d\n",ans);
	}
	return 0;
}