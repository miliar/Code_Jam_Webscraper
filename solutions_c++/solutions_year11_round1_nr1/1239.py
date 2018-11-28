#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;


int main () {
	ifstream cin("A-small.in");
	ofstream cout("A-small.out");
	int T;
	cin >> T;
	int cc = 1;
	
	while (T--) {
		cout << "Case #" << cc++ << ": ";
		int N, pd, pg;
		cin >> N >> pd >> pg;

		if (pg == 100 && pd != 100)
			cout << "Broken";
		else if (pg == 0 && pd != 0) {
			cout << "Broken";
		} else {
			bool can = false;
			for (int i = 1; i <= min(N,100); i++)
				if (pd/100.0 * i == int(pd/100.0*i))
					can = true;
			if (can)
				cout << "Possible";
			else
				cout << "Broken";
		}


		cout << endl;
	}
	return 0;
}