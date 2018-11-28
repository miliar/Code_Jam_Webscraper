#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<queue>
using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define mabs(x) ( ((x)>0) ? (x) : (-(x)) )
#define SIZE 100005
#define INF 1e10
#define EPS 1e-7
#define i64 __int64

struct Point {
	i64 x,y;
}p[SIZE+5];

i64 c[5][5];

int main() {
	i64 T,A,B,C,D,n,x0,y0,M;
	i64 i,j,k,l,e,f;
	i64 x,y;
	i64 r,kase=1;
	i64 c1,c2,c3;
	scanf("%I64d",&T);
	while(T--) {
		scanf(" %I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&n,&A,&B,&C,&D,&x0,&y0,&M);
		p[0].x = x0, p[0].y = y0;
		x = x0, y = y0;
		for(i=1;i<n;i++) {
			x = (A * x + B) % M;
			y = (C * y + D) % M;
			p[i].x = x, p[i].y = y;
		}

		rep(i,5) rep(j,5) c[i][j] = 0;
		rep(i,n) c[p[i].x % 3][p[i].y % 3]++;

		r = 0;
		rep(i,3) rep(j,3) { //point A
			rep(k,3) rep(l,3) { //point B
				rep(e,3) rep(f,3) { //point C

					
					if((i+k+e)%3==0 && (j+l+f)%3==0) {

						c1 = c[i][j];
						c2 = c[k][l];
						c3 = c[e][f];

						if(k==i && l==j) c2--;
						if(e == k && f == l) c3--;
						if(e == i && f == j) c3--;


						r += c1 * c2 * c3;
					}
				}
			}
		}
		printf("Case #%I64d: %I64d\n",kase++,r/6);
	}
	return 0;
}