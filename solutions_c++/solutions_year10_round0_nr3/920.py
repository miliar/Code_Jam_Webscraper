#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	long long sum[3000],been[2000],k,r,m,n,numtest,test,i,start,ji,ans,cost[2000];
	
	ifstream cin ("a.in");
	ofstream cout ("a.out");
	cin >> numtest;
	for(test=1;test<=numtest;test++)
	{
		cin >> r >> m >> n;
		sum[0]=0;
		for(i=1;i<=n;i++) {cin >> k;sum[i]=sum[i-1]+k;}
		if(m<sum[n])
		{
			for(i=1;i<=n;i++) sum[n+i]=sum[n+i-1]+sum[i]-sum[i-1];
			for(i=1;i<=n;i++) been[i]=0;
			start=1;ji=0;
			while(!been[start])
			{
				ji++;
				been[start]=ji;
				for(i=start;;i++) 
				{
					if(sum[i]-sum[start-1]>m) break;
				}
				cost[ji]=sum[i-1]-sum[start-1];
				start=(i-1)%n+1;
			}
			
			if(r<=ji)
			{
				ans=0;
				for(i=1;i<=r;i++) ans+=cost[i];
			}
			else
			{
				ans=0;
				for(i=been[start];i<=ji;i++) ans+=cost[i];
				ans*=(r-been[start]+1)/(ji-been[start]+1);
				for(i=1;i<been[start];i++) ans+=cost[i];
				for(i=1;i<=(r-been[start]+1)%(ji-been[start]+1);i++) ans+=cost[been[start]+i-1];
			}
		}
		else ans=r*sum[n];		
		cout << "Case #" << test << ": " << ans << endl;
	}
	
	return 0;
}
