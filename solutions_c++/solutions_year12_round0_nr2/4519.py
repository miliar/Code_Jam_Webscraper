#include<stdio.h>  
#include<string.h>

int a[1100];

int main()
{
	freopen("r.in","r",stdin);
	freopen("w.txt","w",stdout);
	int n,i,len,ii=0,cnt1,cnt2,p,s,t;

	scanf("%d",&t);

	while(t--)
	{
		cnt1=cnt2=0;
		scanf("%d",&n);
		scanf("%d%d",&s,&p);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			if(a[i]>=3*p-2)
				cnt1++;
			else if((a[i]==3*p-3||a[i]==3*p-4)&&p>=2)
				cnt2++;
		}
		printf("Case #%d: %d\n",++ii,cnt1+(cnt2<s?cnt2:s));
	}
}