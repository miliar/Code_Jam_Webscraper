// round1.cpp : Defines the entry point for the console application.
//

#include <stdio.h>

int v[2][800],n;

void sort(int d[]) {
	for(int i=0;i<n-1;i++) {
		int k=i;
		for(int j=i+1;j<n;j++) if (d[k]>d[j]) k=j;
		if (k!=i) {
			int swap = d[k];
			d[k]=d[i];
			d[i]=swap;
		}
//		printf("%d ",d[i]);
	}
//	printf(" - sorted.\n");
}
__int64 work() {
	sort(v[0]);
	sort(v[1]);
	__int64 sum1 = 0;
	for(int i=0;i<n;i++) {
		__int64 v1 = v[0][i];
		__int64 v2 = v[1][i];
		sum1 += v1*v2;
	}
	__int64 sum2 = 0;
	for(int i=0;i<n;i++) {
		__int64 v1 = v[0][i];
		__int64 v2 = v[1][n-i-1];
		sum2 += v1*v2;
	}
	return sum1<sum2?sum1:sum2;
}
int main() {
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) {
		scanf("%d",&n);
		for(int j=0;j<2;j++) {
			for(int k=0;k<n;k++) {
				scanf("%d",&v[j][k]);
			}
		}
		printf("Case #%d: %I64d\n",i,work());
	}

	/*
	int tmp;
	scanf("%d",&tmp);
	*/
}