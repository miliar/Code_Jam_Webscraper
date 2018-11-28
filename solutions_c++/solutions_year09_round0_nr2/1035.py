#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <sstream>
#include <cstring>
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i,v) for (int i = 0; i < v.size(); i++)
#define fors(i,s) for (int i = 0; i < s.length(); i++)
#define rep(i,f,t) for (int i = (int)(f); i < (int)(t); i++)
#define per(i,f,t) for (int i = f; i > t; i--)
#define fe(it,container) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define all(a) a.begin(),a.end()
#define mp make_pair
#define pb push_back
#define sz size()
#define ft first
#define sd second
#define VI vector< int >
#define VS vector< string >
#define PII pair< int,int >
#define PIS pair< int, string >
#define VPIS vector< PIS >
#define VPII vector< PII >
#define sqr(a) ((a)*(a))
#define cube(a) ((a)*(a)*(a))
#define pname "domino"
#define mod 1000000007LL
#define pi 3.1415926535
#define have(u,v) (u&(1<<v))
#define maxn 50000
#define inf (1<<20)
#define ll long long
#define maxnm 105
using namespace std;

int a[maxnm][maxnm];
int p[maxnm][maxnm];
VPII c[maxnm][maxnm];
int ans[maxnm][maxnm];
char rans[30];

int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

void dfs(int u,int v,int color) {
	ans[u][v]=color;
	forv(i,c[u][v])dfs(c[u][v][i].first,c[u][v][i].second,color);
}

void solve() {
	int h,w;
	cin >> h >> w;

	forn(i,h)forn(j,w){
		p[i][j]=0;
		cin>> a[i][j];
		c[i][j].clear();
		ans[i][j]=0;
	}

	forn(i,h)forn(j,w) {
		int x=-1,y=-1,H=inf;
		forn(k,4) {
			int nx=i+dx[k];
			int ny=j+dy[k];
			if (nx < 0 || ny < 0 || nx >= h || ny >= w || a[nx][ny] >= a[i][j] || a[nx][ny] >= H)continue;
			x=nx;
			y=ny;
			H=a[nx][ny];
		}
		if (x!=-1) {
			p[i][j]=1;
			c[x][y].pb(mp(i,j));
		}
	}

	memset(rans, 0, sizeof(rans));

	int count=1;
	forn(i,h)forn(j,w)if (!p[i][j])dfs(i,j,count++);
	count=0;
	forn(i,h)forn(j,w)if (!rans[ans[i][j]])rans[ans[i][j]]='a'+count++;
	forn(i,h) {
		forn(j,w)cout<< rans[ans[i][j]] << " ";
		cout<< endl;
	}
}

int main() {

   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);

	int n;
	cin >> n;
	forn(i,n) {
		printf("Case #%d:\n",i+1);
		solve();
	}
	return 0;
}	

