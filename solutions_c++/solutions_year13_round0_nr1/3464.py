#include <cstdio>
#include <string>
#include <cstring>
#define n 4
using namespace std;
char a[4][4];

int main() {
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int T,Ti;
	scanf("%d",&T);
	for(Ti=1;Ti<=T;Ti++) {
		int i,j;
		for(i=0;i<n;i++) {
			strset(a[i],0);
		}
		for(i=0;i<n;i++) {
			scanf("%s",a[i]);
		}
		int x=0,o=0,uf=0;
		for(i=0;i<n;i++) {
			x=0,o=0;
			for(j=0;j<n;j++) {
				if(a[i][j]=='X') x++;
				else if(a[i][j]=='O') o++;
				else if(a[i][j]=='T') x++,o++;
				else if(a[i][j]=='.') uf=1;
			}
			if(x==4) {
				printf("Case #%d: X won\n",Ti);
				break;
			} else if(o==4) {
				printf("Case #%d: O won\n",Ti);
				break;
			}
		}
		if(i<n) continue;
		for(i=0;i<n;i++) {
			x=0,o=0;
			for(j=0;j<n;j++) {
				if(a[j][i]=='X') x++;
				else if(a[j][i]=='O') o++;
				else if(a[j][i]=='T') x++,o++;
			}
			if(x==4) {
				printf("Case #%d: X won\n",Ti);
				break;
			} else if(o==4) {
				printf("Case #%d: O won\n",Ti);
				break;
			}
		}
		if(i<n) continue;
		x=0,o=0;
		for(i=0;i<n;i++) {
			if(a[i][i]=='X') x++;
			else if(a[i][i]=='O') o++;
			else if(a[i][i]=='T') x++,o++;
		}
		if(x==4) {
			printf("Case #%d: X won\n",Ti);
			continue;
		} else if(o==4) {
			printf("Case #%d: O won\n",Ti);
			continue;
		}
		x=0,o=0;
		for(i=0;i<n;i++) {
			if(a[i][3-i]=='X') x++;
			else if(a[i][3-i]=='O') o++;
			else if(a[i][3-i]=='T') x++,o++;
		}
		if(x==4) {
			printf("Case #%d: X won\n",Ti);
			continue;
		} else if(o==4) {
			printf("Case #%d: O won\n",Ti);
			continue;
		} else if(uf) {
			printf("Case #%d: Game has not completed\n",Ti);
		} else {
			printf("Case #%d: Draw\n",Ti);
		}
	}
	return 0;
}