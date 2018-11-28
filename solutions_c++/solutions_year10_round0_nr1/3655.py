#include<string>
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas=1,t,n,k,i;
	cin>>t;
	while(t--)
	{
		cin>>n>>k;
		i=0;
		while(i<n&&k>0)
		{
			if(k&1==1)
				i++;
			else
				break;
			k>>=1;
		}
		cout<<"Case #"<<cas<<": ";
		if(i>=n)
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
		cas++;
	}
	return 0;
}


