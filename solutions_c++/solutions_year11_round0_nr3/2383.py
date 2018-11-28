#include<stdio.h>
int T;
int seq[1005];
int d1[1000001];
int main()
{
	freopen("largeinput.txt", "r", stdin);
	freopen("largeoutput.txt", "w", stdout);
	int t;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		int N, i, j;

		int xo = 0, min = 0, tot = 0;
		scanf("%d",&N);
		for(i=1;i<=N;i++){ scanf("%d",&seq[i]); xo^=seq[i]; tot += seq[i];}
		if(xo != 0){
			printf("Case #%d: NO\n", t);
			continue;
		}
		min = seq[1];
		for(i=1;i<=N;i++) if(min > seq[i]) min = seq[i];
		printf("Case #%d: %d\n", t, tot - min);
	}

	return 0;
}