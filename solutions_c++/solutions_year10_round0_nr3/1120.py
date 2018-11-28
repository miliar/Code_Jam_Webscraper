#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

const int MAX = 1000+50;

ll R,K,N;
ll G[MAX];
int flag[MAX];
ll earn[MAX];

int main(int argc, char *argv[])
{	
	int t;
	int i,rou;
	ll  tot,gtot;
	ll ans;
	int cas=0;

	freopen("in","r",stdin);
	freopen("out","w",stdout);

	scanf("%d",&t);
	while (t--)
	{
		cas++;
		cin>>R>>K>>N;		
		tot=0;
		for (i=0;i<N ;i++ ) cin>>G[i],tot+=G[i];

		if (tot<=K)
			ans=R*tot;
		else
		{
			ans=0;
			memset(flag,-1,sizeof(flag));
			memset(earn,0,sizeof(earn));
			flag[0]=0;
			i=0;rou=0;
			gtot=0;
			while (rou<R)
			{
				tot=0;rou++;
				for (;tot+G[i]<=K ;tot+=G[i],i=(i+1)%N );
				gtot+=tot;
				if (flag[i]==-1)
				{
					flag[i]=rou;					
					earn[i]=gtot;
				}
				else
				{
					int cr=rou-flag[i];
					ll add=gtot-earn[i];
					int times=(R-flag[i])/cr;
					int left=(R-flag[i])%cr;
					ans=earn[i]+add*times;
					rou=left;
					while (left--)
					{
						tot=0;
						for (;tot+G[i]<=K ;tot+=G[i],i=(i+1)%N );
						ans+=tot;
					}
					break;
				}
			}
			if (rou==R) ans=gtot;
		}
		cout<<"Case #"<<cas<<": "<<ans<<"\n";
	}
	return 0;
}
