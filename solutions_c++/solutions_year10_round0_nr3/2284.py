#include<iostream>
using namespace std;

int main()
{
	int t,r,k,n;;
	int val,flag;
	int c,i,j,tc;
	int grp[1001];

	cin>>t;
	c=0;

	while(c++<t)
	{
		cin>>r>>k>>n;
		i=0;
		while(i<n)
			cin>>grp[i++];

		val=0;
		j=0;
		for(i=0;i<r;i++)
		{	tc=0;
			flag=n;
			while(flag && ((tc + grp[j]) <= k))
			{
				tc += grp[j++];
				j %=n;
				flag--;
			}
			val+=tc;
		}		
		cout<<"Case #"<<c<<": "<<val<<endl;
	}

	return 0;
}
