//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define F first
#define S second

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_N = 400 + 10;

int n;
vector<int> list[MAX_N];

void input(){
	int m;
	scanf("%d %d", &n, &m);
	FOR(i, n)
		list[i].clear();
	FOR(i, m){
		int u, v;
		scanf("%d,%d", &u, &v);
		list[u].PB(v);
		list[v].PB(u);
	}
}

int dis[MAX_N];
int que[MAX_N];

void bfs(int s){
	dis[s] = 0;
	int head = 0, tail = 1;
	que[0] = s;
	while(head < tail){
		int v = que[head++];
		FOR(i, SZ(list[v])){
			int u = list[v][i];
			if(dis[u] == -1){
				dis[u] = dis[v] + 1;
				que[tail++] = u;
			}
		}
	}
}

int s, t;
map<joft, int> dp;
bool mark[MAX_N];

int mset(int v, int len){
	int ret = 0;
	FOR(i, SZ(list[v])){
		int u = list[v][i];
		if(dis[u] == len && !mark[u]++)
			ret++;
	}
	return ret;
}

int cal(int u, int v){
	if(v == s)
		return 0;
	
	if(dp.find(joft(u, v)) != dp.end())
		return dp[joft(u, v)];
	
	int ret = 0;
	FOR(i, SZ(list[v])){
		int z = list[v][i];
		if(dis[z] + 1 != dis[v])
			continue;
		int cur = cal(v, z);
		memset(mark, 0, sizeof mark);
		cur += mset(z, dis[v]);
		cur += mset(u, dis[v]);
		cur += mset(v, dis[v]);
		cur--;
		ret = max(ret, cur);
	}
	return (dp[joft(u, v)] = ret);
}

int main(){
	int testN;
	s = 0;
	t = 1;
	scanf(" %d", &testN);
	FOR(test, testN){
		input();
		memset(dis, -1, sizeof dis);
		bfs(0);
		
		if(dis[t] == 1){
			int ans = 0;
			FOR(i, n)
				if(dis[i] == 1)
					ans++;
			printf("Case #%d: 0 %d\n", test + 1, ans);
			continue;
		}
		
		dp.clear();
		int ans = 0;
		FOR(i, SZ(list[t])){
			int u = list[t][i];
			if(dis[u] + 1 != dis[t])
				continue;
			FOR(j, SZ(list[u])){
				int v = list[u][j];
				if(dis[v] + 2 != dis[t])
					continue;
				int cur = cal(u, v);
				memset(mark, 0, sizeof mark);
				FOR(i, SZ(list[u]))
					if(dis[list[u][i]] >= dis[t] - 1)
						if(!mark[list[u][i]]++)
							cur++;
				FOR(i, SZ(list[v]))
					if(dis[list[v][i]] >= dis[t] - 1)
						if(!mark[list[v][i]]++)
							cur++;
				cur--;
				ans = max(ans, cur);
			}
		}
			
		printf("Case #%d: %d %d\n", test + 1, dis[t] - 1, ans);
	}
	return 0;
}
