#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define MAXN 1100
#define ll long long

int r, k, n, a[MAXN];

bool hash[MAXN];

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("ans.out", "w", stdout);
	int i, j, t, T, cas = 1;
	ll sum, rcnt, rcnt1, cnt, cnt1, p, ans;
	scanf("%d", &T);
	while (T--){
		printf("Case #%d: ", cas++);
		scanf("%d %d %d", &r, &k, &n);
		for (i = 0; i < n; i++){
			scanf("%d", &a[i]);
		}

		memset(hash, false, sizeof(hash));
		
		i = 0;
		rcnt = cnt = 0;
		while (!hash[i]){
			hash[i] = true;
			sum = a[i];
			j = i + 1;
			if (j == n)j = 0;
			while (1){
				if (j == i)break;
				t = j + 1;
				if (t == n)t = 0;
				if (sum + a[j] > k)break;
				sum += a[j];
				j = t;
			}
			rcnt++;
			cnt += sum;
			if (rcnt == r)break;
			i = j;
		}
		if (rcnt == r){
			printf("%lld\n", cnt);
			continue;
		}


		p = i;
		i = 0;
		rcnt1 = cnt1 = 0;
		while (i != p){
			sum = a[i];
			j = i + 1;
			if (j == n)j = 0;
			while (1){
				if (j == i)break;
				t = j + 1;
				if (t == n)t = 0;
				if (sum + a[j] > k)break;
				sum += a[j];
				j = t;
			}
			rcnt1++;
			cnt1 += sum;
			i = j;
		}

		cnt -= cnt1;
		rcnt -= rcnt1;

		ans = cnt1;
		r -= rcnt1;

		ans += cnt * (r / rcnt);
		r %= rcnt;

		i = p;
		rcnt = cnt = 0;
		while (r){
			sum = a[i];
			j = i + 1;
			if (j == n)j = 0;
			while (1){
				if (j == i)break;
				t = j + 1;
				if (t == n)t = 0;
				if (sum + a[j] > k)break;
				sum += a[j];
				j = t;
			}
			rcnt++;
			cnt += sum;
			r--;
			i = j;
		}
		ans += cnt;

		printf("%lld\n", ans);
	}
	return 0;
}

		

				






