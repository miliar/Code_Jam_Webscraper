#include<iostream>
#include<algorithm>
#define maxt 1000000000
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int tt,n,t;
int need[2100],cost[2100];
int f[2100][11];

int main()
{
	freopen("bl.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>tt;
	fo(ii,1,tt)
	{
		cin>>n;
		t=1<<n;
		fo(i1,0,t-1)
		{
			int i=t-1-i1;
			cin>>need[i];
			need[i]=n-need[i];
			fo(j,0,n)f[i+t][j]=maxt;
			f[i+t][need[i]]=0;
		}
		for(int i=t-1;i;i--)
			cin>>cost[i];
		for(int i=t-1;i;i--)
		{
			fo(j,0,n)f[i][j]=maxt;
			fo(j,0,n)
				fo(k,0,n)
				{
					f[i][max(j,k)]<?=f[i+i][j]+f[i+i+1][k];
					f[i][max(0,max(j,k)-1)]<?=f[i+i][j]+f[i+i+1][k]+cost[i];
				}
		}			
		cout<<"Case #"<<ii<<": "<<f[1][0]<<endl;
	}			
	return 0;
}

