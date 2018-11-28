#include <iostream>

using namespace std;

int a[50],ok[50];

void swap(int i,int j){
	int tmp = a[i]; a[i] = a[j]; a[j] = tmp;
}

int main(){
	freopen("A.in","r",stdin); freopen("A.out","w",stdout);
	int t1,t2 = 0;
	scanf("%d\n",&t1);
	while (t1){
		t1--; t2++;
		printf("Case #%d: ",t2);
		int n;
		scanf("%d\n",&n);
		for (int i=1; i<=n; ++i){
			ok[i] = 1;
			char tmp;
			for (int j=1; j<=n; ++j){
				scanf("%c",&tmp);
				if (tmp == '1') ok[i] = j;
			}
			scanf("\n");
		}
		for (int i=1; i<=n; ++i)
			a[i] = i;
		int ans = 0;
		for (int i=1; i<=n; ++i)
			for (int j=i; j<=n; ++j)
				if (ok[a[j]] <=i){
					for (int k = j; k>i; k--)
						swap(k,k-1);
					ans += j-i;
					break;
				}
		printf("%d\n",ans);
	}
}
