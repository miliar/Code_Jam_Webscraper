#include<iostream>
#include<algorithm>
using namespace std;

const int inf=1000000000;
int a[1000],b[1000],n;
int cmp(int a,int b)
{
	if(a>b)
		return 1;
	else
		return 0;
}
__int64 solve()
{	
	int Min,i;

	__int64 ans=0,w;
	sort(a,a+n);
	sort(b,b+n,cmp);
	for(i=0;i<n;i++)
		ans+=a[i]*b[i];
	return ans;

}
int main()
{
	
	int i,T;
	int t=1;
	__int64 ans;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin>>T;

	while(T--)
	{
	
		cin>>n;

		for(i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];

		ans=solve();
		
		printf("Case #%d: %I64d\n",t++,ans);

	}

return 0;
}