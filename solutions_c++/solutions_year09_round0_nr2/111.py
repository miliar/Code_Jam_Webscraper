#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ALL(v) v.begin(), v.end()
#define SZ(v) (int)v.size()

#define vi vector<int>
#define vs vector<string>
#define ui unsigned int
#define ll long long

using namespace std;

typedef struct { int h, x, y; } cell;

int T, h, w, i, j, k;
int a[110][110];
cell v[10010]; int sz;

bool cmp(cell aa, cell bb) { return aa.h > bb.h; }

int reg[110][110];
int tot;


int main()
{
	
	scanf("%d", &T);
	for(int caso=1; caso<=T; caso++) {
		scanf("%d %d", &h, &w);
		sz=0;
		for(i=0; i<h; i++) for(j=0; j<w; j++) {
			scanf("%d", &a[i][j]);
			cell c;
			c.h=a[i][j];
			c.x=i; c.y=j;
			v[sz++] = c;
		}
		
		sort(v, v+sz, cmp);
		tot=0;
		memset(reg, -1, sizeof(reg));
		
		for(i=0; i<sz; i++) {
			cell c=v[i];
			if(reg[c.x][c.y] >= 0) continue;
			
			stack<cell> s;
			s.push(c);
			
			while(1) {
				cell d = s.top();
				if(reg[d.x][d.y] >= 0) {
					int r = reg[d.x][d.y];
					s.pop();
					while(!s.empty()) {
						cell e = s.top();
						s.pop();
						reg[e.x][e.y] = r;
					}
					break;
				} else {
					int nx=d.x, ny=d.y;
					if(d.x-1>=0 && d.y>=0 && a[nx][ny] > a[d.x-1][d.y]) nx=d.x-1, ny=d.y;
					if(d.x>=0 && d.y-1>=0 && a[nx][ny] > a[d.x][d.y-1]) nx=d.x, ny=d.y-1;
					if(d.x>=0 && d.y+1<w && a[nx][ny] > a[d.x][d.y+1]) nx=d.x, ny=d.y+1;
					if(d.x+1<h && d.y>=0 && a[nx][ny] > a[d.x+1][d.y]) nx=d.x+1, ny=d.y;
					
					if(nx==d.x && ny==d.y) {
						int r = tot++;
						while(!s.empty()) {
							cell e = s.top();
							s.pop();
							reg[e.x][e.y] = r;
						}
						break;
					} else {
						cell e;
						e.h = a[nx][ny];
						e.x = nx;
						e.y = ny;
						s.push(e);
					}
				}
			}
		}
		
		printf("Case #%d:\n", caso);
		
		int mp[10100];
		memset(mp, -1, sizeof(mp));
		int curr=0;
		
		for(i=0; i<h; i++) {
			for(j=0; j<w; j++) {
				if(mp[reg[i][j]] < 0) mp[reg[i][j]] = curr++;
				if(j) printf(" ");
				printf("%c", 'a'+mp[reg[i][j]]);
			}
			printf("\n");
		}
		
		
	}
	
	
}
