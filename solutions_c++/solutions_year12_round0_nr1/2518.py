#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

typedef vector <   int  > vi;
typedef vector <   vi   > vvi;
typedef vector < double > vd;
typedef vector <   vd   > vvd;
typedef vector < string > vs;

int main () {
	string map = "yhesocvxduiglbkrztnwjpfmaq";
	string line;
	int T; cin >> T;
	getline(cin, line, '\n');
	
	for (int t = 1; t <= T; t++) {
		getline(cin, line, '\n');
		for (int i = 0; i < line.size(); i++) {
			if (line[i] != ' ')
				line[i] = map[ line[i]-'a' ];
		}

		cout << "Case #" << t << ": " << line << endl;
	}

	return 0;
}
