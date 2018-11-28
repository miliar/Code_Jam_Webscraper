#include <iostream>
using namespace std;

int s,n,t,ca,mi,v,j,i;

int main()
{
	freopen("in.in","r",stdin);
	freopen("ou.ou","w",stdout);
	cin>>t;
	while (t--)
	{
		ca++;
		cin>>n;
		s=0; v=0; mi=100000000;
		for (i=1;i<=n;i++) 
		{
			cin>>j;
			if (j<mi) mi=j;
			s=s+j;
			v=v^j;
		}
		cout<<"Case #"<<ca<<": ";
		if (v==0) cout<<s-mi<<endl;
		else cout<<"NO"<<endl;
	}
}
