#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

#define MAXN 60

double x[MAXN], v[MAXN], b, t;
int n, k;
int s[MAXN];

int main(){
	freopen("/home/liang/桌面/B-large.in", "r", stdin);
	freopen("ans.out", "w", stdout);
	int i, j, k;
	int T, cas  = 1;
	scanf("%d", &T);
	while (T--){
		scanf("%d %d %lf %lf", &n, &k, &b, &t);
		for (i = 1; i <= n; i++){
			scanf("%lf", &x[i]);
		}
		for (i = 1; i <= n; i++){
			scanf("%lf", &v[i]);
		}

		for (i = 1; i <= n; i++){
			if ((b - x[i]) / v[i] > t){
				s[i] = 0;
			}
			else s[i] = 1;
		}

		if (k == 0){
			printf("Case #%d: 0\n", cas++);
			continue;
		}

		int sum = 0;
		for (i = n; i >= 1; i--){
			sum += s[i];
			if (sum >= k)break;
		}
		if (sum < k){
			printf("Case #%d: IMPOSSIBLE\n", cas++);
			continue;
		}

		int ans = 0;
		sum = 0;
		for (j = i; j <= n; j++){
			if (s[j]){
				sum++;
			}
			else ans += sum;
		}
		printf("Case #%d: %d\n", cas++, ans);
	}
	return 0;
}


