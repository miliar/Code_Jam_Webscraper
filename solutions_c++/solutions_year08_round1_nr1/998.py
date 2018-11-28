#include <iostream>
#include <algorithm>
using namespace std;

int a[880];
int b[880];

int cmp(int x,int y)
{
	if (x>y)
		return 1;
	else return 0;
}

__int64 ans;

int main()
{
	freopen("A-small-attempt0.out","w",stdout);
	freopen("A-small-attempt0.in","r",stdin);

	int n,T,t,i;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(i=0;i<n;i++)
			scanf("%d",&b[i]);
		sort(a,a+n);
		sort(b,b+n,cmp);
		ans=0;
		for(i=0;i<n;i++){
			ans+=a[i]*b[i];
		}
		printf("Case #%d: %I64d\n",t,ans);
	}
	return 0;
}
