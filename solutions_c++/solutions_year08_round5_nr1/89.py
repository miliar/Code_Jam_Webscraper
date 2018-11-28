#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;

struct PT {
	int x,y;
	PT(int a=0, int b=0) : x(a), y(b) {}
};
int tr(const PT& a, const PT& b) { return (b.x - a.x)*(b.y + a.y); } 
int signed_area(const vector<PT>& v) {
	int ret = 0.;
	for (int i=0;i<v.size();++i) ret += tr(v[i], v[(i+1)%v.size()]);
	assert(ret%2==0);
	return ret/2;
}
int area(const vector<PT>& v) { return abs(signed_area(v)); }

const int INF=1<<29;
const int MAX=6005;
int minl[MAX];
int maxr[MAX];
int minu[MAX];
int maxd[MAX];
char s[10000];

const int UP=0;
const int RIGHT=1;
const int DOWN=2;
const int LEFT=3;
int dx[]={-1,0,1,0};
int dy[]={0,1,0,-1};

void turn_left(int& d) { d = (d-1 + 4)%4; }
void turn_right(int& d) { d = (d+1)%4; }

void checkx(int x, int y) {
	assert(0 <= x && x < MAX && 0 <= y && y < MAX);
	maxr[x]=max(maxr[x],y);
	minl[x]=min(minl[x],y);
}
void checky(int y, int x) {
	maxd[y]=max(maxd[y],x);
	minu[y]=min(minu[y],x);
}

void update(int x, int y, int nx, int ny, int d) {
	if (d==UP || d==DOWN) { // place at x-coordinate
		if (d==DOWN) {
			return checkx(x,y);
		}
		else {
			return checkx(nx,y);
		}
	}
	else { // place at x-coordinate
		if (d==RIGHT) {
			return checky(y,x);
		}
		else {
			return checky(ny,x);
		}
	}
	assert(0);
}


bool ok(int x, int y) {
	return (minl[x] <= y && y < maxr[x]) || (minu[y] <= x && x < maxd[y]);
}

int main() {
	int NCASES;
	scanf("%d", &NCASES);
	for (int z=1;z<=NCASES;++z) {
		for (int i=0;i<MAX;++i) 
			minl[i]=minu[i]=INF, maxr[i]=maxd[i]=-INF;
		int x=3002, y=3002, d=UP;
		vector<PT> pol;
		pol.push_back(PT(x,y));
		
		int minx=x,maxx=x;
		int miny=y,maxy=y;
		int T;
		scanf("%d", &T);
		while (T-- > 0) {
			int k;
			scanf("%s %d", s, &k);
			int len = strlen(s);
			while (k-- > 0) {
				for (int j=0;j<len;++j) {
					switch (s[j]) {
						case 'F':
							update(x,y,x+dx[d],y+dy[d],d);
							x += dx[d], y += dy[d];
							minx=min(minx,x);
							maxx=max(maxx,x);
							miny=min(miny,y);
							maxy=max(maxy,y);
						break;
						case 'R': {
							pol.push_back(PT(x,y));
							turn_right(d);
							break;
						}
						case 'L': {
							pol.push_back(PT(x,y));
							turn_left(d);
							break;
						}
					}
					//printf("%d %d %d\n", x,y,d);
				}
			}
		}

		int ans=0;
		for (int x=minx-1;x<=maxx+1;++x) {
			for (int y=miny-1;y<=maxy+1;++y) {
				if (ok(x,y)) {
					/*
					printf("\tX: %d, Y: %d\n", x-3002, y-3002);
					printf("\t\tMINL[x]: %d, MAXR[x]: %d\n", minl[x], maxr[x]);
					printf("\t\tMINU[Y]: %d, MAXD[y]: %d\n", minu[y], maxd[y]);
					*/
					//printf("OK %d %d\n", x-3002,y-3002);
					++ans;
				}
			}
		}
		int A = area(pol);
		//printf("AREA %d\n", A);
		int res = ans - A;
		assert(res>=0);
		printf("Case #%d: %d\n", z, res);
	}
}
