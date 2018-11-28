#include<iostream>
using namespace std;

int main()
{
	int cases = 0;
	cin >> cases;
	
	for(int i = 1; i <= cases; i++)
	{
		int numButtons = 0;
		cin >> numButtons;
		
		int positionO = 1;
		int positionB = 1;
		
		char robot = 'O';
		int position = 0;
		
		int timeAvailableO = 0;
		int timeAvailableB = 0;
		
		int totalTimeTaken = 0;
		
		for(int j = 0; j < numButtons; j++)
		{
			cin >> robot;
			cin >> position;
			
			if(robot == 'O')
			{
				int timeRequired = position - positionO;
				if(timeRequired < 0)
					timeRequired *= (-1);
				timeRequired++; //For pressing button.
				
				timeAvailableO -= timeRequired;
				if(timeAvailableO < 0)
				{
					timeAvailableB += (timeAvailableO * (-1));
					totalTimeTaken += (timeAvailableO * (-1));
					timeAvailableO = 0;
				}
				else
				{
					timeAvailableO = 0;
					totalTimeTaken += 1; // For pressing button.
					timeAvailableB = 1;
				}
				positionO = position;
			}
			else
			{
				int timeRequired = position - positionB;
				if(timeRequired < 0)
					timeRequired *= (-1);
				timeRequired++; //For pressing button.
				
				timeAvailableB -= timeRequired;
				if(timeAvailableB < 0)
				{
					timeAvailableO += (timeAvailableB * (-1));
					totalTimeTaken += (timeAvailableB * (-1));
					timeAvailableB = 0;
				}
				else
				{
					timeAvailableB = 0;
					totalTimeTaken += 1; // For pressing button.
					timeAvailableO = 1;
				}
				positionB = position;
			}
		}
		
		cout << "Case #" << i << ": " << totalTimeTaken << "\n";
	}

	return 0;
}