#include <stdio.h>
#include <string.h>
#include <math.h>
int hash[1000];
char a[100];
long long ans;
long long bi;
void solve()
{
	int i, len;
	int num[1000];
	scanf("%s",a);
	len=strlen(a);
	memset(hash,0,sizeof(hash));
	for(i=0;i<len;i++)
		hash[a[i]]++;
	int tt=0;
	for(i=0;i<1000;i++)
		if(hash[i]) tt++;
	bi=1;
	if(tt==1) tt++;
	for(i=1;i<len;i++)
		bi*=tt;
//		printf("bi:%d",bi);
	int tmp=0;
	memset(num,-1,sizeof(num));
	num[a[0]]=1;
	ans=0;
//	if(bi==1) bi=2;
	for(i=0;i<len;i++)
	{
//		printf("a[i]:%c num:%d\n",a[i],num[a[i]]);
		if(num[a[i]]!=-1)
			ans+=bi*num[a[i]];
		else
		{
			num[a[i]]=tmp;
			ans+=bi*num[a[i]];
			tmp++;
			if(tmp==1) tmp++;	
		}
		bi/=tt;
		
	}
	printf("%I64d\n",ans);
}
int main()
{
	int T;
	int i;
	freopen("A-large.in","r",stdin);
	freopen("alarge.out","w",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
