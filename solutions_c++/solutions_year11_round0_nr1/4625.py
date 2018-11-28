#include<iostream>

using namespace std;

int difference(int a, int b)
{
	if(a>=b)
		return (a-b);
	else 
		return (b-a);
}

int main()
{
	int numTest = 0;
	int i = 1;
	cin>>numTest;
	while(i <= numTest)
	{
		int numButton;
		cin>>numButton;
		char robot;
		int button;
		int posO = 1, timeO = 0;
		int posB = 1, timeB = 0;
		for(int j=0; j<numButton; j++)
		{
			cin>>robot;
			cin>>button;
			if(robot == 'O')
			{
				timeO += difference(posO, button);
				posO = button;
				if(timeO < timeB)
					timeO = timeB;

				timeO = timeO + 1;		
			}	
			else if(robot == 'B')	
			{
				timeB += difference(posB,button);
				posB = button;
				if(timeB < timeO)
					timeB = timeO;
			
				timeB = timeB + 1;	
			}
		}
		
		if(timeO >= timeB)
			cout<<"Case #"<<i<<": "<<timeO<<endl;
		else	
			cout<<"Case #"<<i<<": "<<timeB<<endl;
		i++;
	}
	return 0;
}
