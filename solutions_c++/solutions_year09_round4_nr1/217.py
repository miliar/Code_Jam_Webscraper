#include<iostream>
#include<string>
using namespace std;
string a[50];
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int i,j,k,n,t,tt=1,ans;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			cin>>a[i];
		ans=0;
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				for(k=i+1;k<n;k++)
					if(a[j][k]=='1')break;
				if(k==n)break;
			}
			for(k=j;k>i;k--){a[k]=a[k-1];ans++;}
		}
		printf("Case #%d: %d\n",tt++,ans);
	}
	return 0;
}
