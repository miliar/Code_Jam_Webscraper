#include<iostream>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int n,m,tt,ii,ans;
int d[1010][2];

int main()
{
	freopen("al.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>tt;
	fo(ii,1,tt)
	{
		cin>>n;
		ans=0;
		fo(i,1,n)
			cin>>d[i][0]>>d[i][1];
		fo(i,1,n)
			fo(j,i+1,n)
				ans+=(d[i][0]>d[j][0])^(d[i][1]>d[j][1]);
		cout<<"Case #"<<ii<<": "<<ans<<endl;
	}
	return 0;
}
	
