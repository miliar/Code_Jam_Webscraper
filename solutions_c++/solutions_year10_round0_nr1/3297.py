#include<iostream>
using namespace std;

int main()
{
	int t,n,k,cnt=0;
	cin>>t;
	while(t--)
	{
		++cnt;
		cin>>n>>k;
		int ones = 0;
		bool yes  = false;
		while(k>0)
		{
			if(k%2)
			{
				ones++;
				if(ones >= n){yes=true;break;}
			}
			else if(ones < n)
			{
				yes = false;
				break;
			}
			k/=2;
		}
		if(yes)
			cout<<"Case #"<<cnt<<": "<<"ON"<<endl;
		else
			cout<<"Case #"<<cnt<<": "<<"OFF"<<endl;
	}
	return 0;
}