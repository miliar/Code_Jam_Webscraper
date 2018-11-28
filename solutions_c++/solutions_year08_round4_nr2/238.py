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

int main() {
	freopen("B.in","r",stdin);
	int e = 0, T;
	scanf("%d",&T);
	int n, m, a;
	while(T--) {
		scanf("%d%d%d",&n,&m,&a);
		if (n*m < a) {
			printf("Case #%d: IMPOSSIBLE\n",++e);
			continue;
		}
		FOR(by,1,m+1) {
			if (a % by == 0) {
				if (0<= a/by && a/by <= n) {
					printf("Case #%d: %d %d %d %d %d %d\n",++e,0,0,0,by,a/by,0);
					goto end;
				}
			}
		}
		
		FOR(ax,0,n+1) {
			FOR(ay,0,m+1) {
				if(ax!=0 && ay!=0)continue;
				FOR(bx,0,n+1) {
					if(ax==bx && bx!=0)continue;
					FOR(by,0,m+1) {
						if(ay==by && by!=0) continue;
						FOR(cx,0,n+1) {
							int cy = a - (bx*ay-ax*by+cx*by-cx*ay);
							if (ax == bx) {
								if (cy == 0) {
									printf("Case #%d: %d %d %d %d %d %d\n",++e,ax,ay,bx,by,cx,cy);
									goto end;
								}
							} else {
								if (cy % (ax - bx) == 0) {								
									cy/= (ax-bx);
									if (0<= cy && cy <= m) {
										printf("Case #%d: %d %d %d %d %d %d\n",++e,ax,ay,bx,by,cx,cy);
										goto end;
									}
								}
							}
						}
					}
				}
			}
		}
		printf("Case #%d: IMPOSSIBLE\n",++e);
		continue;
		end:;
	}
	return 0;
}