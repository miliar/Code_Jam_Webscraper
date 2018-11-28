#include<iostream>
#include<algorithm>
using namespace std;

int t,n;
int ans;

int num[1001];
bool vis[1001];

void trans()
{
	for(int i=1;i<=n;++i)
	{
		num[i]=n-num[i]+1;
	}
}

int calc()
{
	memset(vis,false,sizeof(vis));

	int ret=0;

	for(int i=1;i<=n;++i)
	{
		if(!vis[i])
		{
			int cnt=0;
			int pos=num[i];
			while(!vis[pos])
			{
				vis[pos]=true;
				pos=num[pos];
				cnt++;
			}

			ret+=((cnt-1)<<1);
		}
	}

	return ret;
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("D-small-attempt1.in","r",stdin);
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	/*
	double s;
	s=0;
	double a;
	a=2;
	for(int k=1;k<=100;++k)
	{
		a*=2;
		s+=(k+1)*(double)k/a;
		//s+=(double)k/a;
	}

	cout<<s<<endl;
	return 0;
*/
	cin>>t;
	for(int ca=1;ca<=t;++ca)
	{
		cin>>n;
		ans=0;

		printf("Case #%d: ",ca);
		for(int i=1;i<=n;++i)
		{
			cin>>num[i];
			if(num[i]!=i)
			{
				ans++;
			}
		}
		

		/*
		ans=calc();

		trans();

		ans=min(ans,calc());
*/
		cout<<ans<<".000000\n";
	}
	return 0;
}
