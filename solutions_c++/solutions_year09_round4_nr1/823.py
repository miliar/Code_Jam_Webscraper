#include<stdio.h>
#include<algorithm>
#include<string.h>
int i,j,k,n,a[50],t,ti,tn,ans;
char str[50];
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&tn);
	for (ti=1;ti<=tn;ti++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%s",str);
			for (j=strlen(str)-1;j>=0;j--) if (str[j]=='1') break;
			a[i]=j;
		}
		ans=0;
		for (i=0;i<n;i++)
			if (a[i]>i)
			{
				for (j=i+1;j<n;j++)
					if (a[j]<=i) break;
				ans+=j-i;
				t=a[j];
				for (k=j;k>i;k--) a[k]=a[k-1];
				a[i]=t;
			}
		printf("Case #%d: %d\n",ti,ans);
	}
	return 0;
}
