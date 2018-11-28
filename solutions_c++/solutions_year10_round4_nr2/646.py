#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int n,test,a[1<<12];

inline int Calc(int i,int j)
{
	int l=j;
	j=i+(1<<l)-1;
	bool ok=false;
	for (int k=i;k<=j;k++) if (a[k]) ok=true;
	if (!ok) return 0;
	for (int k=i;k<=j;k++) if (a[k]) a[k]--;
	int A=Calc(i,l-1),B=Calc(i+(1<<(l-1)),l-1);
	return 1+A+B;
}
int main()
{
	//freopen("B_s.in","r",stdin);
	int cnt=1;
	for (scanf("%d",&test);test--;cnt++)
	{
		printf("Case #%d: ",cnt);
		scanf("%d",&n);
		int x;
		for (int i=1;i<=1<<n;i++) scanf("%d",&a[i]);
		for (int i=1;i<=1<<n;i++) a[i]=n-a[i];
		for (int i=n-1;i>=0;i--)
			for (int j=1;j<=1<<i;j++) scanf("%d",&x);
		int ans=Calc(1,n);
		printf("%d\n",ans);
	}
	return 0;
}
