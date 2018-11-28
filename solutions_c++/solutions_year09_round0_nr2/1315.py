#include <stdio.h>
#include <string.h>
#include <memory.h>
#define H 111
long map[H][H];
long ans[H][H];
char cur,n;

char rec(long x, long y) {
	if (ans[x][y]) return ans[x][y];

	long mx = x, my = y;
        if (map[x][y-1]<map[mx][my]) {
        	mx = x;
        	my = y-1;
        }
        if (map[x-1][y]<map[mx][my]) {
        	mx = x-1;
        	my = y;
        }
        if (map[x+1][y]<map[mx][my]) {
        	mx = x+1;
        	my = y;
        }
	if (map[x][y+1]<map[mx][my]) {
        	mx = x;
        	my = y+1;
        }
        
        if (mx!=x || my!=y) ans[x][y] = rec(mx,my);
        else ans[x][y] = cur++;

        return ans[x][y];
}

int main(void) {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d\n",&n);
	
	for (long _=1;_<=n;_++) {
		long h,w;
		scanf("%d%d\n",&h,&w);
		for (long j=1;j<=h;j++) {
			for (long i=1;i<=w;i++) scanf("%d",&map[i][j]);
			scanf("\n");
		}			

		
		for (long i=0;i<=w+1;i++) map[i][0] = map[i][h+1] = 999999;
		for (long i=0;i<=h+1;i++) map[0][i] = map[w+1][i] = 999999;
		
		cur = 'a';
		printf("Case #%d:\n",_);
                for (long j=1;j<=h;j++) {
                	for (long i=1;i<=w;i++) printf("%c ",rec(i,j));
                        printf("\n");                
                } 
                memset(ans,0,sizeof(ans));

	}

	return 0;
}

