#include <iostream>

using namespace std;

int main()
{
	unsigned int trials;
	char * state[2]={"OFF","ON"};
	cin >> trials;

	for(unsigned int i=0;i<trials;i++)
	{
		unsigned int n,k;
		cin >> n;
		cin >> k;

		unsigned int lbState=0;
		unsigned int firstOn = (1<<n)-1;
		
		if(k==firstOn)
		{
			lbState = 1;
		}
		else
		if(k>firstOn)
		{
			// after this, the light will be on
			// every 2^n steps
			k = k - firstOn;
			if ((k % (firstOn+1))==0)
			{
				lbState = 1;
			}
		}
		

		cout << "Case #"<<i+1<<": " << state[lbState]<<endl;
	}
	return 0;
}
