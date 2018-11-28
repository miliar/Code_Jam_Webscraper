#include <iostream>
#include <math.h>
#include <fstream>
#include <cstdlib>
 
using namespace std;

void queue(double *array, int size) {

	/*cout << "[";
	for(int x = 0; x < size; ++x)
		cout << array[x] << " ";
	cout << "]\n";
		*/
		
	double temp[size];
	for(int x = 0; x < size; ++x)
		temp[x] = array[x];
		
	for(int x = 0; x < size; ++x) {
		if(x+1 < size)
			array[x] = temp[x+1];
		else
			array[x] = temp[0];
	}
	

}

int main() {
int t = 0;
int m = 0;				// Money made this day
double r, k, n = 0;		// rider per day, people per ride, amout of groups
double q[1000]; 				// queue order
char inLine[128];

ifstream inFile;
inFile.open("C-small-attempt0.in");

ofstream outFile;
outFile.open("C-small.out");

inFile >> inLine;
t = atoi(inLine);


for(int c = 0; c < t; ++c) {
	inFile >> inLine;
	r = atof( inLine );
	
	inFile >> inLine;
	k = atof( inLine );
	
	inFile >> inLine;
	n = atof( inLine );
	
	
	for(int x = 0; x < n; x++) {
		inFile >> inLine;
		q[x] = atof( inLine );
	}
	
	
	double on = 0;

	for(int i = 0; i < r; ++i) {
		on = 0;
	
		for(long y = 0; y < n; ++y) {
			if(on + q[y] <= k) {
				on += q[y];			
			
			} else {
				for(int x = 0; x < y; ++x)
					queue(q, n);
				y = n;
			}
		}
	
		
		m += on;
	}
	outFile << "Case #" << c+1 << ": " << m << "\n";
	cout << c+1 << " of " << t << "\n";
	m = 0;

}

inFile.close();
outFile.close();
return 0;
}
