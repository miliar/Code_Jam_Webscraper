#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <queue>
#include <map>
using namespace std;

int a[900],b[900];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
	__int64 ans;
	int d=1,i;
	int n;
	int t;
	cin>>t;
	while(t--)
	{
		ans=0;
		cin>>n;
		for(i=0;i<n;i++)cin>>a[i];
		for(i=0;i<n;i++)cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		for(i=0;i<n;i++)
		{
			ans=ans+a[i]*b[n-1-i];
		}
		printf("Case #%d: %I64d\n",d++,ans);
	}
	return 0;
}

/*power by gdut_chc*/