#include <cstdio>
int abs(int x){
	if(x>0)
		return x;
	else
		return -x;
}
void go(int tc, int n, int m, int a){
	for(int x1=0; x1<=n; x1++){
		for(int y1=0; y1<=m; y1++){
			for(int x2=0; x2<=n; x2++){
				for(int y2=0; y2<=m; y2++){
					int t = x1*y2 - x2*y1;
					if(abs(t) == a){
						printf("Case #%d: 0 0 %d %d %d %d\n",tc,x1,y1,x2,y2);
						return;
					}
				}
			}
		}
	}
	printf("Case #%d: IMPOSSIBLE\n",tc);
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tt=1; tt<=t; tt++){
		int ans=0;
		int a;
		int n,m;
		scanf("%d %d %d\n",&n,&m,&a);
		go(tt,n,m,a);
	}
	return 0;
}