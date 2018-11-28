#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	int sun;
	cin>>sun;
	for(int pra=0;pra<sun;pra++)
	{
		cout<<"Case #"<<pra+1<<": ";
	int L,P,C;
	cin>>L>>P>>C;
	int count=0;
	while(P>L)
	{
		if(P%C==0)
			P=P/C;
		else
			P=(P/C)+1;
		if(P<=L)
			break;
		count+=1;
	}


	double ans=0;
	if(count!=0)
		ans=(log10(count)*1.0/log10(2));

	if(count==0)
		cout<<(int)ans<<endl;
	else
	{
		cout<<(int)ans+1<<endl;
	}
	}
}
