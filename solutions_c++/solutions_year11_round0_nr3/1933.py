#include <iostream>

using namespace std;

long long n,k,i,j,tmp,mint,xo,sum,cas=1;

void casen()
{
cout<<"Case #"<<cas<<": ";
cas++;
}

int main()
{
	freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
	cin>>n;
	for(i=0;i<n;i++)
	{
	mint=100000000;
	xo=0;
	sum=0;
	cin>>k;
	for(j=0;j<k;j++)
		{
			cin>>tmp;
			xo^=tmp;
			sum+=tmp;
			if(mint>tmp)mint=tmp;
		}
	if(xo==0)
	{
		casen();
		cout<<sum-mint<<endl;
	}
	else 
		{
		casen();
		cout<<"NO"<<endl;
	}
		
	}
	return 0;
}