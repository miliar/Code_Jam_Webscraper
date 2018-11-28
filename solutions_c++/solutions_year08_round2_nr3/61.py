#include <cstdio>
#include <cstring>
#include <cassert>

#define maxk (1 << 20)

struct rsq {
	int a[maxk * 2];
	
	void add(int v, int dx) {
		for(v += maxk; v > 0; v >>= 1) a[v] += dx;
	}
	
	int sum(int l, int r) {
		if(l >= r) return 0;
		l += maxk;
		r += maxk-1;
		int lsum = a[l], rsum = a[r];
		while(r-l > 1) {
			if((l & 1) == 0) lsum += a[l+1];
			if((r & 1) == 1) rsum += a[r-1];
			l >>= 1; r >>= 1;
		}
		return lsum + rsum;
	}
	
	int find_pos(int sum) {
		int v = 1;
		while(v < maxk) {
			int l = 2*v, r = 2*v+1;
			if(sum <= a[l]) v = l;
			else {
				v = r;
				sum -= a[l];
			}
		}
		return v-maxk;
	}
	
} tree;


int mas[maxk];

int main() {
	int t, tc;
	scanf("%d", &tc);
	for(t = 1; t <= tc; t++) {
		int k, i, j, q, gy;
		scanf("%d", &k);
		int cur = 0, left = k;
		for(i = 0; i < k; i++) tree.add(i, 1);
		memset(mas, -1, sizeof(int)*k);
		for(i = 1; i <= k; i++) {
			int s = tree.sum(0, cur);
			int req = ((i-1) % left) + 1;
//			printf("%d, %d\n", s, req);
			int v;
			if(left - s >= req) v = tree.find_pos(s + req);
			else v = tree.find_pos(req - (left-s));
			assert(v >= 0 && v < k);
			assert(mas[v] == -1);
			tree.add(v, -1);
//			printf("[%d] = %d\n", v, i);
			mas[v] = i;
			left--;
			cur = v;
			
		}
//		for(int i = 0; i < 10; i++) printf("%d ", mas[i]); puts("");
		scanf("%d", &q);
		printf("Case #%d:", t);
		for(i = 0; i < q; i++) {
			scanf("%d", &gy);
//			printf(" %d", gy);
			printf(" %d", mas[gy-1]);
		}
		puts("");
	}
	return 0;
}
