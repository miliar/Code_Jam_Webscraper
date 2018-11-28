#include <stdio.h>

int n;
int A[3000];
int B[3000];

bool inter(int i,int i2) {
	return (A[i]>A[i2])^(B[i]>B[i2]);
}

int main() {
	int id=1;int t;scanf("%d",&t);
	while(t--) {
		int wyn=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++) {
			scanf("%d %d",&A[i],&B[i]);
		}
		for(int i=0;i<n;i++) for(int i2=i+1;i2<n;i2++) {
			if(inter(i,i2)) {
				wyn++;
			}
		}
		printf("Case #%d: %d\n",id++,wyn);
	}
	return 0;
}
