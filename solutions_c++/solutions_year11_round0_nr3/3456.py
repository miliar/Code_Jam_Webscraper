#include <iostream>

using namespace std;

int main()
{
	freopen("C3.in","r",stdin);
	freopen("outC3.txt","w",stdout);
	int i,test,n,j;
	int ans;
	int p,min,sum;
	cin>>test;
	for(i=1;i<=test;i++)
	{
		cin>>n;
		ans=0;
		sum=0;
		for(j=1;j<=n;j++)
		{
			cin>>p;
			ans=ans^p;
			sum+=p;
			if(j==1) min=p;
			else
			{
				if(min>p) min=p;
			}

		}
		if(ans!=0) {cout<<"Case #"<<i<<": NO"<<endl;}
		else{cout<<"Case #"<<i<<": "<<sum-min<<endl;}
	}
	return 0;
}