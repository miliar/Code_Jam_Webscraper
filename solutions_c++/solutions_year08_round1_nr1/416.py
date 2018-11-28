#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))

const int maxn=1000;
int cas;

int n;

__int64 a[maxn],b[maxn];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&cas);
	int lv,i;
	for(lv=1;lv<=cas;lv++) {
		__int64 ans=0;
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%I64d",&a[i]);
		for(i=0;i<n;i++) scanf("%I64d",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		for(i=0;i<n;i++) ans+=a[i]*b[n-1-i];
		printf("Case #%d: %I64d\n",lv,ans);
		fprintf(stderr,"Case #%d: %I64d\n",lv,ans);
	}
	return 0;
}