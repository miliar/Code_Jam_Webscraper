#include <map>     
#include <set>     
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
 
typedef long long i64;     
int dx[4] = {0, 1, -1, 0};
int dy[4] = {1, 0, 0, -1};
char dat[32][32];
 int tx, ty;
 int front, rear ;
 int qu[32*32][2];
 int vis[32][32];
 int vis2[32][32];
 int n, m;
 bool found;
 int marked;
 void add(int x, int y, int v) {
	 vis[x][y] = v+1;
	 qu[rear][0] = x;
	 qu[rear++][1] = y;
 }
void doit(int sx, int sy) {
		front=rear=0;
		SET(vis, -1);
		add(sx,sy,-1);
		for(;front<rear;front++) {
			int x = qu[front][0];
			int y = qu[front][1];
			int v = vis[x][y];
			FOR(k,0,4) {
				int px = x + dx[k];
				int py = y + dy[k];
				if(px>=0 && py>=0 && px<n && py<m && dat[px][py]!='.' && vis[px][py]==-1) {
					add(px, py, v);
				}
			}
		}

}
void mark(int x, int y, int prev) {
	bool hey = false;
	FOR(k,0,4) {
		int px = x + dx[k];
		int py = y + dy[k];
		if(px>=0 && py>=0 && px<n && py<m) {
			if(dat[px][py]=='#') {
				if(vis[px][py] + vis2[px][py] == vis2[tx][ty] && vis[px][py]== prev - 1) {
					marked++;
					dat[px][py]='T';
					mark(px, py, prev - 1);
					hey = true;
					return;
				}
			}
			else if(px==tx && py==ty) {
				found = true;
				return;
			}
		}
	}
	if(!hey) {
		printf("Wtf (%d, %d)\n", x, y);
	}
}
int main() {

	freopen("D.in","r",stdin);
	int e = 0, T;

	scanf("%d",&T);
	while(T--) {
		scanf("%d%d",&n,&m);
		FOR(i,0,n)
			scanf("%s",dat[i]);
		tx = ty = -1;
		FOR(i,0,n) {
			FOR(j,0,m) {
				if(i || j)
					if(dat[i][j]=='T') {
						tx = i;
						ty = j;
					}
			}
		}
		int base = 0;
		{

			doit(0, 0);
			int ans  = 0;
			FOR(i,0,n)
				FOR(j,0,m)
					if(dat[i][j]=='#' || dat[i][j]=='T') {
						ans+= vis[i][j];
					}
			base = ans;
		}

		if(tx!=-1) {
			doit(0, 0);
			//TODO: XXX : FIXME: ans can be long long?
			int ans = 0;
			ans = vis[tx][ty] * (vis[tx][ty] + 1);
			ans/=2;
			//minimum cost
			memcpy(vis2, vis, sizeof vis);
			doit(tx, ty);
			
			found = false;
			marked = 0;
			mark(0, 0, vis[0][0]);
			if(!found || marked != vis2[tx][ty]-1) {
				printf("errr... %d %d/%d\n",found,marked,vis2[tx][ty]-1);
				
				printf("min path: %d\n",vis2[tx][ty]);
				FOR(i,0,n)
					printf("%s\n",dat[i]);
				printf("begin with %d\n",ans);
				
			}
			
			
			FOR(i,0,n)
				FOR(j,0,m)
					if(dat[i][j]=='#') {
						int v = min(vis[i][j], vis2[i][j]);
						//printf("(%d, %d): %d\n",i,j,v);
						ans+=v;
	
					}
			base = min(base, ans);
		} 
		printf("Case #%d: %d\n",++e, base);

	}


	return 0;
}



