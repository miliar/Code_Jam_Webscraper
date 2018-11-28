#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX = 1000;

int t, ncas = 0, n;
int v1[MAX], v2[MAX];

int main(){
	scanf("%d", &t);
	while (t--){
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &v1[i]);
		for (int i = 0; i < n; ++i)
			scanf("%d", &v2[i]);
		sort(v1, v1+n);
		sort(v2, v2+n);
		int res=0;
		for (int i = 0, j = n-1; i < n; ++i, --j)
			res += v1[i]*v2[j];
		printf("Case #%d: %d\n", ++ncas, res);
	}
	return 0;
}
