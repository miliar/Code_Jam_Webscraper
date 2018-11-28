#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int kk,cs,n,i,j,k,ans,a[50];
	char mp[50][50];
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>cs;
	for (kk=1;kk<=cs;kk++)
	{
		cin>>n;
		//cout<<n<<endl;
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
			{
				cin>>mp[i][j];
			}
		for (i=1;i<=n;i++)
		{
			for (j=n;j>=1;j--)
				if (mp[i][j]=='1')
				{
					//cout<<i<<" "<<j<<endl;
					a[i]=j;
					//cout<<i<<" "<<a[i]<<endl;
					break;
				}
			if (j==0) a[i]=0;
		}
		ans=0;
		for (i=1;i<=n;i++)
			if (a[i]>i)
			{
				for (j=i+1;j<=n;j++)
					if (a[j]<=i)
					{
						//cout<<i<<" "<<j<<endl;
						for (k=j;k>i;k--)
						{
							//cout<<ans<<endl;
							ans++;
							swap(a[k],a[k-1]);
						}
						break;
					}
			}
		cout<<"Case #"<<kk<<": "<<ans<<endl;
	}	
	return 0;
}
