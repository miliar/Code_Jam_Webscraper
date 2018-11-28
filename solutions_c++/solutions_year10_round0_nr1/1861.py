#include <stdio.h>
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, t, N, K;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%d%d",&N,&K);
		printf("%s\n",(K+1)%(1<<N)?"OFF":"ON");
	}
	return 0;
}