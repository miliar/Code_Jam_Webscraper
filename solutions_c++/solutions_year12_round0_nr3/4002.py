#include <stdio.h>
#include <math.h>

int main() {
	int T, n, m, cnt;
	int g[10];
	
	scanf("%d",&T);
	int x=1;
	while(x<=T) {
		scanf("%d %d",&n,&m);
		
		cnt = 0;
		int p = n;
		int max = 0;
		while(p/10) {
			++max;
			p=p/10;
		}

		for(int i=n;i<=m;++i) {
			int d;
			int h = 0;
			for(int j=1;j<=max;++j) {
				d=pow(10,j);
				int t = (i%d)*pow(10,max-j+1) + i/d;
				
				bool found = false;
				for(int k=0;k<h;++k)
					if(g[k]==t) {
						found = true;
						break;
					}
				if(t>i && t<=m && !found) {
					++cnt;
					g[h++] = t;
				}
			}
		}
		printf("Case #%d: %d\n",x,cnt);
		++x;
	}
	return 0;
}