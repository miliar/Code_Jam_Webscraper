#include <iostream>
#include <queue>
using namespace std;

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	queue<unsigned long long> Passengers , Riders;
	unsigned long long R =0 , K = 0, N = 0 ;
	unsigned long long g = 0;
	unsigned long long T = 0;
	unsigned long long i = 0 , j = 0 ;
	unsigned long long Sum = 0;
	unsigned long long hold = 0 , k = 0;

	cin>>T;

	for (i=0;i<T;i++)
	{
		cin>>R>>K>>N;
		Sum = 0 ;
		k = 0 ;
		hold = 0 ;
		g = 0 ;

		for (j=0;j<N;j++)
		{
			cin>>g;
			Passengers.push(g);
		}

		for (j=0;j<R;j++)
		{
			k = K;
			while(Passengers.size() != 0)
			{
				if ( k < Passengers.front())
				{
					break;
				}
				hold = Passengers.front();
				Sum += hold;
				k = k - Passengers.front();
				Passengers.pop();
				Riders.push(hold);
			}
			hold = Riders.size();
			while ( hold > 0)
			{
				hold--;
				Passengers.push(Riders.front());
				Riders.pop();
			}
		}
		cout<<"Case #"<<i+1<<": "<<Sum<<endl;
		while ( !Passengers.empty() )
			Passengers.pop();
		while ( !Riders.empty() )
			Riders.pop();
	}


	return 0;
}