#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	long long int t,n,o_time = 0,b_time = 0,var,temp =1;
	long long int time = 0, pos_o = 1, pos_b = 1;
	char bot,prev_bot;
	cin>>t;
	while(temp <= t)
	{
		
		time = 0;
		o_time = 0;
		b_time = 0;
		pos_b = 1, pos_o = 1;
		cin>>n;
		while(n--)
		{
			cin>>bot;
			if (bot == 'o' || bot == 'O')
			{
				cin>>var;
				if(time == 0)
					o_time = var;
				
				else
				{
					o_time = o_time + sqrt((var - pos_o)*(var - pos_o)) +1; 
				
					if(prev_bot == 'B')
					{
						if(o_time <= b_time)
							o_time = b_time + 1;
					}
				}	
				time = o_time;
				pos_o = var;
				prev_bot = 'O';
			}
			else if (bot == 'B')
			{
				cin>>var;
				if(time == 0)
					b_time = var;
				else 
				{
					b_time = b_time + sqrt((var - pos_b)*(var - pos_b)) +1;
					
					if(prev_bot == 'O')
					{
						if(b_time <= o_time)
							b_time = o_time + 1;
					}
				}

				time  = b_time;
				pos_b = var;
				prev_bot = 'B';
			}
		}
		cout<<"Case #"<<temp<<": "<<time<<endl;
		temp++;
	}
	
}
