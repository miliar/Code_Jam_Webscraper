#include <iostream>

using namespace std;

int r;
int b[102][102];
int b2[102][102];

int main() {
	//freopen("bacteria.in","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int tests;
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++) {
		memset(b,0,sizeof(b));
		scanf("%d",&r);
		for (int i=0;i<r;i++) {
			int x1,y1,x2,y2;
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for (int y=y1;y<=y2;y++) for (int x=x1;x<=x2;x++) b[y][x]=1;
		}
		int t=0,cnt=1;
		while (cnt>0) {
			cnt=0;
			for (int y=1;y<=100;y++) for (int x=1;x<=100;x++) {
				if (b[y][x]==1) {
					if (b[y-1][x]==0 && b[y][x-1]==0) b2[y][x]=0;
					else b2[y][x]=1;
				} else {
					if (b[y-1][x]==1 && b[y][x-1]==1) b2[y][x]=1;
					else b2[y][x]=0;
				}
				cnt+=b2[y][x];
			}
			memcpy(b,b2,sizeof(b2));
			t++;
		}
		printf("Case #%d: %d\n",test,t);
	}
    return 0;
}
