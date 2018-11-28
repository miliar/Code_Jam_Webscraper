#include <cstdio>
#include <algorithm>
#include <cstring>
#include <ctime>
using namespace std;

int C,n,a[1005],v[1005],x,cnt,ret;

int main(){

	scanf("%d", &C);
	for (int tc=1; tc<=C; tc++){
		scanf("%d", &n);
		for (int i=1; i<=n; i++) scanf("%d", &a[i]), v[i] = 0;
		
		ret = 0;
		for (int i=1; i<=n; i++){
			if (v[i]) continue;
			if (i==a[i]) continue;
			x = i;
			cnt = 0;
			while (!v[x]){
				cnt++;
				v[x] = 1;
				x = a[x];
			}
			ret += cnt;
		}
		
		printf("Case #%d: %d\n", tc, ret);
	}

	return 0;
}
