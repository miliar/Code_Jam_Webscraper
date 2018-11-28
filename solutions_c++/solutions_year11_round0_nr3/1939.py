
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
using namespace std;
int a[1005];
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t,n,k;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d",&n);
		scanf("%d",&a[1]);
		int ans=a[1],sum=a[1];
		for(int i = 2;i <= n;i++)
		{
			scanf("%d",&a[i]);
			ans^=a[i];
			sum+=a[i];
		}
		printf("Case #%d: ",k);
		if(ans==0)
		{
			sort(a+1,a+n+1);
			cout<<sum-a[1]<<endl;
		}
		else cout<<"NO"<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
