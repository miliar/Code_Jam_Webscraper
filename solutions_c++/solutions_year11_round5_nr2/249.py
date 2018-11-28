#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int a[1005];
int b[10005];
int cc[10005];
bool cmp(int aa,int bb)
{
	return aa<bb;
}
int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("out","w",stdout);
	int t,tt;
	scanf("%d",&tt);
	for(t=1;t<=tt;t++)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		sort(a,a+n,cmp);
//		for(int i=0;i<n;i++) printf("%d ",a[i]-a[0]);
//		printf("\n");
		int l=1;
		int r=n;
		int c;
/*		while(l<r)
		{
			printf("%d %d\n",l,r);
			c=(l+r)/2;
			for(int i=0;i<=10000;i++) b[i]=0;
			for(int i=0;i<n;i++) b[a[i]]++;
			bool ok=1;
			for(int i=0;i<=10000 && ok==1;i++)
			{
				while(b[i]>0 && ok==1)
				{
					for(int j=0;j<c;j++)
					{
						if(b[i+j]==0)
						{
							ok=0;
							break;
						}
						b[i+j]--;
					}
				}
			}
			if(ok==1) l=c+1;
			else r=c-1;
			
		}*/
			c=(l+r)/2;
			for(c=n;c>0;c--)
			{
			for(int i=0;i<=10000;i++) b[i]=0;
			for(int i=0;i<=10000;i++) cc[i]=0;
			for(int i=0;i<n;i++) b[a[i]]++;
			bool ok=1;
			for(int i=0;i<=10001 && ok==1;i++)
			{
				while(b[i]>0 && ok==1)
				{
					for(int j=0;j<c;j++)
					{
						if(b[i+j]==0)
						{
							ok=0;
							break;
						}
						b[i+j]--;
					}
					if(ok==1)
						cc[i+c]++;
					if(ok==0 && cc[i]>0)
					{
						cc[i]--;
						ok=1;
					}
				}
			}
			if(ok==1) break;
		}
		printf("Case #%d: %d\n",t,c);
	}
	return 0;
}
