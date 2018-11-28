#include<iostream>
using namespace std;
int main()
{
	freopen("small","r",stdin);		
	freopen("smalloutput","w",stdout);
	
	int T;
	int n;
	int creditO,creditB;
	int preO,preB;
	char ch;
	int button;
	int time;
	int sum;

	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>n;

		sum=0;
		creditO=creditB=0;
		preO=preB=1;
		for(int i=0;i<n;i++)
		{
			cin>>ch>>button;
			if(ch=='O')
			{
				time=abs(button-preO);
				
				if(time>creditO)  time-=creditO;
				else time=0;
				
				time++;  //time for press button
				sum+=time;
				creditB+=time;   // Blue can use this time+1 seconds to walk, but cannot to press button
				creditO=0;
				preO=button;
			}
			else if(ch=='B')
			{
				time=abs(button-preB);
				
				if(time>creditB)  time-=creditB;
				else time=0;
				
				time++;  //time for press button
				sum+=time;
				creditO+=time;   // Blue can use this time+1 seconds to walk, but cannot to press button
				creditB=0;
				preB=button;
			}
			else
			{
				cout<<"read error\n";
			}
		}
		cout<<"Case #"<<t<<": "<<sum<<endl;
	}

}