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
const int UP = 1;
const int RIGHT = 2;
const int DOWN = 4;
const int LEFT = 8;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
typedef long long i64;
vector<pair<int, int> > dat;
int c[256][256];
int wall[256][256];
vector<pair<int, int> > qu;
int main() {
	freopen("A.in","r",stdin);
	int e = 0, T;
	int m;
	scanf("%d",&T);
	while(T--) {
		scanf("%d",&m);
		int repeat;
		char buff[64];
		dat.clear();
		dat.pb(mp(120,120));
		int px = 120, py = 120, dir = 0;
		bool changed = false;
		FOR(i,0,m) {
			scanf("%s%d",buff,&repeat);
			string tmp = buff;
			while(repeat--) {
				FOR(j,0,tmp.sz) {
					if(tmp[j]=='L') {
						dir=(dir+3)%4;
						changed = true;
					}
					else if(tmp[j]=='R') {
						dir=(dir+1)%4;
						changed = true;
					}
					else {
						if(changed) {
							if(px!=0 || py!=0)
								dat.pb(mp(px, py));
						}
						changed = false;
						px+=dx[dir];
						py+=dy[dir];
					}
				}
			}			
		}
		//printf("size: %d\n",dat.sz);FOR(i,0,dat.sz)printf("(%d, %d)",dat[i].first-120,dat[i].second-120);printf("\n");
		int n = dat.sz, min1;
		px = 1000, py = 1000;
		FOR(i,0,n) {
			if (py > dat[i].second) {
				px = dat[i].first;
				py = dat[i].second;
				min1 = i;
			} else if (py == dat[i].second && px > dat[i].first) {
				px = dat[i].first;
				min1 = i;
			}
		}
		dat.pb(mp(dat[0].first, dat[0].second));
		SET(wall,0);
		FOR(i,0,n) {
			int ax = dat[i].first, ay = dat[i].second;
			int bx = dat[i+1].first, by = dat[i+1].second;
			if (ax == bx) {
				FOR(k,min(ay,by),max(ay,by)) {
					wall[ax][k] |= LEFT;
					wall[ax-1][k] |= RIGHT;
				}
			} else {
				FOR(k,min(ax,bx),max(ax,bx)) {
					wall[k][ay] |= DOWN;
					wall[k][ay-1] |= UP;
				}
			}
		}
		// (px, py) is inside for sure
		int front=0,rear=0;
		SET(c,0);
		qu.clear();
		qu.pb(mp(px, py));
		c[px][py] = 1;
		for(;front<qu.sz;front++) {
			int x = qu[front].first;
			int y = qu[front].second;
			//qu.earse(qu.begin());
			FOR(k,0,4) {
				int qx=x+dx[k];
				int qy=y+dy[k];
				if(wall[x][y] & (1<<k))continue;
				if(c[qx][qy]==0) {
					qu.pb(mp(qx,qy));
					c[qx][qy]=1;
				}
			}
		}
		int cnt = 0;
		FOR(i,19,225) {
			FOR(j,19,225) {
				if(c[i][j])continue;
				bool left,right,up,down;
				left=right=up=down=false;
				//left-right
				for(int k=i-1;k>=19 && !left;k--) 
					if(c[k][j]) 
						left=true;
				if(left) {
					for(int k=i+1;k<225 && !right;k++)
						if(c[k][j])
							right=true;
					if(left&&right) {cnt++;continue;}
				}
				for(int k=j-1;k>=19 && !down;k--)
					if(c[i][k])
						down=true;
				if(down) {
					for(int k=j+1;k<225 && !up;k++)
						if(c[i][k])
							up=true;
					if(up)cnt++;
				}		
			}
		}
		printf("Case #%d: %d\n",++e,cnt);
	}

	return 0;
}

