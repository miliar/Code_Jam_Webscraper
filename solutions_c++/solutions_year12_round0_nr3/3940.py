#include <iostream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdlib>
#include <cassert>
#include <algorithm>
#include <functional>

#define maxn 3000000

using namespace std;

int used[maxn];
int st[10];

int main(){
	freopen("rand.in", "r", stdin);
	freopen("rand.out", "w", stdout);

	int n, a, b;
	scanf("%d", &n);
	st[0] = 1;
	for(int i = 1; i < 10; ++i)st[i] = st[i - 1] * 10;
	for(int test = 1; test <= n; ++test){
		int ans = 0;
		scanf("%d%d", &a, &b);
		int cc = 0, tmp = a;
		memset(used, 0, sizeof(used));
		while(tmp > 0){
			++cc; tmp /= 10;
		}
		for(int i = a; i <= b; ++i){
			int cur = i;
			for(int j = 1; j <= cc; ++j){
				int mp = cur % 10;
				cur /= 10;
				cur = cur + st[cc - 1] * mp;
				if(cur > i && cur <= b){
					if(used[cur] != i)++ans;
					used[cur] = i;
				}
			}
		}

		printf("Case #%d: %d\n", test, ans);
	}

	return 0;
}
