#include <stdio.h>
#include <string.h>

#define MAXN 2000

int a[2][MAXN];
int price[20][MAXN];
int miss[MAXN];

int main(){
	freopen("D:\\B-small-attempt0.in", "r", stdin);
	freopen("D:\\out.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int case_t = 1; case_t <= cases; ++case_t){
		int p, res = 0;
		scanf("%d", &p);
		bool id = false;
		for(int i = 0; i < (1 << p); ++i) scanf("%d", &a[id][i]);
		for(int i = 1; i <= p; ++i)
			for(int j = 1; j <= 1 << (p - i); ++j) scanf("%d", &price[i][j]);
		int x = (1 << (p));
		for(int i = 1; i <= p; ++i){
			int total = 0;
			for(int j = 0; (j + 1) * 2 <= x; ++j){
				if(a[id][j * 2] == 0 || a[id][j * 2 + 1] == 0){
					++res;
				}
				else{
					--a[id][j * 2];
					--a[id][j * 2 + 1];
				}
				if(a[id][j * 2] < a[id][j * 2 + 1]) a[!id][total++] = a[id][j * 2];
				else a[!id][total++] = a[id][j * 2 + 1];
			}
			id = !id;
			x = total;
		}
		printf("Case #%d: %d\n", case_t, res);
	}
	return 0;
}