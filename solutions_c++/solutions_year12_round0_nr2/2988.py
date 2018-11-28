
#include<cstdio>
#include<map>
#include<algorithm>
using namespace std;
int n,s,p;
int a[109];
bool cmp(int x,int y)
{
	return x>y;
}
void solve()
{
	scanf("%d%d%d",&n,&s,&p);
	for(int i=0;i<n;i++)
	scanf("%d",&a[i]);
	sort(a,a+n,cmp);
	int ans=0;
	for(int i=0;i<n;i++)
	{
		int tmp=a[i]/3;
		if(tmp>=p)ans++;
		if(tmp==p-1&&a[i]%3==0&&s&&tmp>0){ans++,s--;}
		if(tmp==p-1&&a[i]%3==1){ans++;}
		if(tmp==p-1&&a[i]%3==2){ans++;}
		if(tmp==p-2&&a[i]%3==2&&s){ans++,s--;}
	}
	printf("%d\n",ans);
}
int main()
{
	int ca;
	char c;
	freopen("F:\\TDDOWNLOAD\\B-large.in","r",stdin);
	freopen("ansBB.out","w",stdout);
	scanf("%d",&ca);
	getchar();
	for(int ii=1;ii<=ca;ii++)
	{
		printf("Case #%d: ",ii);
		solve();
	}
	return 0;
}