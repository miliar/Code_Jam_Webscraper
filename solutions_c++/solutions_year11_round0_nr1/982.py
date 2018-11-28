#include <cstdio>
#include <cstring>
//#include <iostream>
using namespace std;
const int c=101;
const int inf=1000000000;
const int dx[9]={-1,0,1,-1,0,1,-1,0,1};
const int dy[9]={-1,-1,-1,0,0,0,1,1,1};
int t,ii;
int n;
char s[c];
int d[c];
int a[c][c][c];
struct rec {
	int p,x,y;
	rec (int a=0, int b=0, int c=0) {
		p=a;
		x=b;
		y=c;
	}
};
rec o[c*c*c];
int yr,yw;
inline int in(int x, int y) {
	return x>=1 && x<c && y>=1 && y<c;
}
inline char geth(char &h) {
	do h=getchar(); while (h!='O' && h!='B');
	return h;
}
int main() {
	scanf("%d",&t);
	int i,j,k,w;
	for (ii=1; ii<=t; ++ii) {
		scanf("%d",&n);
		for (i=1; i<=n; ++i) {
			geth(s[i]);
			scanf("%d",&d[i]);
		}
		printf("Case #%d: ",ii);
		for (i=0; i<=n; ++i)
			for (j=1; j<c; ++j)
				for (k=1; k<c; ++k)
					a[i][j][k]=inf;
/*
		for (i=1; i<=n; ++i) cerr << s[i] << ' ';
		cerr << '\n';
		for (i=1; i<=n; ++i) cerr << d[i] << ' ';
		cerr << '\n';
*/
		a[0][1][1]=0;
		yr=0;
		yw=1;
		o[1]=rec(0,1,1);
		rec now,next;
		while (yr<yw) {
			now=o[++yr];
			if (now.p==n) break;
			for (w=0; w<9; ++w) if (in(now.x+dx[w],now.y+dy[w])) {
				next=rec(now.p,now.x+dx[w],now.y+dy[w]);
				if (s[now.p+1]=='B' && d[now.p+1]==next.x && next.x==now.x || s[now.p+1]=='O' && d[now.p+1]==next.y && next.y==now.y)
					next.p++;
				if (a[next.p][next.x][next.y]==inf) {
					a[next.p][next.x][next.y]=a[now.p][now.x][now.y]+1;
					o[++yw]=next;
				}
			}
		}
		printf("%d\n",a[now.p][now.x][now.y]);
	}
	return 0;
}