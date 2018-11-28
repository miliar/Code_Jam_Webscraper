#include<iostream>
using namespace std;
const int N=1003;
const int M=N*N;

typedef __int64 ll;

bool flag[N];
int a[N];
ll dp[N];
ll x[N];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	int r,k,n;
	cin>>T;
	for(int sce=1;sce<=T;sce++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(int i=1;i<=n;i++)
			scanf("%d",&a[i]);

		memset(flag,false,sizeof(flag));
		int cnt=0,pos=1;
		ll all=0;
		while(true)
		{
			if(flag[pos])
				break;
			cnt++;
			flag[pos]=true;
			x[pos]=cnt;
			ll sum=0;			
			int start=pos;
			bool fl=false;
			while(true)
			{
				if(sum+a[pos]>k)
					break;
				if(fl && pos==start)
					break;
				fl=true;
				sum+=a[pos];
				pos++;
				if(pos>n)
					pos=1;
			}
			dp[cnt]=dp[cnt-1]+sum;

		}

		printf("Case #%d: ",sce);

		int last=x[pos];
		int cur=cnt;
		if(r<=cur)
		{
			printf("%I64d\n",dp[r]);
			continue;
		}
		r-=cur;
		ll ans=dp[cur]+(r/(cur-last+1))*(dp[cur]-dp[last-1]);
		r%=(cur-last+1);
		if(r)
			ans+=dp[last+r-1]-dp[last-1];
		printf("%I64d\n",ans);
	}
	
}