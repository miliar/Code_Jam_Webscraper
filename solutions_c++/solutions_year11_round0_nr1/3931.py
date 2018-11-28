#include <iostream>
#include <cmath>

using namespace std;


int main()
{
	int T;
	cin >> T;
	int time = 0;
	
	
	for(int t = 0; t < T; t++)
	{
		int num;
		cin >> num;
		time = 0;
		int currentBlue = 1;
		int currentOrange = 1;
		int blueLapse = 0;
		int orangeLapse = 0;
	
		
		
		for(int i = 0; i < num; i++)
		{
			char r;
			int b;
			cin >> r;
			cin >> b;
			
			if(r == 'O')
			{

				int pTime = (abs(b - currentOrange) + 1) - orangeLapse;
				if(pTime > 0)
				{
					time += pTime;
					blueLapse += pTime;
				}
				else
				{
					time++;
					blueLapse++;
				}

				orangeLapse = 0;
				currentOrange = b;

			}

			if(r == 'B')
			{
				int pTime = (abs(b - currentBlue) + 1) - blueLapse;
				if(pTime > 0)
				{
					time += pTime;
					orangeLapse += pTime;
				}
				else
				{
					time++;
					orangeLapse++;
				}
				blueLapse = 0;
				currentBlue = b;

			}

		}
		cout << "Case #" << t+1 << ": " << time << endl;
	}
	return 0;
}