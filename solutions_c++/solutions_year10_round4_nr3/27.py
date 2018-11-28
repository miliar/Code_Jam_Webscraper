//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back

using namespace std;

const int MAX_N = 1000 + 10;
const int INF = 1 << 30;

int r;
int crd[MAX_N][4];
//vector<int> list[MAX_N];
bool mark[MAX_N];

bool esht(int a, int b){
	if(crd[a][2] + 1 < crd[b][0])
		return false;
	if(crd[b][2] + 1 < crd[a][0])
		return false;
	if(crd[a][3] + 1 < crd[b][1])
		return false;
	if(crd[b][3] + 1 < crd[a][1])
		return false;
	if(crd[a][2] + 1 == crd[b][0] && crd[a][3] + 1 == crd[b][1])
		return false;
	if(crd[b][2] + 1 == crd[a][0] && crd[b][3] + 1 == crd[a][1])
		return false;
	return true;
}

int maxx, maxy, summin;

void dfs(int v){
	mark[v] = true;
	maxx = max(maxx, crd[v][2]);
	maxy = max(maxy, crd[v][3]);
	summin = min(summin, crd[v][0] + crd[v][1]);
	FOR(j, r)
		if(!mark[j] && esht(v, j))
			dfs(j);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++){
		scanf("%d", &r);
		FOR(i, r){
			FOR(j, 4)
				scanf("%d", &crd[i][j]);
			/*list[i].clear();
			FOR(j, i)
				if(esht(j, i)){
					list[i].PB(j);
					list[j].PB(i);
				}*/
			mark[i] = 0;
		}
		int ans = 0;
		FOR(i, r)
			if(!mark[i]){
				summin = INF;
				maxx = 0;
				maxy = 0;
				dfs(i);
				ans = max(ans, maxx + maxy - summin);
			}
		//cerr<<maxx<<" "<<maxy<<" "<<summin<<endl;
		printf("Case #%d: %d\n", test, ans + 1);
	}
	return 0;
}
