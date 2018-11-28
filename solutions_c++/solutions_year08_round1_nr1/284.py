#include <cstdio>
#include <algorithm>
using namespace std;

__int64 a[10000],b[10000];

bool cmp1(const __int64 &a,const __int64 &b){
	return a<b;
}

bool cmp2(const __int64 &a,const __int64 &b){
	return a>b;
}

int main() {
int z,zz,i,n;
__int64 j;
	freopen("d:\\in","r", stdin);
    freopen("d:\\out","w",stdout);


	for (scanf("%d",&zz),z=1;z<=zz;++z){
		scanf("%d",&n);
		for (i=0;i<n;++i){
			scanf("%I64d",&a[i]);
		}
		for (i=0;i<n;++i){
			scanf("%I64d",&b[i]);
		}
		sort(a,a+n,cmp1);
		sort(b,b+n,cmp2);
		j=0;
		for (i=0;i<n;++i) {
			j+=a[i]*b[i];
		}
		printf("Case #%d: %I64d\n",z,j);
	}
	return 0;
}

