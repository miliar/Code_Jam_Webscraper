#include <cstdio>
#include <cstring>
using namespace std;
const int dir[4][2]={0,1,1,0,1,1,1,-1};

int n,k;
int g[110][110],r[110][110],p[110][110];
char bl[10];

bool inrange(int x) {
	return x>=1 && x<=n;
}

bool lined(int sx,int sy,char ch) {
	int x,y;
	for (int d=0;d<4;d++) {
		x=sx;y=sy;int ans=1;
		while (1) {
			x=x+dir[d][0];
			y=y+dir[d][1];
			if (inrange(x) && inrange(y) && p[x][y]==ch) {
				ans++;
			} else {
				break;
			}
		}
		x=sx;y=sy;
		while (1) {
			x=x-dir[d][0];
			y=y-dir[d][1];
			if (inrange(x) && inrange(y) && p[x][y]==ch) {
				ans++;
			} else {
				break;
			}
		}
		if (ans>=k) return true;
	}
	return false;
}

int main() {
	int cases;
	scanf("%d",&cases);
	for (int dog=1;dog<=cases;dog++) {
		scanf("%d%d",&n,&k);
		gets(bl);
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++) 
				scanf("%c",&g[i][j]);
			gets(bl);
		}
		memset(r,0,sizeof(r));
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++) {
				r[j][n+1-i]=g[i][j];
			}
		}
		memset(p,0,sizeof(p));
		for (int j=1;j<=n;j++) {
			int w=n;
			for (int i=n;i>=1;i--) {
				if (r[i][j]!='.') {
					p[w--][j]=r[i][j];
				}
			}
		}
		
		/*for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++) printf("%c",p[i][j]);
			printf("\n");
		}*/
		
		
		bool bb=false,rr=false;
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++) {
				if (!bb && p[i][j]=='B' && lined(i,j,'B')) bb=true;
				if (!rr && p[i][j]=='R' && lined(i,j,'R')) rr=true;
			}
		printf("Case #%d: ",dog);
		if (bb && rr) printf("Both");
		if (!bb && rr) printf("Red");
		if (bb && !rr) printf("Blue");
		if (!bb && !rr) printf("Neither");
		printf("\n");
	}
}
