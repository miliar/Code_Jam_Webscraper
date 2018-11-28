#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
const int MAXN = 1050;
const int MAXL = 10050;
int tot[MAXL];
int all[MAXN];
int as;
int n,a[MAXN];
bool OK(int m)
{
	if (m==1) return true;
	memset(tot,0,sizeof(tot));
	as=0;
	for (int i=1;i<=n;i++) tot[a[i]]++;
	for (int i=1;i<=n;i++) 
	if (tot[a[i]]>0 && a[i]+m-1<=10000)
	{
		bool flag=true;
		for (int j=a[i];j<=a[i]+m-1;j++)
			if (tot[j]==0) {flag=false;break;}
		if (!flag) continue;
		for (int j=a[i];j<=a[i]+m-1;j++)
			tot[j]--;
		all[++as]=a[i]+m-1;
	}
	for (int i=1;i<=n;i++)
	if (tot[a[i]]>0)
	{
		tot[a[i]]--;
		bool flag=false;
		for (int j=1;j<=as;j++)
		if (all[j]+1==a[i]) 
		{
			flag=true;
			all[j]=a[i];
			break;
		}
		if (!flag) return false;
	}
	return true;
}
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
			scanf("%d",&a[i]);
		if (n==0)
		{
			printf("Case #%d: %d\n",tcase,0);
			continue;
		}
		sort(a+1,a+n+1);
		int f=1,r=n,mid;
		memset(tot,0,sizeof(tot));
		while (f<r)
		{
			mid=(f+r+1)/2;
			if (OK(mid)) f=mid;
				else r=mid-1;
		}
		printf("Case #%d: %d\n",tcase,f);
	}
	return 0;
}
