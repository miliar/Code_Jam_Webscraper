#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int main(){
	freopen("in", "rt", stdin);
	freopen("out", "wt", stdout);
	int ntest, n, k;
	char q;
	int a[50], u;
	scanf("%d", &ntest);
	for (int itest=0; itest<ntest; ++itest){
		scanf("%d\n", &n);
		for (int i=0; i<n; ++i){
			a[i] = 0;
			for (int j=0; j<n; ++j){
				scanf("%c", &q);
				if (q == '1') a[i] = j+1;
			}
			scanf("\n");
		}
		printf("Case #%d: ", itest+1);
		int ans = 0;
		for (int i=0; i<n; ++i){
			k=n-1;
			for (int j=n-2; j>=i; --j)
				if (a[j]<=i+1) k = j;
			for (int j=k-1; j>=i; --j){
				++ans;
				u = a[j];
				a[j] = a[j+1];
				a[j+1] = u;
			}		
		}
		printf("%d\n", ans);	
	}
	return 0;
}