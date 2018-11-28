#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int c,cs,n,k,b,t,i,j,cnt,ans,pp;
	double time[110],p[110],v[110];
	cin>>cs;
	for (c=1;c<=cs;c++)
	{
		cin>>n>>k>>b>>t;
		for (i=0;i<n;i++)
			cin>>p[i];
		for (i=0;i<n;i++)
			cin>>v[i];
		for (i=0;i<n;i++)
			time[i]=(b-p[i])/v[i];
		
//		for (i=0;i<n;i++) printf("%.2lf ",time[i]);		cout<<endl;
		cnt=0;
		for (i=n-1;i>=0;i--)
			if (time[i]<=t) 
			{
				cnt++;
				if (cnt==k) pp=i;
			}
		if (cnt<k) cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
		else 
		{
			ans=0;
			for (i=pp;i<n;i++)
				if (time[i]<=t)
				{
					for (j=i;j<n;j++)
						if (time[j]>t) ans++;
				}
			cout<<"Case #"<<c<<": "<<ans<<endl;			
				
		}
	}
	return 0;
}
