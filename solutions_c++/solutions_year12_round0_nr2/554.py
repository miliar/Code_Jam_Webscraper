//Code Jam 2012 B 
#include<iostream>
#include<cstring>
using namespace std;

int main(){
	int T,n,S,p,tmax,ans;
	int t[105];
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>T;
	for(int cnt=1;cnt<=T;cnt++)
	{
		cin>>n>>S>>p;
		for(int i=0;i<n;i++)
			cin>>t[i];
		ans=0;
		for(int i=0;i<n;i++)
		{
			if(t[i]==0)
			{
				if(0>=p) ans++;
			}
			else if(t[i]%3==1)
			{
				tmax=t[i]/3+1;
				if(tmax>=p) ans++;
			}
			else if(t[i]%3==2)
			{
				tmax=t[i]/3+1;
				if(tmax>=p)
					ans++;
				else if(tmax+1>=p && S>0)
				{
					S--;
					ans++;
				}
			}
			else if(t[i]%3==0)
			{
				tmax=t[i]/3;
				if(tmax>=p)
					ans++;
				else if(tmax+1>=p && S>0)
				{
					S--;
					ans++;
				}
			}
		}
		cout<<"Case #"<<cnt<<": "<<ans<<endl;
	}
	return 0;
}
 
