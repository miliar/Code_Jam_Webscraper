#include<stdio.h>
#include<algorithm>
using namespace std;

int cs,n;
int a[50];

int get(char *in)
{
	for(int i=n-1;i>=0;i--){
		if(in[i]=='1') break;
	}
	return i;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	int i,j,k,cn;
	char in[50];
	scanf("%d",&cs);
	for(cn=1;cn<=cs;cn++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",in);
			a[i]=get(in);
		}
		int ans=0;
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				if(a[j]<=i)break;
			}
			ans+=j-i;
			for(k=j;k>i;k--)
			{
				int tmp = a[k];
				a[k] = a[k-1];
				a[k-1] = tmp;
			}
		}
		printf("Case #%d: %d\n",cn,ans);
	}
	return 0;
}
