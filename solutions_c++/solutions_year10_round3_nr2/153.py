#include <stdio.h>
#include <string.h>
#include <math.h>

typedef long long LL;

int main(){
	freopen("D:\\B-large.in", "r", stdin);
	freopen("D:\\out1.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int case_t = 1; case_t <= cases; ++case_t){
		LL L, P, C;
		scanf("%lld%lld%lld", &L, &P, &C);
		int res = 0;
		while(L * C < P){
			++res;
			LL low = L, high = P, mid, ans;
			while(low <= high){
				mid = (low + high) >> 1;
				if(mid * mid >= L * P)
					high = mid - 1, ans = mid;
				else
					low = mid + 1;
			}
			P = ans;
		}
		printf("Case #%d: %d\n", case_t, res);
	}
	return 0;
}