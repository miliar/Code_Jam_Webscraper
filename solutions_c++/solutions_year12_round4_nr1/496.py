#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

const int maxn = 10010;
int T, n, m, a[maxn], l[maxn], d;
int f[maxn];

int main(){
	scanf("%d",  &T);
	for (int ca = 1; ca <= T; ca++){
		scanf("%d",  &n);
		for (int i = 1; i <= n; i++) scanf("%d%d", a + i, l + i);
		scanf("%d", &d);
		bool flag = false;
		memset(f, 0, sizeof(f));
		f[1] = a[1];
		for (int i = 1; i <= n; i++){
			if (a[i] + f[i] >= d){
				flag = true;
				break;
			}
			for (int j = i + 1; j <= n; j++){
				if (a[i] + f[i] >= a[j]){
					f[j] = max(f[j], min(a[j] - a[i], l[j]));
				}else break;
			}
		}
		printf("Case #%d: %s\n", ca, flag ? "YES" : "NO");
	}
}
