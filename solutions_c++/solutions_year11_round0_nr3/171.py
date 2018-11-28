#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int C,n,S,X,a[1005],ret;

int main(){

	scanf("%d", &C);
	for (int tc=1; tc<=C; tc++){
		scanf("%d", &n);
		S = X = 0;
		for (int i=0; i<n; i++){
			scanf("%d", &a[i]);
			S += a[i];
			X ^= a[i];
		}
		
		sort(a, a+n);
		ret = -1;
		for (int i=n-1; i>=0; i--){
			if ((X^a[i])==a[i]) ret = S-a[i];
		}
		
		printf("Case #%d: ", tc);
		if (ret==-1) printf("NO\n");
		else printf("%d\n", ret);
		
	}

	return 0;
}
