#include<iostream>
using namespace std;
int main()
{
	long long int ttt;
	cin>>ttt;
	for(long long int tt=1;tt<=ttt;tt++)
	{
		cout<<"Case #"<<tt<<": ";
		int  n,L,H;
		cin>>n>>L>>H;
		int a[100000];
		for(int i=0;i<n;i++)
			cin>>a[i];
		int GCD,LCM;
		int flag=0;
		for(int i=L;i<=H;i++)
		{
			flag=1;
			for(int j=0;j<n;j++)
			{
				if(i%a[j]!=0 && a[j]%i!=0)
				{
					flag=0;
					break;
				}
			}
			if(flag==1)
			{cout<<i<<endl;
				break;
			}
		}
		if(flag==0)cout<<"NO\n";




	}


}
