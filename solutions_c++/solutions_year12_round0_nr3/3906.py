#include<iostream>
#include<cstring>
using namespace std;

int dig[10]={1,10,100,1000,10000,100000,1000000,10000000};
int vis[2000005];

int main()
{
	freopen("111.in","r",stdin);
	freopen("out.out","w",stdout);
	int T,tc,A,B,n,m,i,c,d,ans;
	cin>>T;
	for(tc=1;tc<=T;tc++)
	{
		ans=d=0;
		memset(vis,0,sizeof(vis));
		cin>>A>>B;
		n=A;
		while(n)
		{  n/=10; d++; }
		for(n=A;n<=B;n++)
			if(!vis[n])
			{
				c=1;
				vis[n]=1;
				for(i=1;i<d;i++)
				{
					m=n/dig[i]+(n%dig[i])*dig[d-i];
					if(m>=A&&m<=B&&!vis[m])
					{
						vis[m]=1;
						c++;
					}
				}
				if(c>=2)
					ans+=c*(c-1)/2;
			}
		cout<<"Case #"<<tc<<": "<<ans<<endl;
	}
	return 0;
}
