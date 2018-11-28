#include<iostream>
using namespace std;
int main()
{
	long long int ttt;
	cin>>ttt;
	for(long long int tt=1;tt<=ttt;tt++)
	{
		cout<<"Case #"<<tt<<": ";
		long long int n,d,g;
		cin>>n>>d>>g;
		long long int flag=0;
		if(n>=100)
			flag=1;
		else
		{
			for(long long int i=1;i<=n;i++)
			{
				if((d*i)%100==0  )
				{
					flag=1;
					break;
				}
			}
		}
		if(flag==0 ||(g==100 && d!=100 )||(g==0&&d!=0))cout<<"Broken\n";
		else cout<<"Possible\n";


	}


}
