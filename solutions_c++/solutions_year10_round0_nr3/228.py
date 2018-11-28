#include<fstream>
#include<iostream>
using namespace std;
unsigned long long sum[1000];
int circlesize;
int g[1000];
bool vis[1000];
int vistime[1000];

int ThemePark()
{
	int cas=0;
	int T;
	int R, k, N;
	ifstream F("C-large.in");
	ofstream G("C-large.out");
	F>>T;
	cout<<"ThemePark Called\n";
	while(T--)
	{
		cas++;
		F>>R>>k>>N;
		for (int i =0 ;i<N;i++)
		{
			F>>g[i];
		}
		int j=0,m;
		memset(vis,0,sizeof(vis));
		circlesize=0;
		while (!vis[j])
		{
			vis[j]=true;
			vistime[j]=circlesize;
			m=j;
			unsigned long long int temp=0;
			while (temp+g[j]<=k)
			{
				temp+=g[j];
				j++;
				j%=N;
				if (j==m)
				{
					break;
				}
			}
			sum[circlesize++]=temp;			
		}

		for (int i = 1; i<vistime[j];i++)
		{
			sum[i]=sum[i]+sum[i-1];
		}
		for (int i= vistime[j]+1;i<circlesize;i++)
		{
			sum[i]=sum[i-1]+sum[i];
		}
		unsigned long long ans;
		if (R<=vistime[j])
		{
			ans=sum[R-1];
		}else{
		R-=vistime[j];
		ans = sum[vistime[j]-1];

		ans += (R/(circlesize-vistime[j]))*sum[circlesize-1];

		if (R%(circlesize-vistime[j])!=0)
		{
			ans+=sum[R%(circlesize-vistime[j])+vistime[j]-1];
		}
		}
		G<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}