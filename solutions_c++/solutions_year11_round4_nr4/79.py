#include <map>        
#include <set>        
#include <queue> 
#include <cmath>       
#include <cstdio>      
#include <vector>        
#include <string>        
#include <sstream>       
#include <iostream>       
#include <algorithm>        
using namespace std;        
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)        
#define FORE(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)        
#define SET(x, v) memset(x, v, sizeof (x))        
#define sz size()        
#define cs c_str()        
#define pb push_back        
#define mp make_pair       
    
typedef long long ll;        
int chk[512][512];
int nn[512], nbr[512][512];
int dist[512][512];
int a1, a2;

int rec[512], n, used[512];
void dfs(int x, int dp) {
	used[x] = 1;
	rec[x]++;
	FOR(i,0,nn[x]) 
		rec[nbr[x][i]]++;
	if(dp == a1) {
		int cnt = 0;
		FOR(i,0,n)
			if(rec[i] && !used[i]) cnt++;
		a2=max(cnt, a2);
	}
	else {
		FOR(i,0,n) {
			if(rec[i]>0 && dist[1][i] + dp == a1) {
				dfs(i, dp+1);
			}
		}
	}
	used[x] = 0;
	rec[x]--;
	FOR(i,0,nn[x]) 
		rec[nbr[x][i]]--;
}
int main() {
	int e= 0, T;
	scanf("%d",&T);
	while(T--) {
		int m;
		scanf("%d%d",&n,&m);
		FOR(i,0,n) FOR(j,0,n) chk[i][j] = 0, dist[i][j] = n+100;
		FOR(i,0,n) dist[i][i] = 0;
		FOR(i,0,n) nn [i] = 0;
		FOR(i,0,m) {
			int x, y;
			scanf("%d,%d",&x,&y);
			chk[x][y] = chk[y][x] = 1;
			dist[x][y] = dist[y][x] = 1;
			nbr[x][nn[x]++] = y;
			nbr[y][nn[y]++] = x;
		}
		FOR(k,0,n) 
			FOR(i,0,n)
				FOR(j,0,n)
					if(dist[i][j] > dist[i][k] + dist[k][j])
						dist[i][j] = dist[i][k] + dist[k][j];
						
		//FOR(i,0,n) {FOR(j,0,n) printf("%d",chk[i][j]); printf("\n");}
		a1 = dist[0][1] - 1;
		a2 = 0;
		FOR(i,0,n) rec[i] = used[i] = 0;
		dfs(0, 0);
		printf("Case #%d: %d %d\n", ++e, a1, a2);
	}
	return 0;
}