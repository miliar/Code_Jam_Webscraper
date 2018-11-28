#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

bool cmp(int a, int b)
{
	return a>b;
}

int cc, cnt, n;
long long a[1000], b[1000], ans;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int i;
	
	scanf("%d", &cc);
	for(cnt=1; cnt<=cc; cnt++){
		scanf("%d", &n);
		for(i=0; i<n; i++) scanf("%I64d", &a[i]);
		for(i=0; i<n; i++) scanf("%I64d", &b[i]);
		sort(a, a+n);
		sort(b, b+n, cmp);
		ans=0;
		for(i=0; i<n; i++) ans+=a[i]*b[i];
		printf("Case #%d: %I64d\n", cnt, ans);
	}
	
	return 0;
}
