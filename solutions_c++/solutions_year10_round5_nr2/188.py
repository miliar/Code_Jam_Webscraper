#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define MAX 101
const int BIG=0x3f3f3f3f;
int a[MAX];
int b[MAX*MAX];
int main()
{
	int cs,dd,i,j,n,mx;
	long long L,ans;
	scanf("%d",&cs);
	for(dd=1;dd<=cs;dd++)
	{
		memset(b,0x3f,sizeof(b));
		scanf("%lld%d",&L,&n);
		for(mx=i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			mx=max(a[i],mx);
		}
		b[0]=0;
		for(i=0;i<n;i++)
			for(j=0;j<MAX*MAX-a[i];j++)
				b[j+a[i]]=min(b[j+a[i]],b[j]+1);
		ans=-1;
		for(i=MAX*MAX-1;i>=0;i--)
			if((L-i)%mx==0&&b[i]!=BIG)
			{
				ans=(L-i)/mx+b[i];
				break;
			}
			if(i==-1)
				printf("Case #%d: IMPOSSIBLE\n",dd);
			else
				printf("Case #%d: %lld\n",dd,ans);
	}
}