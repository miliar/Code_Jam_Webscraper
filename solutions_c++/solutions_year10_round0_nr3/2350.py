#include <cstdio>
#include <cstring>

int r, k, n, arr[1010], start[1010];

int main() {
	freopen("small.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int nca;
	scanf("%d", &nca);
	for (int ii = 1; ii <= nca; ii++) {
		scanf("%d%d%d", &r, &k, &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &arr[i]);
		int sum = 0, tem=0;
		int i, j, s=0;
		for(i=0;i<r;i++){
			j=s;
			tem=0;
			while(tem <= k){
				tem+=arr[j];
				j=(j+1)%n;
				if(j==s)break;
			}
			if(j!=s||tem>k){
				if(j==0)j=n-1;
				else j--;
				sum+=tem-arr[j];
			}
			else sum+=tem;
			s=j;
		}
		printf("Case #%d: %d\n", ii, sum);
	}
	return 0;
}