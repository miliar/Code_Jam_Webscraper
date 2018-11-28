#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
const int MAXN = 2020;
int a[MAXN];
bool ok;
int h[MAXN];
void Work(int l,int r,int lh,int rh)
{
	if (!ok) return;
	if (l>r) return;	
	if (l==r) return ;
	if (a[l]>r) {
		ok=false;
		return;
	}
	/*
	if (rh==-1) {
		h[a[l]]=lh;
		Work(l,a[l],lh,lh);
		Work(a[l]+1,r,lh-1,-1);
		return ;
	}	
	*/
	double k=(double)(rh-lh)/(r-l+1);
	double b=rh-k*r;
	h[l]=(int)(k*l+b-10000);
	int now=l;
	vector<int> v;
	while (now!=r)
	{
		if (a[now]>r) {
			ok=false;
			return;
		}
		v.push_back(now);
		now=a[now];
	}
	for (int i=v.size()-1;i>=0;i--)
	{
		int t=v[i];
		h[t]=(int)(h[a[t]]-k*(a[t]-t)-2);
		k=(double)(h[a[t]]-h[t])/(a[t]-t);
		Work(t+1,a[t],h[t],h[a[t]]);
	}
}
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		int n;
		scanf("%d",&n);
		for (int i=1;i<n;i++)
			scanf("%d",&a[i]);
		printf("Case #%d:",tcase);
		ok=true;
		h[n]=1000000000;
		Work(1,n,1000000000,1000000000);
		if (!ok) {puts(" Impossible");continue;}
		for (int i=1;i<=n;i++)
			printf(" %d",h[i]);
		printf("\n");
	}
	return 0;
}
