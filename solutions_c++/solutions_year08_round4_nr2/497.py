#include <cstdio>
#include <string>
using namespace std;

int area,m,n,x2,y2,x3,y3;

bool gao() {
int mn=m*n,a,i;
	for (y2=0;y2<=n;++y2) {
		for (x3=0;x3<=m;++x3) {
			a=y2*x3+area;
			if (a>mn) {
				break;
			}
			for (i=1;i<=m;++i) {
				if ((a%i==0) && (a/i<=n)) {
					x2=i;
					y3=a/i;
					return true;
				}
			}
		}
	}
	return false;
}

int main() {
int z,zz;
	
	for (scanf("%d",&zz),z=1;z<=zz;++z) {
		printf("Case #%d:",z);
		scanf("%d%d%d",&m,&n,&area);
		if (gao()) {
			printf(" 0 0 %d %d %d %d\n",x2,y2,x3,y3);
		}
		else {
			puts(" IMPOSSIBLE");
		}
	}
}
	


	





