#include <cstdio>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

int ans[1005],mark[1005];
int a[1005],n,k;

int gao(int &i) {
int j,x=i;
	for (j=0;;) {
		if (j+a[i]>k) {
			break;
		}
		j+=a[i];
		if (++i==n) {
			i=0;
		}
		if (x==i) {
			break;
		}
	}
	return j;
}


int main() {
int z,zz,r,i,at,j,p;
__int64 res,temp,m,t;
	freopen("d:\\in.in","r",stdin);
	freopen("d:\\out","w",stdout);
	scanf("%d",&zz);
	for (z=1;z<=zz;++z) {
		scanf("%d%d%d",&r,&k,&n);
		for (i=0;i<n;++i) {
			scanf("%d",&a[i]);
		}
		memset(mark,0,sizeof(mark));
		res=0;
		for (at=0,i=1;i<=r;++i) {
			ans[i]=gao(j=at);
			res+=ans[i];
			mark[at]=i;
			if (mark[j]) {
				break;
			}
			at=j;
			
		}
		printf("Case #%d: ",z);

		if (i>=r) {
			printf("%I64d\n",res);
			continue;
		}
		
		//ans[mark[j]]=ans[i+1];
		
		res=0;
		for (p=1;p<mark[j];++p) {
			res+=ans[p];
		}
		t=i-mark[j]+1;
		m=(r-mark[j]+1)/t;
		temp=0;
		for (p=mark[j];p<=i;++p) {
			temp+=ans[p];
		}
		
		r=(r-mark[j]+1)%t;
		for (p=0;p<r;++p) {
			res+=ans[mark[j]+p];
		}
		res+=m*temp;
		printf("%I64d\n",res);	

	}
	return 0;
}
