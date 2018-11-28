#include<iostream>
#include<algorithm>
#include<cmath>
#include<cassert>
using namespace std;

int a[1000],b[1000];
bool cmp(int x,int y){ return x>y;}
int main()
{	

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out","w",stdout);

	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++){
		printf("Case #%d: ",ii);
		int n;
		scanf("%d",&n);
		int i;
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(i=0;i<n;i++)
			scanf("%d",&b[i]);
		sort(a,a+n);
		sort(b,b+n,cmp);
		__int64 re=0;
		for(i=0;i<n;i++) re+=(__int64)(a[i])*b[i];
		printf("%I64d\n",re);
	}
	return 0;
}