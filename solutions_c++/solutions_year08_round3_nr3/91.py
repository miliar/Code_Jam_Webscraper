// c3.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
int n,m;
__int64 X,Y,Z;

int d[500000];
int A[100];
void generate() {
	//printf("[%d %d %d %d %d\n",n,m,X,Y,Z);
	//for(int i=0;i<m;i++) printf("-%d\n",A[i]);
	for(int i=0;i<n;i++) {
		d[i] = A[i % m];
		//printf("%d ",d[i]);
		A[i % m] =  (X * A[i % m] + Y * (i + 1)) % Z;
		//for(int i=0;i<m;i++) printf("-%d\n",A[i]);
	}
	//printf(" | %d\n",n);
}

int max[500000];
int work() {
	max[0]=1;
	for(int i=1;i<n;i++) {
		int c = 1;
		for(int j=0;j<i;j++) {
			if (d[j]<d[i]) c=(c+max[j])%1000000007;
		}
		max[i]=c % 1000000007;
		//printf("%d ",max[i]);
	}
	//printf("]]\n");
	__int64 sum = 0;
	for(int i=0;i<n;i++) {
		sum += max[i];
		sum %= 1000000007;
	}
	return (int)sum;
}


int main() {
	int N;
	scanf("%d",&N);
	for(int i=1;i<=N;i++) {
		scanf("%d %d %d %d %d",&n,&m,&X,&Y,&Z);
		for(int j=0;j<m;j++) scanf("%d",A+j);
		generate();
		printf("Case #%d: %d\n",i,work());
	}
}
