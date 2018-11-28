#include<set>
#include<map>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
#define FORE(i,a) for(typeof(a.begin()) i = a.begin(); i!= a.end(); ++i)
#define SET(x,v) memset(x,v,sizeof(x))
#define cs c_str()
#define sz size()
#define mp make_pair
#define pb push_back
int n[2];
vector<pair<int, int> > to[2][128];
int deg[2][128];
vector<pair<int,int> > dat[2];
int add, cnt;
int ans[2];
void doit(int t, int x) {
	deg[t][x] = -1;
	cnt--;
	int mintime = 24*60, min1 = -1;
//	printf("doit(%d, %d)  %d\n",t,x, to[t][x].sz);
	FOR(i,0,to[t][x].sz) {
		int s = to[t][x][i].first;
		int y = to[t][x][i].second;
		deg[s][y] --;
		if (deg[s][y] == 0) {
			if(mintime > dat[s][y].first) {
				mintime = dat[s][y].first;
				min1 = i;
			}
		}
	}
	if (min1 != -1) {
		int s = to[t][x][min1].first;
		int y = to[t][x][min1].second;
		doit(s, y);
	}
}
pair<int, int> getit() {
	int h1, m1, h2, m2;
	scanf("%d:%d%d:%d",&h1,&m1,&h2,&m2);
	return mp(h1*60+m1, h2*60+m2);
}
int main() {
	freopen("Binput.txt","r",stdin);
	int e = 0, T;
	FILE *fo=fopen("Boutput.txt","w");
	scanf("%d",&T);
	while(T--) {
		scanf("%d%d%d",&add,&n[0],&n[1]);
		SET(deg, 0);
		dat[0].resize(n[0]);
		dat[1].resize(n[1]);
		FOR(t,0,2) {
			FOR(i,0,n[t]) {
				dat[t][i] = getit();
				to[t][i].clear();
			}
		}
		FOR(t,0,2)
			sort(dat[t].begin(), dat[t].end());
	ans[0]=ans[1]=0;
		while(dat[0].sz && dat[1].sz) {
			int turn, arrival;
			//printf("%d vs %d\n",dat[0][0].first, dat[1][0].first);
			if (dat[0][0].first > dat[1][0].first) {
				turn = 0;
				arrival = dat[1][0].second;
				dat[1].erase(dat[1].begin());
			} else {
				turn = 1;
				arrival = dat[0][0].second;
				dat[0].erase(dat[0].begin());
			}
			ans[1-turn]++;
			while(true) {
				//printf("now turn: %d, arrival: %d\n",turn,arrival);
				bool found = false;
				FORE(i,dat[turn]) {
					if (i->first >= arrival + add) {
						arrival = i->second;
						dat[turn].erase(i);
						found = true;
						turn = 1 - turn;
						break;
					}
				}
				if(!found)break;
			}
		}
		//printf("remaining: %d %d\n",dat[0].sz,dat[1].sz);
		ans[0] += dat[0].sz;
		ans[1] += dat[1].sz;
		fprintf(fo,"Case #%d: %d %d\n",++e, ans[0], ans[1]);
		printf("Case #%d: %d %d\n",e,ans[0],ans[1]);
	}
	fclose(fo);
	return 0;
}