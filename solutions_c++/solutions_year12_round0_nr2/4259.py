#include <iostream>

using namespace std;

int main()
{
	int T, count = 0;
	int N, S, p, t[100];

	cin>>T;

	while(count++ < T)
	{
		cin>>N>>S>>p;

		for(int i = 0; i < N; i ++)
			cin>>t[i];

		int c = 0;
		for(int i = 0; i < N; i ++)
		{
			int avg = t[i] / 3;
			int rem = t[i] % 3;
			
			if(avg >= p)
			{	
//				cout<<"a: "<<t[i]<<endl;
				c++;
			}
			else if(avg == 0 && rem == 0)
				continue;
			else if(rem != 0)
			{
				if(avg + rem >= p && avg + rem <= 10)
				{
					if(rem == 2 && S > 0)
					{
//						cout<<"b: "<<t[i]<<endl;
						S--;
						c++;
					}
					else if(rem == 1 || (rem == 2 && avg + 1 >= p))
					{
//						cout<<"d: "<<t[i]<<endl;
						c++;
					}
				}
			}
			else if(avg + 1 >= p && avg - 1 >= 0 && avg + 1 <= 10)
			{
				if(S > 0)
				{
//					cout<<"c: "<<t[i]<<endl;
					S--;
					c++;
				}
			}
		}

		cout<<"Case #"<<count<<": "<<c<<endl;
	}

	return 0;
}
