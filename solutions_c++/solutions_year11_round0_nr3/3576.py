#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX = 1001;

int t, c[MAX], n, sum, total;

int main(){
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++cas){
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &c[i]);
		sort(c, c+n);
		sum = total = 0;
		for (int i = 1; i < n; ++i){
			sum = sum ^ c[i];
			total += c[i];
		}
		if (sum == c[0])
			printf("Case #%d: %d\n", cas, total);
		else
			printf("Case #%d: NO\n", cas);
	}
	return 0;
}
