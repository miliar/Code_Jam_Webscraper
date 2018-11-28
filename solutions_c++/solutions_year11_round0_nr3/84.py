#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
int a[1200],_,ca,i,te,ans,n;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&_);ca=0;
	while(_--)
	{
		ca++;
		scanf("%d",&n);
		te=0;
		for(i=0;i<n;i++)
		scanf("%d",&a[i]),te^=a[i];
		if(te!=0){printf("Case #%d: NO\n",ca);continue;}
		sort(a,a+n);
		ans=0;
		for(i=1;i<n;i++)ans+=a[i];
		printf("Case #%d: %d\n",ca,ans);
	}
}
