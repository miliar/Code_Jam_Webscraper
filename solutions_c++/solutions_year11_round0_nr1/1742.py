#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;

int main()
{
	//freopen("data.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int k,n;
	cin>>k;
	int i,j;
	for(i=1;i<=k;++i)
	{
		int oPos=1;
		int bPos=1;
		int oTime=0;
		int bTime=0;
		cout<<"Case #"<<i<<": ";
		cin>>n;
		int a;
		char c;
		for(j=0;j<n;++j)
		{
			cin>>c>>a;
			if(c=='O')
			{
				int oNtime=bTime+1;
				if(oNtime<oTime+abs(a-oPos)+1)
					oNtime=oTime+abs(a-oPos)+1;
				oTime=oNtime;
				oPos=a;
			}
			else if(c=='B')
			{
				int bNtime=oTime+1;
				if(bNtime<bTime+abs(a-bPos)+1)
					bNtime=bTime+abs(a-bPos)+1;
				bTime=bNtime;
				bPos=a;
			}

		}
		int ans=bTime;
		if(ans<oTime) ans=oTime;
		cout<<ans<<endl;
	}
	return 0;
}