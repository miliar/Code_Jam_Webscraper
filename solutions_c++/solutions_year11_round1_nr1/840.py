#include <iostream>


using namespace std;


//
// Main Function
//

int main()
{
	// Obtain the number of test cases
	int T;
	cin >> T;
	
	// Handle each test case
	for (int i = 0; i < T; i++) {
		
		// Obtain the maximum possible number of games today, the percentage
		// of games today won, and the percentage won for all games played
		unsigned long long N;
		int Pd, Pg;
		cin >> N;
		cin >> Pd;
		cin >> Pg;
		
		// Eliminate special cases
		if (((Pg == 100) && (Pd < 100)) || ((Pg == 0) && (Pd > 0))) {
			cout << "Case #" << i + 1 << ": Broken" << endl;
			continue;
		}
		
		// Look for a candidate value for D based on values <= N where the
		// number of wins for the day will come out to be an integer value
		bool found = false;
		if (N >= 100)  // guaranteed at least 1 candidate when N is big enough
			found = true;
		else {
			for (unsigned long long j = 1; j <= N; j++) {
				if ((unsigned long long) Pd * j % 100 == 0) {
					found = true;
					break;
				}
			}
		}
		
		if (found)
			cout << "Case #" << i + 1 << ": Possible" << endl;
		else
			cout << "Case #" << i + 1 << ": Broken" << endl;
			
	}
	
	return 0;
}
