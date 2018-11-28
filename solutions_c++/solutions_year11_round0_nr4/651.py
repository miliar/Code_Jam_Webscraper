#include<iostream>

using namespace std;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);

	int T;
	cin>>T;

	for(int tt=1;tt<=T;tt++)
	{
		int n;
		cin>>n;
		double ans = 0;
		for(int i=1;i<=n;i++)
		{
			int t;
			cin>>t;
			ans+=t!=i;
		}
		printf("Case #%d: %f\n",tt,ans);
	}

	return 0;
}
