#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int MAXN =1050;
int n,l[MAXN],p[MAXN],ind[MAXN];
bool cmp(const int&a,const int&b)
{
	int ta=l[a]*p[a];
	int tb=l[b]*p[b];
	if (ta!=tb) return ta>tb;
	return a<b;
}
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		scanf("%d",&n);
		for (int i=0;i<n;i++) scanf("%d",&l[i]);
		for (int i=0;i<n;i++) scanf("%d",&p[i]);
		printf("Case #%d: ",tcase);
		for (int i=0;i<n;i++) ind[i]=i;
		sort(ind,ind+n,cmp);
		for (int i=0;i<n;i++) printf(" %d",ind[i]);
		printf("\n");
//		f[i]=l[i]+p[i]*f[0]+(1-p[i])*f[i+1]
//		f[0] = (f[i]-l[i]-(1-p[i])*f[i+1])/p[i]
	}
	return 0;
}
