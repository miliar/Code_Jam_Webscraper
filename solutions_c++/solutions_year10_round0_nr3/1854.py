#include<iostream>
using namespace std;

long long a[234234];
int next[103423];
long long ge[234234];
int pre[1001];
long long liang[234234];
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	for(int i=1;i<=zu;i++)
	{
		printf("Case #%d: ",i);
		long long m,k;
		int n;
		cin>>m>>k>>n;
		for(int i=1;i<=n;i++)
		{
			cin>>a[i];
		}
		for(int i=1;i<=n;i++)
		{
			a[i+n]=a[i];
		}
		for(int i=1;i<=(n<<1);i++)
		{
			a[i]+=a[i-1];
		}
		if(a[n]<=k)
		{
			cout<<m*a[n]<<endl;
			continue;
		}
		int q=0;
		for(int i=1;i<=n;i++)
		{
			while(a[q+1]-a[i-1]<=k)q++;
			next[i]=q+1;
			if(next[i]>n)next[i]-=n;
			ge[i]=a[q]-a[i-1];
			//cout<<i<<" "<<next[i]<<" "<<ge[i]<<endl;
		}
		memset(pre,-1,sizeof(pre));
		int beg = 1;
		pre[beg]=0;
		liang[beg]=0;
		long long int res =0;
		bool fin = 1;
		int xuanhuan = 0;
		for(int ci = 1;ci<=m;ci++)
		{
			int end = next[beg];
			res+=ge[beg];
			if(pre[end]==-1)
			{
				liang[end]=res;
				pre[end]=ci;
				beg=end;
			}
			else
			{
				xuanhuan = ci-pre[end];
				long long rr = liang[end];
				m-=pre[end];
				int cheng = m/xuanhuan;
				rr = rr+cheng*(res-liang[end]);
				m%=xuanhuan;
				beg=end;
				for(int j=0;j<m;j++)
				{
					rr+=ge[end];
					end=next[end];
				}
				cout<<rr<<endl;
				fin=0;break;
			}
		}
		if(fin)
		{
			cout<<res<<endl;
			continue;
		}
	}
}