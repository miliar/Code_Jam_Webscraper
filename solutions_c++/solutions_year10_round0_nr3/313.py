#include <stdio.h>
#include <string.h>
#define MAXN 1001

typedef long long LL;

LL g[MAXN], sum[MAXN], v[MAXN];
int pos[MAXN];

int bs(int low, int high, LL val){
	int res = 0;
	while(low <= high){
		int mid = (low + high) >> 1;
		if(sum[mid] <= val)
			res = mid, low = mid + 1;
		else
			high = mid - 1;
	}
	return res;
}

int main(){
	freopen("D:\\C-large.in", "r", stdin);
	freopen("D:\\C-large-attempt0.out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int case_t = 1; case_t <= cases; ++case_t){
		int r, n;
		LL k;
		scanf("%d%lld%d", &r, &k, &n);
		for(int i = 1; i <= n; ++i){
			scanf("%lld", g + i);
			sum[i] = sum[i - 1] + g[i];
		}
		memset(pos, -1, sizeof(pos));
		int curr = 1, next, total = 0, c, remain;
		LL ans = 0, cx, temp;
		while(total < r){
			if(pos[curr] != -1){
				c = total + 1 - pos[curr];
				remain = r - total;
				cx = ans - v[pos[curr] - 1];
				ans += cx * (remain / c);
				remain %= c;
				ans += v[pos[curr] + remain - 1] - v[pos[curr] - 1];
				break;
			}
			++total;
			pos[curr] = total;
			if(sum[n] - sum[curr - 1] >= k) next = bs(curr, n, k + sum[curr - 1]), temp = sum[next] - sum[curr - 1], v[total] = v[total - 1] + temp;
			else{
				next = bs(1, curr - 1, k - sum[n] + sum[curr - 1]), temp = sum[n] - sum[curr - 1] + sum[next], v[total] = v[total - 1] + temp;
				if(next < 1) next = n;
			}
			ans = v[total];
			curr = next + 1;
			if(curr == n + 1) curr = 1;
		}
		printf("Case #%d: %lld\n", case_t, ans);
	}
	return 0;
}