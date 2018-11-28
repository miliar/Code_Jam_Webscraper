#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<iostream>
#include<sstream>
#include<cassert>
using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define SIZE 1005
#define EPS 1e-11
#define INF 1e11

struct Bird {
	int x,y;
	bool isbird;
}b[SIZE];

int minx,maxx,miny,maxy;
int uminx,umaxx,uminy,umaxy;

int n,m;

void process() {
	int i;
	bool f=0;

	minx = miny = maxx = maxy = -1;
	rep(i,n) if(b[i].isbird) {
		if(!f) {
			minx = maxx = b[i].x;
			miny = maxy = b[i].y;
			f = 1;
			continue;
		}
		minx = min(minx,b[i].x);
		miny = min(miny,b[i].y);
		maxx = max(maxx,b[i].x);
		maxy = max(maxy,b[i].y);
	}

	uminx = uminy = 1;
	umaxx = umaxy = 1000000;

	rep(i,n) if(b[i].isbird == 0) {
		if(maxx < 0) continue;
		if(b[i].x >= minx && b[i].x <= maxx) { //case A
			if(b[i].y > maxy) umaxy = min(umaxy,b[i].y-1);
			else uminy = max(uminy,b[i].y+1);
		}
		else if(b[i].y >= miny && b[i].y <= maxy) { //case B
			if(b[i].x > maxx) umaxx = min(umaxx,b[i].x - 1);
			else uminx = max(uminx,b[i].x+1);
		}
		else { //case C

			/*
			if(b[i].y > maxy) umaxy = min(umaxy,b[i].y-1);
			else uminy = max(uminy,b[i].y+1);

			if(b[i].x > maxx) umaxx = min(umaxx,b[i].x - 1);
			else uminx = max(uminx,b[i].x+1);
			*/
		}
	}

}

void query(int x,int y) {
	if(maxx > 0 && x >=minx && x<=maxx && y >=miny && y<=maxy) {
		printf("BIRD\n");
		return;
	}

	//if(maxx < 0) {
		int i;
		rep(i,n) if(b[i].isbird == 0) {
			if(x == b[i].x && y == b[i].y)
			{
				printf("NOT BIRD\n");
				return;
			}
		}
	//}

		

	if(x >= uminx && x <= umaxx && y >= uminy && y <= umaxy) {
		if(maxx > 0) {
			rep(i,n) if(b[i].isbird == 0) {
				if(b[i].x >= minx && b[i].x <= maxx) ;
				else if(b[i].y >= miny && b[i].y <= maxy) ;
				else {
					if(b[i].y > maxy && b[i].x > maxx) {
						if(x >= b[i].x && y >= b[i].y) {
							printf("NOT BIRD\n");
							//assert(0);
							return;
						}
					}
					else if(b[i].y > maxy && b[i].x < minx) {
						if(x <= b[i].x && y >= b[i].y) {
							printf("NOT BIRD\n");
							//assert(0);
							return;
						}
					}
					else if(b[i].y < miny && b[i].x > maxx) {
						if(x >= b[i].x && y <= b[i].y) {
							printf("NOT BIRD\n");
							//assert(0);
							return;
						}
					}
					else if(b[i].y < miny && b[i].x < minx) {
						if(x <= b[i].x && y <= b[i].y) {
							printf("NOT BIRD\n");
							//assert(0);
							return;
						}
					}

				}
			}
		}
		printf("UNKNOWN\n");
		return;
	}

	printf("NOT BIRD\n");
}

int main() {
	int T,kase=1;
	char s[1000],t[100];
	int i;
	int x,y;
	freopen("C:\\Documents and Settings\\codejam\\Desktop\\Projects\\Problem A\\Problem A\\a.in","r",stdin);
	freopen("C:\\Documents and Settings\\codejam\\Desktop\\Projects\\Problem A\\Problem A\\a.out","w",stdout);
	scanf("%d",&T);
	while(T--) {
		printf("Case #%d:\n",kase++);
		scanf("%d",&n);gets(s);
		rep(i,n) {
			gets(s);
			sscanf(s,"%d %d %s",&b[i].x,&b[i].y,t);
			if(t[0] == 'B') b[i].isbird = 1; else b[i].isbird = 0;
		}

		process();
		

		scanf("%d",&m);
		rep(i,m) {
			scanf(" %d %d",&x,&y);
			query(x,y);
		}
	}
	return 0;
}