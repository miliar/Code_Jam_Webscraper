#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

int a[1100];

int main()
{
	//freopen("in3.txt","r",stdin);
	//freopen("out3.txt","w",stdout);
	int t,ca=1;
	int r,k,n;
	int i;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++) scanf("%d",&a[i]);
		map<int,pair<long long,int> > mp;
		mp[0]=make_pair(0,0);
		long long ans=0;
		int ss=0,tt=0;
		i=0;
		long long delta=-1;
		int start=-1,len=-1;
		for(i=1;i<=r;i++)
		{
			int num=0;
			while(1)
			{
				if(num!=0 && ss==tt) break;
				if(num+a[tt]<=k)
				{
					num+=a[tt++];
					if(tt>=n) tt=0;
				}
				else break;
			}
			ss=tt;
			ans+=num;
			if(mp.find(ss)!=mp.end())
			{
				pair<long long,int> aa=mp[ss];
				delta=ans-aa.first;
				len=i-aa.second;
				start=aa.second;
				ans=aa.first;
				break;
			}
			else
			{
				mp[ss]=make_pair(ans,i);
			}
		}
		if(len==-1) printf("Case #%d: %lld\n",ca++,ans);
		else
		{
			ans+=delta*((r-start)/len);
			int rest=start+(r-start)/len*len;
			for(i=rest+1;i<=r;i++)
			{
				int num=0;
				while(1)
				{
					if(num!=0 && ss==tt) break;
					if(num+a[tt]<=k)
					{
						num+=a[tt++];
						if(tt>=n) tt=0;
					}
					else break;
				}
				ss=tt;
				ans+=num;
			}
			printf("Case #%d: %lld\n",ca++,ans);
		}
	}
	return 0;
}