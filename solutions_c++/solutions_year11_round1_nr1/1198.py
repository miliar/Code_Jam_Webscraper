#include <iostream>

using namespace std;

int main()
{
	long long temp = 1,t,n,pd,pg,won,lost,d,g,g_won;
	cin>>t;
	while(temp <= t)
	{
		won = 0, lost = 0, d = 0;
		cin>>n>>pd>>pg;
		for(int i = 1; i <=n; i++)
		{
			if((pd*i)%100 == 0)
			{
				won =  (pd*i)/100;
				lost = i - won;
				d = i;
				break;
			}
		}
		if(!d)
			cout<<"Case #"<<temp<<": Broken"<<endl;
		else if(lost && pg == 100)
			cout<<"Case #"<<temp<<": Broken"<<endl;
		else if(won && pg == 0)
			cout<<"Case #"<<temp<<": Broken"<<endl;
		else
			cout<<"Case #"<<temp<<": Possible"<<endl;

		temp++;
	}
}
