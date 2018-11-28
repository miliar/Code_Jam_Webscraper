#include <cstdio>
#include <algorithm>
using namespace std;

int a[110],T,n,s,p;

int main()
{
	scanf("%d",&T);
	for (int cases=0;cases<T;++cases){
		scanf("%d%d%d",&n,&s,&p);
		for (int i=0;i<n;++i) scanf("%d",&a[i]);
		sort(a,a+n);
		int ans=0,p1=max(p-1,0),p2=max(p-2,0);
		for (int i=n-1;i>=0;--i){
			if (a[i]>=p+p1+p1) ++ans;
			else if ((a[i]>=p+p2+p2)&&(s>0)) ++ans,--s;
		}
		printf("Case #%d: %d\n",cases+1,ans);
	}
	return 0;
}

