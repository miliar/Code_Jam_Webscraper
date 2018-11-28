#include <iostream>
#include <vector>
#include <string>


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
		
		// Obtain the dimensions for the picture
		int R, C;
		cin >> R;
		cin >> C;
		
		// Obtain the original picture
		vector<string> picture;
		picture.resize(R);
		for (int j = 0; j < R; j++) {
			string line;
			cin >> line;
			picture[j] = line;
		}
		
		// Perform the tile replacement
		bool okay = true;
		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				if (picture[j][k] != '#')
					continue;
				if ((j == R - 1) || (k == C - 1)) {
					okay = false;
					break;
				}
				if ((picture[j][k + 1] != '#') || (picture[j + 1][k] != '#') ||
					(picture[j + 1][k + 1] != '#')) {
					okay = false;
					break;
				}
				picture[j][k] = '/';
				picture[j][k + 1] = '\\';
				picture[j + 1][k] = '\\';
				picture[j + 1][k + 1] = '/';
			}
			if (!okay)
				break;
		}
		
		cout << "Case #" << i + 1 << ":" << endl;
		if (okay) {
			for (int j = 0; j < R; j++) {
				for (int k = 0; k < C; k++)
					cout << picture[j][k];
				cout << endl;
			}
		}
		else
			cout << "Impossible" << endl;
			
	}
	
	return 0;
}
