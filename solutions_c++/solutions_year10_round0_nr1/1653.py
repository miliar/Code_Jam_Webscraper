/*#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
	int n=4;
	int m=47;
	vector<int> a(n);
	printf("Step %d: ",0);
	for(int i=0; i<n; i++)
		printf("%d ",a[i]);
	printf("\n");
	for(int i=1; i<=m; i++){
		int x = 0;
		while(x<n && a[x]==1)
			x++;
		for(int i=0; i<=min(x,n-1); i++)
			a[i] = 1-a[i];
		printf("Step %d: ",i+1);
		for(int i=0; i<n; i++)
			printf("%d ",a[i]);
		printf("\n");
	}
	return 0;
}*/
#include <cstdio>
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tc=1; tc<=t; tc++){
		long long  n,k;
		scanf("%lld %lld\n",&n,&k);
		k++;
		long long ans = 1;
		for(int i=1; i<=n; i++)
			ans*=2;
		bool ok = false;
		if(k%ans==0)
			ok=true;
		printf("Case #%d: %s\n",tc,ok?"ON":"OFF");
	}
	return 0;
}