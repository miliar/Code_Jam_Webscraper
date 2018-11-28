#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
typedef long long INT;

int f[1001][1001],T;
INT L,P,C;

int log(INT n)
{
	INT t = 1;
	int s = 0;
	while(t < n)
		s++,t *= C;
	return s;
}

int two(int n)
{
	int i;
	for(i = 0;(1 << i) < n;i++);
	return i;
}

inline int get(int L,int P)
{
	int n = log(P%L == 0 ? P/L : P/L + 1);
	return two(n);
}


int main()
{
	int i,j,k;
	//freopen("B-large.in","r",stdin);
	//freopen("B.out","w",stdout);
	scanf("%d",&T);
	for(int Case = 1;Case <= T;Case++)
	{
		scanf("%lld%lld%lld",&L,&P,&C);
		printf("Case #%d: %d\n",Case,get(L,P));
	}
	return 0;
}
