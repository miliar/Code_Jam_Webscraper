#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define x first
#define y second

const int N = 536;
LL a[N][N];
LL b[N][N];
LL z[N][N];
char s[N][N];

LL sumx(int sx,int sy,int ex,int ey) {
	return a[ex][ey] - a[sx-1][ey] - a[ex][sy-1] + a[sx-1][sy-1];
}
LL sumy(int sx,int sy,int ex,int ey) {
	return b[ex][ey] - b[sx-1][ey] - b[ex][sy-1] + b[sx-1][sy-1];
}
int r, c;

bool chk(int x,int y,int k) {
	if(x+k-1>r || y+k-1>c) return 0;
	LL xm=sumx(x,y,x+k-1,y+k-1);
	LL ym=sumy(x,y,x+k-1,y+k-1);
	int xa[]={x,x,x+k-1,x+k-1};
	int ya[]={y,y+k-1,y,y+k-1};
	LL wei = z[x+k-1][y+k-1] - z[x+k-1][y-1] - z[x-1][y+k-1] + z[x-1][y-1];
	FOR(i,0,4) {
		int w=s[xa[i]][ya[i]]-'0';
		xm-=w*xa[i];
		ym-=w*ya[i];
		wei -= w;
	}
//	FOR(i,0,4) printf("[%d %d]\n", xa[i],ya[i]);
//	printf("[%d %d %d %d]\n",x,y,x+k-1,y+k-1);
//	printf("%d %d %d\n", x, y, k);
//		printf("wei=%lld\n", wei);
//	if(xm<0) printf("%lld\n", xm);
//	if(ym<0) printf("%lld\n", ym);
	while(xm<0);
	while(ym<0);
	int d=k/2;
	if(k%2==1) {
		if((LL)(x+d)*(wei)==xm && (LL)(y+d)*(wei)==ym)
			return 1;
	}else{
		if((LL)(2*x+2*d-1)*(wei)==xm*2)
		if((LL)(2*y+2*d-1)*(wei)==ym*2)
			return 1;
	}
	return 0;
}

int main() {
	int T,ca=0;
	scanf("%d", &T);
	while (T--) {
		int d;
		scanf("%d%d%d",&r,&c,&d);
		FOR(i,0,r) scanf("%s",s[i+1]+1);
		CLR(a);
		CLR(b);
		CLR(z);
		FOE(i,1,r) FOE(j,1,c) {
			int x = s[i][j] - '0';
			a[i][j] = a[i][j-1] + a[i-1][j] - a[i-1][j-1] + i*x;
			b[i][j] = b[i][j-1] + b[i-1][j] - b[i-1][j-1] + j*x;
			z[i][j] = z[i][j-1] + z[i-1][j] - z[i-1][j-1] + x;
		}
		int ans = 0;
		for(int k=min(r,c);k>=3;k--) if(ans==0) {
			bool ok = 0;
			FOR(i,1,r) FOE(j,1,c) if(!ok) {
				if(chk(i,j,k)) {
					ok  = 1;
					ans = k;
					break;
				}
			}
		}

		printf("Case #%d:", ++ca);
		if(ans==0) puts(" IMPOSSIBLE");
		else printf(" %d\n", ans);
	}
	return 0;
}
