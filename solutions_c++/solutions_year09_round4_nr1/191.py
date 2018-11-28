#include<stdio.h>
#include<algorithm>
using namespace std;

int n;
int a[50],b[50];
char s[50];

int cal(char *s)
{
	int i,n=strlen(s);
	for(i=n-1;i>=0;i--)
	{
		if(s[i]=='1')break;
	}
	return i;
}

bool cmp(int p,int q)
{
	return a[p]<a[q]||a[p]==a[q]&&p<q;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,t,ca;
	scanf("%d",&t);
	for(ca=1;ca<=t;ca++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",s);
			a[i]=cal(s);
		}
	/*	for(i=0;i<n;i++)
		{
			printf("a[%d]=%d\n",i,a[i]);
		}*/
		int ans=0;
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				if(a[j]<=i)break;
			}//printf("j=%d\n",j);
			ans+=j-i;
		/*	for(k=0;k<n;k++)
			{
				printf("%d ",a[k]);
			}printf("\n");*/
			for(k=j;k>i;k--)
				swap(a[k],a[k-1]);
		/*	for(k=0;k<n;k++)
			{
				printf("%d ",a[k]);
			}printf("\n");*/
		}
		printf("Case #%d: %d\n",ca,ans);
	}

	return 0;
}