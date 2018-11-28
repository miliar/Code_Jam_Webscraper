#include<iostream>
using namespace std;
int solve(int a,int n)
{
	int ans=1;
	for(int i=1;i<=n;i++)
		ans*=a;
	return ans;
}
int main()
{
	int T,n,k,cnt=1;
	freopen("E: \\A-large.in","r",stdin);
	freopen("E: \\A-large.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&k);
		int ans=solve(2,n);
		//printf("%d\n",ans);
		int temp=k%ans;
		if(temp==ans-1) printf("Case #%d: ON\n",cnt);
		else printf("Case #%d: OFF\n",cnt);
		cnt++;
	}
	return 0;
}