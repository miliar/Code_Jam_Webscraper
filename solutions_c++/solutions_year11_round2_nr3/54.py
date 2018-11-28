#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <sstream>
using namespace std;

const int maxn = 2222;
int N , M;
int s[maxn] , e[maxn];

vector < vector<int> > vec;
int MAX;
int ans[maxn];
int temp[maxn];
bool have[maxn];
bool has[maxn];
bool hash[maxn];

void check() {
	memset(have , false , sizeof(have));
	for (int i = 1 ; i <= N ; i ++) {
		have[ temp[i] ] = true;
	}

	for (int i = 0 ; i < vec.size() ; i ++) {
		memset(has , false , sizeof(has));
		for (int j = 0 ; j < vec[i].size() ; j ++) {
			has[ temp[ vec[i][j] ] ] = true;
		}
		for (int j = 1 ; j <= 5 ; j ++) {
			if (have[j] && !has[j]) return ;
		}
	}


	int tot = 0;
	for (int j = 1 ; j <= 5 ; j ++) {
		if (have[j]) tot ++;
	}
	if (tot > MAX) {
		MAX = tot;
		for (int i = 1 ; i <= N ; i ++) {
			ans[i] = temp[i];
		}
	}
}
void dfs(int x) {
	if (x > N) {
		check();
		return ;
	}
	for (int i = 1 ; i <= 5 ; i ++) {
		temp[x] = i;
		dfs(x + 1);
	}
}

void divide() {
	memset(hash , false , sizeof(hash));
	vec.clear();
	for (int dis = 1 ; dis <= N ; dis ++) {
		
		for (int i = 0 ; i < M ; i ++) {
			if (s[i] + dis == e[i]) {
				vector <int> vv;
				vv.push_back(s[i]);
				vv.push_back(e[i]);
				for (int j = s[i] + 1 ; j < e[i] ; j ++) {
					if (hash[j]) continue;
					hash[j] = true;
					vv.push_back(j);
				}
				vec.push_back(vv);
			}
		}
		
	}
	vector <int> vv;
	for (int i = 1 ; i <= N ; i ++) {
		if (!hash[i]) vv.push_back(i);
	}
	vec.push_back(vv);

	return ;
	for (int i = 0 ; i < vec.size() ; i ++) {
		for (int j = 0 ; j < vec[i].size() ; j ++) {
			printf("%d ",vec[i][j]);
		}
		puts("");
	}
}
int main() {
	freopen("C-small-attempt2.in","r",stdin);
	freopen("C-small-attempt2.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas = 1 ; cas <= T ; cas ++) {
		
		scanf("%d%d",&N,&M);
		for (int i = 0 ; i < M ; i ++) scanf("%d",&s[i]);
		for (int i = 0 ; i < M ; i ++) scanf("%d",&e[i]);

		divide();
		MAX = 0;
		dfs(1);
		printf("Case #%d: %d\n" , cas , MAX);
		for (int i = 1 ; i <= N ; i ++) {
			if (i != 1) printf(" ");
			printf("%d",ans[i]);
		}
		puts("");
	}
	return 0;
}