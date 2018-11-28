#include <iostream>
#include <cmath>
using namespace std;


int main() {
	int numCases(0);
	cin >> numCases;

	for(int i = 1; i <= numCases; i++) {
		int numGooglers(0), numSurprising(0), p(0), better(0), surprising(0);
		cin >> numGooglers >> numSurprising >> p;

		for(int j = 0; j < numGooglers; j++) {
			int total(0), a(0);
			cin >> total;
			a = (int)ceil(total/3.0);
			if(total == 0 && p > 0) continue;
			if(total%3 == 2 && a >= p) better++;
			else if(total%3 == 2 && a+1 >= p) surprising++;
			else if(total%3 == 1 && a >= p) better++; 
			else if(total%3 == 0 && a >= p) better++;
			else if(total%3 == 0 && a+1 >= p) surprising++;

			}

		if(surprising > numSurprising) surprising = numSurprising;
		cout << "Case #" << i << ": " << better+surprising << endl;

	}


}


