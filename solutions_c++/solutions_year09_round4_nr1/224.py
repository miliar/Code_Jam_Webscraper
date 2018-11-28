#include<stdio.h>
#include<algorithm>
using namespace std;
int n;
int a[50],b[50];
char s[50];

int cal(char m[50])
{
	int i,n=strlen(m);
	for(i=n-1;i>=0;i--)
	{
		if(m[i]=='1')
			break;
	}
	return i;
}


int main()
{
	
	int i,j,k,t,t1;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	t1=1;
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",s);
			a[i]=cal(s);
		}
		int ans=0;
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				if(a[j]<=i)break;
			}
			ans+=(j-i);
			for(k=j;k>i;k--)
				swap(a[k],a[k-1]);
		}
		printf("Case #%d: %d\n",t1++,ans);
	}
	
	return 0;
}
