#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w+",stdout);
	int test,t,i,j;
	int n,l,h,f[200],flag,flag1;
	cin>>test;
	for (t=1;t<=test;t++)
	{
		cin>>n>>l>>h;
		for (i=0;i<n;i++) cin>>f[i];
		flag1=0;
		for (j=l;j<=h;j++)
		{
			flag=0;
			for (i=0;i<n;i++)
			{
				if (!(f[i]%j==0 || j%f[i]==0))
				{
					flag=1;
					break;
				}
			}
			if (!flag) 
			{
				printf("Case #%d: %d\n",t,j);
				flag1=1;
				break;
			}
		}
		if (!flag1) printf("Case #%d: NO\n",t);
	}
	return 0;
}