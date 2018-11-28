#include <cstdio>

int data[10000][2];

int test() {
	int n;
	scanf("%d", &n);
	int res = 0;
	for (int i=0;i<n;i++) {
		scanf("%d%d", &(data[i][0]), &(data[i][1]));
		for (int j=0;j<i;j++) {
			if (data[i][0] < data[j][0] && data[i][1]>data[j][1]) res++;
			if (data[i][0] > data[j][0] && data[i][1]<data[j][1]) res++;
		}
	}
	return res;
}

main() {
	int z;
	scanf("%d", &z);
	for (int i=0;i<z;i++) 
		printf("Case #%d: %d\n", i+1, test());
}
