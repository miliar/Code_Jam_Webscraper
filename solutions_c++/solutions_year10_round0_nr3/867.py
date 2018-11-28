#include <cstdio>

typedef long long int lld;

int r,k,n;
int que[1000];
int next[1000];
int price[1000];
int cyclelen[1000];
lld cycleprice[1000];

void test(int caze) {
	scanf("%d%d%d", &r, &k, &n);
	for (int i=0;i<n;i++) scanf("%d", &(que[i]));
	for (int i=0;i<n;i++) {
		int sum = 0;
		int j=0;
		for (; j<n && sum+que[(i+j)%n]<=k; j++) sum += que[(i+j)%n];
		next[i] = (i+j)%n;
		price[i] = sum;
		cyclelen[i]=cycleprice[i]=0;
		//printf("pos %d, next %d, price %d\n", i, next[i], price[i]);
	}
	int pos = 0;
	lld sum = 0;
	int step = 1;
	while (r>0 && cyclelen[pos]==0) {
		r--;
		cyclelen[pos] = step++;
		cycleprice[pos] = sum;
		//printf("cycle[%d] = %d, %d\n", pos, step-1, sum);
		sum += price[pos];
		pos = next[pos];
	}
	if (cyclelen[pos]) {
		//printf("from %d r=%d cycle %d price %lld\n",pos,r, step-cyclelen[pos], sum-cycleprice[pos]);
		sum += ((lld)(r / (step-cyclelen[pos]))) * (sum-cycleprice[pos]);
		r %= step-cyclelen[pos];
	}
	//printf("r = %d\n", r);
	while (r>0) {
		r--;
		sum += price[pos];
		pos = next[pos];
	}
	printf("Case #%d: %lld\n", caze+1, sum);
}

main() {
	int z;
	scanf("%d", &z);
	for (int i=0;i<z;i++) test(i);
}

