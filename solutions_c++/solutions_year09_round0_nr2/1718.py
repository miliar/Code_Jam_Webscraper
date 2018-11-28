#include <cstdio>
#include <cstring>
#pragma comment(linker,"/STACK:10000000")
const int c=110;
const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};
char a[c][c];
char res[c][c];
int t,h,w;
char now,label;
bool in(int x, int y) {
	return x>=1 && x<=h && y>=1 && y<=w;
}
void go(int x, int y) {
	if (res[x][y]>0) {
		label=res[x][y];
		return;
	}
	int i,j;
	j=-1;
	for (i=0; i<4; ++i) if (in(x+dx[i],y+dy[i]) && a[x+dx[i]][y+dy[i]]<a[x][y] &&
		(j==-1 || a[x+dx[i]][y+dy[i]]<a[x+dx[j]][y+dy[j]])) j=i;
   	if (j<0) label=++now; else go(x+dx[j],y+dy[j]);
   	res[x][y]=label;
}
int main() {
	int ii,i,j;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		scanf("%d%d",&h,&w);
		for (i=1; i<=h; ++i)
			for (j=1; j<=w; ++j)
				scanf("%d",&a[i][j]);
		memset(res,0,sizeof(res));
		now='a'-1;
		for (i=1; i<=h; ++i)
			for (j=1; j<=w; ++j) {
				go(i,j);
			}
		printf("Case #%d:\n",ii);
		for (i=1; i<=h; ++i) {
			for (j=1; j<=w; ++j) printf("%c ",res[i][j]);
			printf("\n");
		}
	}
	return 0;
}