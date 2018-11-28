#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

const int M = 600;
char grid[M][M];
int r,c,d;

inline int balx(int x,int y,int xi,int yi) {
	return (2*x-(2*xi+1))*grid[xi][yi];
}

inline int baly(int x,int y,int xi,int yi) {
	return (2*y-(2*yi+1))*grid[xi][yi];
}

inline int balx2(int x,int y,int xi,int yi) {
	return (x-xi)*grid[xi][yi];
}

inline int baly2(int x,int y,int xi,int yi) {
	return (y-yi)*grid[xi][yi];
}

inline int blade(int x,int y) {
	int mr = min(min(x,r-x),min(y,c-y));
	int mx=0;
	int my=0;
	int ret = -1;
	for (int i=1; i<=mr; ++i) {
		{
			int xi=x-i;
			for (int yi=y-i+1; yi<y+i-1; ++yi) {
				mx += balx(x,y,xi,yi);
				my += baly(x,y,xi,yi);
			}
		}
		{
			int xi=x+i-1;
			for (int yi=y-i+1; yi<y+i-1; ++yi) {
				mx += balx(x,y,xi,yi);
				my += baly(x,y,xi,yi);
			}
		}
		{
			int yi=y-i;
			for (int xi=x-i+1; xi<x+i-1; ++xi) {
				mx += balx(x,y,xi,yi);
				my += baly(x,y,xi,yi);
			}
		}
		{
			int yi=y+i-1;
			for (int xi=x-i+1; xi<x+i-1; ++xi) {
				mx += balx(x,y,xi,yi);
				my += baly(x,y,xi,yi);
			}
		}

		if (mx == 0 && my == 0) ret = i+i;
		mx += balx(x,y,x-i,y-i);
		mx += balx(x,y,x-i,y+i-1);
		mx += balx(x,y,x+i-1,y+i-1);
		mx += balx(x,y,x+i-1,y-i);
		my += baly(x,y,x-i,y-i);
		my += baly(x,y,x-i,y+i-1);
		my += baly(x,y,x+i-1,y+i-1);
		my += baly(x,y,x+i-1,y-i);
	}
	return ret;
}

inline int blade2(int x,int y) {
	int mr = min(min(x,r-x-1),min(y,c-y-1));
	int mx=0;
	int my=0;
	int ret = -1;
	if (x==3 && y==4) {
		//printf("mr: %d\n",mr);
	}
	for (int i=1; i<=mr; ++i) {
		{
			int xi=x-i;
			for (int yi=y-i+1; yi<y+i; ++yi) {
				mx += balx2(x,y,xi,yi);
				my += baly2(x,y,xi,yi);
			}
		}
		{
			int xi=x+i;
			for (int yi=y-i+1; yi<y+i; ++yi) {
				mx += balx2(x,y,xi,yi);
				my += baly2(x,y,xi,yi);
			}
		}
		{
			int yi=y-i;
			for (int xi=x-i+1; xi<x+i; ++xi) {
				mx += balx2(x,y,xi,yi);
				my += baly2(x,y,xi,yi);
			}
		}
		{
			int yi=y+i;
			for (int xi=x-i+1; xi<x+i; ++xi) {
				mx += balx2(x,y,xi,yi);
				my += baly2(x,y,xi,yi);
			}
		}

	if (x==3 && y==4) {
		//printf("mr%d %d %d\n",i, mx, my);
	}
		if (mx == 0 && my == 0) ret = i+i+1;
		mx += balx2(x,y,x-i,y-i);
		mx += balx2(x,y,x-i,y+i);
		mx += balx2(x,y,x+i,y+i);
		mx += balx2(x,y,x+i,y-i);
		my += baly2(x,y,x-i,y-i);
		my += baly2(x,y,x-i,y+i);
		my += baly2(x,y,x+i,y+i);
		my += baly2(x,y,x+i,y-i);

	if (x==3 && y==4) {
		//printf("mr%d %d %d\n",i, mx, my);
	}
	}
	//printf("[%d %d] %d\n",x,y,ret);
	return ret;
}

int main(void) {
	int t;
	scanf("%d",&t);
	for (int tc=1;tc<=t; ++tc) {
		scanf("%d%d%d",&r,&c,&d);
		for (int i=0; i<r; ++i) {
			scanf("%s",grid[i]);
			for (int j=0; j<c; ++j) grid[i][j]-='0';
		}
		int ret = -1;
		for (int x=1; x<r; ++x) for (int y=1; y<c; ++y) ret = max(ret,blade(x,y));
		for (int x=1; x<r-1; ++x) for (int y=1; y<c-1; ++y) ret = max(ret,blade2(x,y));
		printf("Case #%d: ",tc);
		if (ret > 2) {
			printf("%d\n",ret);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
