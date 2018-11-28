#include <iostream>
#include <string>

#define MAXNUM 100000

using std::cin;
using std::cout;
using std::endl;
using std::string;

typedef struct {
	string name;
	int mkdir;
} directory;

// All the existent directories
directory directories[MAXNUM];

// Number of test cases
int t = 0, num = 1;
// Number of already existent directories and the ones you want to create
int ni = 0, nf = 0, m = 0;

int numDir (string direc)
{
	// Search in all the directories
	for (int i = 0; i < nf; i++) {
		if (direc == directories[i].name)
			return 0;
	}

	// If it didn't find
	for (int i = (direc.length()-1); i >= 0; i--)
		if (direc[i] == '/') {
			// Because i = 0 means that you're looking at the root directory
			int k = 0;
			if (i != 0)
				k = numDir (direc.substr(0, i));
			directories[nf].name = direc;
			directories[nf].mkdir = k+1;
			//cout << direc << endl;
			nf++;
			return directories[nf-1].mkdir;
		}
}

int main()
{
	cin >> t;

	while (num <= t) {
		cin >> ni >> m;
		string input = "";
		getline (cin, input);

		for (int i = 0; i < ni; i++) {
			cin >> directories[i].name;
			directories[i].mkdir = 0;
		}

		// Number of directories in the end of the "mkdir" proccess
		nf = ni;
		for (int i = 0; i < m; i++) {
			string dir = "";
			cin >> dir;
			numDir (dir);
		}

		cout << "Case #" << num << ": " << (nf - ni) << endl;

		num++;
	}

	return 0;
}
