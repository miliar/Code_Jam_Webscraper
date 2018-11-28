#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;

typedef long long LL;
typedef vector<int> vi;
typedef vector< pair<int, int> > vii;
#define MP(x,y) make_pair(x, y)

int e[105][105];
char ta[105][105];
int r, c, cnt=0;
int dx[4][2] = {{1, -1}, {0, 0}, {1, -1}, {-1, 1}};
int dy[4][2] = {{0, 0}, {1, -1}, {1, -1}, {1, -1}};

vector<int> a[10005];
vector<int> rev[10005];

int id(int x, int y) {
	return x*c+y;
}

int vis[20005];
int vist[20005];
int lleft=0, rright=0, fault=0;
int st[10005], top=0;

void dfs2(int x);
void dfs1(int x) {
	vis[x] = 1;
	++lleft;
	for(int i=0;i<a[x].size();i++) {
		if(!vist[a[x][i]])
			dfs2(a[x][i]);
	}
	//st[top++] = x;
}

void dfs2(int x) {
	vist[x] = 1;
	++rright;
	for(int i=0;i<rev[x].size();i++) {
		if(!vis[rev[x][i]])
			dfs1(rev[x][i]);
	}
}
/*
void dfs2(int x, int cc) {
	vis[x] = cc;
	//fprintf(stderr, "x=%d, cc=%d\n", x, cc);
	for(int i=0;i<rev[x].size();i++)
		if(!vis[rev[x][i]])
			dfs2(rev[x][i], cc);
}
*/
int main(void) {
	int T, cs;
	scanf("%d", &T);
	for(cs=1;cs<=T;cs++) {

		scanf("%d%d", &r, &c);
		int i, j;
		cnt=0;
		for(i=0;i<r;i++)
			scanf("%s", ta[i]);
		//memset(e, 0, sizeof(e));
		//go(0, 0);
		for(i=0;i<r;i++)
			for(j=0;j<c;j++){
				int type=0;
				if(ta[i][j] == '|') type=0;
				else if(ta[i][j]=='-') type=1;
				else if(ta[i][j]=='\\') type=2;
				else type=3;
				int x = id(i, j);
				for(int u=0;u<2;u++){
					int xx=i+dx[type][u], yy = j+dy[type][u];
					if(xx<0)xx=r-1;
					if(yy<0)yy=c-1;
					if(xx>=r) xx=0;
					if(yy>=c) yy=0;
					int y = id(xx, yy);
					a[x].push_back(y);
					rev[y].push_back(x);
				}
			}

		memset(vis, 0, sizeof(vis));
		memset(vist,0,sizeof(vist));
		top=0;
			int ans = 1;
		const int MOD = 1000003;
		for(i=0;i<r*c;i++) {
			if(!vis[i]) {
				lleft=rright=0;
				fault = 0;
				dfs1(i);
				if(fault || lleft!=rright)
					ans=0;
				else

				ans = ans * 2 % MOD;

			}
		}



		/*int cc=0;
		memset(vis, 0, sizeof(vis));
		while(--top>=0) {
			if(!vis[st[top]]) {
				++cc;
				//fprintf(stderr, "cc=%d\n", cc);
				dfs2(st[top], cc);
			}
		}*/

	
	/*	int vr[10005]={};
		for(i=0;i<r*c;i++){
			int www=0;
			printf("vis[%d]=%d\n", i, vis[i]);
			for(j=0;j<2;j++)
				if(vis[a[i][j]] == vis[i]) {
					++www;
					vr[a[i][j]]++;
				}
			if(www==0) ans = 0;
			else if(www==2 && a[i][0] != a[i][1])
				ans = ans * 2 % MOD;
		}
		for(i=0;i<r*c;i++)
			printf("vr[%d]=%d\n", i, vr[i]);*/
		/*for(i=0;i<cc;i++)
			ans = ans * 2 % MOD;*/

		for(i=0;i<r*c;i++) {
			a[i].clear();
			rev[i].clear();
		}
		

		cnt = ans;
		printf("Case #%d: %d\n", cs, cnt);
		fprintf(stderr, "Case #%d: %d\n", cs, cnt);
    }
    return 0;
}


