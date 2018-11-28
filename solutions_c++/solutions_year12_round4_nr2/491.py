#include <stdio.h>
#include <algorithm>
using namespace std;

struct circle{
	int x, y, r, id;
}c[1000];

bool operator<(const circle &a, const circle &b){
	return a.r > b.r;
}

bool cmp(const circle &a, const circle &b){
	return a.id < b.id;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++){
		int n, W, L;
		scanf("%d%d%d", &n, &W, &L);
		for(int i = 0; i < n; i++){
			scanf("%d", &c[i].r);
			c[i].id = i;
		}

		sort(c, c+n);
		int oy = 0;

		int offset = 0;
		int tmp = 0;
		while(offset < n){
			tmp++;
			int tx = c[offset].r;
			c[offset].x = 0;
			c[offset].y = oy;
			int last = n;
			int h = c[offset].r;
			if(tmp > 1)
				h += c[offset].r;
			for(int i = offset+1; i < n; i++){
				if(tx + c[i].r <= W){
					c[i].x = tx + c[i].r;
					c[i].y = oy;
					tx += c[i].r*2;
				}else{
					last = i;
					break;
				}
			}
			offset = last;
			oy += h;
			if(offset != n-1){
				oy += c[offset].r;
			}
		}

		sort(c, c+n, cmp);
		printf("Case #%d:", TT);
		for(int i = 0; i < n; i++){
			printf(" %d %d", c[i].x, c[i].y);
		}
		printf("\n");
	}
}