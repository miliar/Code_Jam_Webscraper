#include <stdio.h>
#include <string.h>

#define MAX 110

char boa[2][MAX][MAX];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n;
		scanf("%d",&n);
		memset(boa,0,sizeof(boa));
		for(int i=0;i<n;++i) {
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int x=x1;x<=x2;++x)
				for(int y=y1;y<=y2;++y)
					boa[0][x][y]=1;
		}
		int ans;
		int prv=0;
		int cnt=0;
		for(int i=0;i<MAX;++i)
			for(int j=0;j<MAX;++j)
				cnt+=boa[prv][i][j];
		for(ans=0;cnt>0;++ans) {
			int nxt=prv^1;
			memset(boa[nxt],0,sizeof(boa[nxt]));
			for(int i=0;i<MAX;++i)
				for(int j=0;j<MAX;++j)
					if(boa[prv][i][j]) {
						if((!i || !boa[prv][i-1][j]) && (!j || !boa[prv][i][j-1])) {
							boa[nxt][i][j]=0;
							--cnt;
						}
						else
							boa[nxt][i][j]=1;
					}
					else {
						if((i>0 && boa[prv][i-1][j]) && (j>0 && boa[prv][i][j-1])) {
							boa[nxt][i][j]=1;
							++cnt;
						}
						else
							boa[nxt][i][j]=0;
					}
			prv=nxt;
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
