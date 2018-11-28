#include <cstdio>
#include <map>
using namespace std;

int H,W;
int v[100][100],chk[100][100];
pair <int,int> ans[100][100];

pair <int,int> f(int x, int y) {
	int best=0,xx,yy,i,dx[]={-1,0,0,1},dy[]={0,-1,1,0};
	
	chk[x][y] = 1;
	for (i=0;i<4;i++) if (x+dx[i] >= 0 && x+dx[i] < H && y+dy[i] >= 0 && y+dy[i] < W) {
		if (v[x][y] - v[x+dx[i]][y+dy[i]] > best) best = v[x][y] - v[x+dx[i]][y+dy[i]], xx = x+dx[i], yy = y+dy[i];
	}
	return ans[x][y] = best ? f(xx,yy) : make_pair(x,y);
}

int main() {
	int T,cnt,i,j,testcase;
	map < pair <int,int>, int > m;
	
	scanf("%d",&T);
	for (testcase=1;testcase<=T;testcase++) {
		scanf("%d %d",&H,&W);
		m.clear();
		for (i=0;i<H;i++) for (j=0;j<W;j++) scanf("%d",&v[i][j]), chk[i][j] = 0;
		for (i=0;i<H;i++) for (j=0;j<W;j++) if (!chk[i][j]) f(i,j);
		for (i=0,cnt=0;i<H;i++) for (j=0;j<W;j++) if (m.find(ans[i][j]) == m.end()) m[ans[i][j]] = cnt++;
		
		printf("Case #%d:\n",testcase);
		for (i=0;i<H;i++) {
			for (j=0;j<W;j++) {
				if (j) printf(" ");
				printf("%c",'a'+m[ans[i][j]]);
			}
			puts("");
		}
	}
	
	return 0;
}
