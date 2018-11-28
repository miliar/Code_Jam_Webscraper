#include <iostream>
#include <math.h>
#include <fstream>
#include <cstdlib>
 
using namespace std;



int main() {
int t,n,k = 0;
char inLine[128];



ifstream inFile;
inFile.open("A-small-attempt0.in");

ofstream outFile;
outFile.open("aa.out");


// Get T on first line
inFile >> inLine;
t = atoi(inLine);

//cout << t+5 << endl;

for(int f = 0; f < t; ++f) {
	inFile >> inLine;
	n = atoi(inLine);
	inFile >> inLine;
	k = atoi(inLine);
	
	//cout << n << " \t " << k << "\n";
	
	int cp = 0;
	for(int i=0; i<=k; ++i) {
	
		while(cp >= pow(2, n))
				cp -= cp;
		
		cp++;
	}

	if(cp == pow(2, n))
		//cout << "CASE #" << f+1 << ": ON\t(" << n << ", " << k << ")\n";
		outFile << "Case #" << f+1 << ": ON\n";
	else
		outFile << "Case #" << f+1 << ": OFF\n";
		//cout << "CASE #" << f+1 << ": OFF\t(" << n << ", " << k << ")\n";
}

inFile.close();
outFile.close();

/*cout << "Please input T:\t";
cin >> t;


cout << "Please input N and K use space (eg: 4 5)\t";
cin >> n >> k;

cout << "\n";


int cp = 0;
for(int i=0; i<=k; ++i) {
	
	while(cp >= pow(2, n))
		cp -= cp;
		
	//cout << "X-";
	//binary(cp);
	//cout << "-sock\t (cp = " << cp << ")\n";
	cp++;
}

if(cp == pow(2, n))
	cout << "ON\n";
else
	cout << "OFF\n";
*/
return 0;
}
