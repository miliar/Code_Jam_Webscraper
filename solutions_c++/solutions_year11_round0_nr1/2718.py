#include <iostream>
#include <string>
#include <cstdlib>


using namespace std;


int main()
{
	// Obtain the number of test cases
	int T;
	cin >> T;
	
	// Handle each test case
	for (int i = 0; i < T; i++) {
		
		// Initialize robot positions and required times
		int posBlue    = 1;
		int posOrange  = 1;
		int timeBlue   = 0;
		int timeOrange = 0;
		
		// Obtain the number of buttons to be pressed for the current test case
		int N;
		cin >> N;
		
		// Handle each button entry
		for (int j = 0; j < N; j++) {
			
			// Obtain details for next button to be pressed
			string robot;
			cin >> robot;
			int button;
			cin >> button;
			
			// Update the time measurement for each robot
			if (robot == "B") {
				int noWait = timeBlue + abs(button - posBlue) + 1;
				if (noWait > timeOrange)
					timeBlue = noWait;
				else
					timeBlue = timeOrange + 1;
				posBlue = button;
			}
			else {
				int noWait = timeOrange + abs(button - posOrange) + 1;
				if (noWait > timeBlue)
					timeOrange = noWait;
				else
					timeOrange = timeBlue + 1;
				posOrange = button;
			}
			
		}
		
		// Output the required time
		cout << "Case #" << i + 1 << ": ";
		if (timeBlue >= timeOrange)
			cout << timeBlue << endl;
		else
			cout << timeOrange << endl;
	}
	
	return 0;
}
