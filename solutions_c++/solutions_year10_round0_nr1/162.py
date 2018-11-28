#include <stdio.h>
#include <string.h>

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,t,n,k,s;
	scanf("%d",&T);
	for (t = 1;t <= T;t++){
		scanf("%d%d",&n,&k);
		s = 1 << n;
		printf("Case #%d: O%s\n",t,((k+1) % s)?"FF":"N");
	}
	fclose(stdout);
}
