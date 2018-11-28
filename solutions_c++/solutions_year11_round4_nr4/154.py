#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <vector>
#define MAX 450

using namespace std;

typedef long long ll;

int vis[MAX];
vector <int> pai[MAX];
vector <int> l[MAX];
bool foi[MAX];
queue <int> q;
int P, W;
int pd[MAX];


int f(int x, ll mask){
	//if (pd[x] != -1)
	//	return pd[x];
	//int &r = pd[x];
	int r = 0;
	for (int i = 0; i < (int)l[x].size(); i++){
		int v = l[x][i];
		if (((1LL<<((ll)v)) & mask) == 0){
			mask |= (1LL<<((ll)v));
			r++;
		}
	}
	int r2 = 0;
	for (int i = 0; i < (int)pai[x].size(); i++)
		r2 = max(r2, f(pai[x][i], mask));
	return r + r2;
}

int bfs(){
	while (!q.empty())
		q.pop();
	for (int i = 0; i < MAX; i++){
		vis[i] = -1;
		pai[i].clear();
		foi[i] = false;
		pd[i] = -1;
	}
	vis[0] = 0;
	q.push(0);
	while (!q.empty()){
		int x = q.front();
		q.pop();
		if (foi[x])
			continue;
		foi[x] = true;
		for (int j = 0; j < (int)l[x].size(); j++){
			int i = l[x][j];
			if (vis[i] == -1 || vis[i] >= vis[x]+1){
				if (vis[i] == -1){
					vis[i] = vis[x] + 1;
					pai[i].clear();
					q.push(i);
				}
				pai[i].push_back(x);
			}
		}
	}
	int resp = 0;
	for (int i = 0; i < (int)pai[1].size(); i++)
		resp = max(resp, f(pai[1][i], 1));
	return resp;
}

int main(){
	int T;
	scanf ("%d", &T);
	for (int cas = 1; cas <= T; cas++){
		scanf ("%d%d", &P, &W);
		for (int i = 0; i < P; i++)
			l[i].clear();
		for (int i = 0; i < W; i++){
			int x, y;
			scanf("%d%*c%d", &x, &y);
			l[x].push_back(y);
			l[y].push_back(x);
		}
		int resp = bfs();
		printf ("Case #%d: %d %d\n", cas, vis[1]-1, resp-(vis[1]-1));
	}
	return 0;
}
