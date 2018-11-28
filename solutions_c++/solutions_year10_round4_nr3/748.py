#include <cstdio>
#include <cstring>
#define h 111

int t,c,r,x1,y1,x2,y2,i,j,k,s,d,a[2][h][h],q;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for(c=1;c<=t;c++) {
		memset(a, 0, sizeof a);
		scanf("%d", &r);
		for(k=0;k<r;k++) {
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for(i=x1;i<=x2;i++)
				for(j=y1;j<=y2;j++)
					a[0][i][j] = 1;
		}
		d = 0;
		for(i=1;i<h;i++)
			for(j=1;j<h;j++)
				d += a[0][i][j];
		q = 0;
		s = 0;
		while(d) {
			d = 0;
			for(i=1;i<h;i++)
				for(j=1;j<h;j++) {
					a[q^1][i][j] = a[q][i][j];
					if(a[q][i][j])
						d ++;
					if(a[q][i][j] && !a[q][i-1][j] && !a[q][i][j-1]) {
						a[q^1][i][j] = 0;
						d --;
					} else
					if(!a[q][i][j] && a[q][i-1][j] && a[q][i][j-1])
						a[q^1][i][j] = 1;
				}
			q ^= 1;
			s ++;
		}
		printf("Case #%d: %d\n", c, s);
	}
}