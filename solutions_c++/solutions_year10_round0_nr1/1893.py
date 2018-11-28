#include <cstdio>

int A[31];
int T;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outzz.txt","w",stdout);
	int i;
	int N,K;
	A[1] = 1;
	for(i = 2; i <= 30; ++ i)
		A[i] = A[i - 1] * 2 + 1;
	scanf("%d",&T);
	for(i = 1; i <= T; ++ i)
	{
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",i);
		if(K < A[N]) {puts("OFF");continue;}
		if(0 == (K + 1) %(A[N] + 1)) puts("ON");
		else puts("OFF");
	}
	return 0;
}