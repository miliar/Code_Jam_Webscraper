#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int a[1200], n;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int it = 1;it <= T; ++it){
		scanf("%d",&n);
		for(int i = 0;i < n; ++i) scanf("%d",&a[i]);
		sort(a,a+n);
		int b = 0, sum = 0;
		for(int i = 0;i < n; ++i){
			b ^= a[i];
			sum += a[i];
		}
		printf("Case #%d: ",it);
		if(b != 0)  printf("NO\n");
		else{
			if(n == 1) printf("NO\n");
			else	printf("%d\n",sum-a[0]);
		}
	}
	
}
