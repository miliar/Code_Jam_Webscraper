#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <queue>
#include <map>
#include <stack>
using namespace std;

int main(){
	
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int n;
	int T;
	int num[1005];
	int cas = 1;
	int i;
	
	scanf("%d", &T);

	while (T --){
		int sum1 = 0; 
		int ans = 0;

		scanf("%d", &n);
		for (i = 0; i < n; i ++){
			scanf("%d", &num[i]);
			sum1 += num[i];
			ans ^= num[i];
		}

		sort(num, num+n);
		int an = 0;
		int sum2 = 0;

		for (i = 0; i < n; i++){
			ans ^= num[i];
			an ^= num[i];
			sum2 += num[i];
			if (ans == an)
				break;
		}
		if (i == n)
			printf("Case #%d: NO\n", cas++);

		else{
			printf("Case #%d: %d\n", cas++, sum2 > (sum1-sum2)?sum2:(sum1-sum2));
		}

	}

	return  0;
}
