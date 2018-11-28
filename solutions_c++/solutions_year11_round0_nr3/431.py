#include <stdio.h>
char sol[128];
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T, n;
	scanf("%d",&T);
	while(T>0){T--;
		scanf("%d",&n);
		int i, mn, C, X = 0, sum = 0;
		for(i=0;i<n;i++){
			scanf("%d" ,&C);
			if(i == 0 || mn > C) mn = C;
			X ^= C;
			sum += C;
		}
		if(X != 0) sprintf(sol, "NO");
		else sprintf(sol, "%d", sum-mn);
		static int cs = 1;
		printf("Case #%d: %s\n", cs++, sol);

	}
	return 0;
}