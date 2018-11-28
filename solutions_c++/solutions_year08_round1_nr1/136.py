#include<iostream>
#include<algorithm>
using namespace std;
int x[1000],y[1000];
int main()
{
	int t,n,p=0,ans,i;
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	for(scanf("%d",&t);t--;printf("Case #%d: %d\n",++p,ans))
	{
			scanf("%d",&n);	
			for(i=0;i<n;++i)scanf("%d",&x[i]);
		    for(i=0;i<n;++i)scanf("%d",&y[i]);
			sort(x,x+n);
			sort(y,y+n);
			for(ans=i=0;i<n;++i)
			{
				ans+=x[i]*y[n-1-i];
			}
	}
	return 0;
}