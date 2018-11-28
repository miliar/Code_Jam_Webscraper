#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cmath>
#include<string>
#include<utility>
#include<cstdlib>
#include<ctime>
using namespace std;
long long ans;
long long i,j,T,r,k,n,casenum,m,a,b,cnt1,cnt2;
long long g[2010],f[2010],mem[2010],cnt[2010],next[2010];
int h[2010];
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		cin>>r>>k>>n;
		for (i=1;i<=n;i++)
		{
			cin>>g[i];
			g[i+n]=g[i];
		}
		for (i=1;i<=n;i++)
		{
			cnt[i]=0;
			j=i;
			while (j-i<=n-1&&cnt[i]+g[j]<=k)
			{
				cnt[i]+=g[j];
				j++;
			}
			next[i]=(j-1)%n+1;
		}
		ans=0;
		j=1;
		memset(h,0,sizeof(h));
		for (i=1;i<=r;i++)
		{
			h[j]=i;
			mem[i]=cnt[j];
			ans+=mem[i];
			j=next[j];
			if (h[j]!=0)
			{
				m=i+1-h[j];
				a=(r-i)/m;
				b=(r-i)%m;
				cnt1=cnt2=0;
				for (k=h[j];k<=i;k++)
				{
					cnt1+=mem[k];
					if (k-h[j]+1<=b) cnt2+=mem[k];
				}
				ans+=cnt1*a+cnt2;
				break;
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}
