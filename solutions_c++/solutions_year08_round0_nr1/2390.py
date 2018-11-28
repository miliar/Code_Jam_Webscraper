#include<memory>
#include<stdio.h>
#include<algorithm>
using namespace std;

int h,i,n,t,q,l,r,m,c[111],d[111],p,s,j;
char a[111][111],b[111];

bool cmp(int i,int j)
{
	return strcmp(a[i],a[j])<0;
}

int main()
{
	freopen("aa.in","r",stdin);
	freopen("aa.txt","w",stdout);
	scanf("%d",&t);
	for(h=1;h<=t;h++)
	{
		scanf("%d\n",&n);
		for(i=0;i<n;i++)
		{
			gets(a[i]);
			c[i]=i;
		}
		sort(c,c+n,cmp);
		scanf("%d\n",&q);
		s=0;p=0;
		memset(d,0,sizeof(d));
		for(i=0;i<q;i++)
		{
			gets(b);
			l=-1;r=n;
			while(l+1<r)
			{
				m=(l+r)/2;
				j=strcmp(b,a[c[m]]);
				if(!j)break;
				if(j<0)r=m;
				else l=m;
			}
			if(!j&&!d[m])
			{
				d[m]=1;p++;
				if(p>=n)
				{
					s++;
					memset(d,0,sizeof(d));
					p=1;d[m]=1;
				}
			}
		}
		printf("Case #%d: %d\n",h,s);
	}
	return 0;
}