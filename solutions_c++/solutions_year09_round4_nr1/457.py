#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<vector>
#include<cstring>
using namespace std;
long long num[50];
long long q[50];
int main(void)
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int tn;
	int cas=0;
	scanf("%d",&tn);
	while(tn--)
	{
	int n;
	scanf("%d",&n);
	char str[100];
	for(int i=0;i<n;i++)
		q[i]=(long long)1<<(i+1);
	for(int i=0;i<n;i++)
	{
		scanf("%s",str);
		num[i]=0;
		for(int j=0;j<n;j++)
			if(str[j]=='1')
				num[i]=num[i]+((long long)1<<j);
			
	}
	int ans=0;
	for(int i=0;i<n;i++)
	{
		for(int j=i;j<n;j++)
		{
			if(num[j]<q[i])
			{
				int t=j;
				while(t!=i)
				{
					ans++;
					swap(num[t],num[t-1]);
					t--;
				}
				break;	
			}
		}
	}
	printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
