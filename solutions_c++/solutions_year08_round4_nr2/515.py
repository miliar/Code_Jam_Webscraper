#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		int n,m,a; scanf("%d%d%d",&n,&m,&a);
		printf("Case #%d: ",tt);
		bool fin=false;
		for (int y1=0; y1<=m; y1++){
			for (int x2=0; x2<=n; x2++){
				for (int x3=0; x3<=n; x3++){
					for (int y3=0; y3<=m; y3++){
						int x1=0,y2=0;
						int area= x1*y2+x2*y3+x3*y1 - x2*y1 - x3*y2 - x1*y3;
						if (abs(area)==a){
							printf("%d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);
							fin=true;
						}
						if (fin) break;
					}
					if (fin) break;
				}
				if (fin) break;
			}
			if (fin) break;
		}
		if (!fin) printf("IMPOSSIBLE\n");
	}
	return 0;
}
