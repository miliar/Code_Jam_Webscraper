#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void countfn (int x, int y);

char test[510];
char welcome[25]="welcome to code jam";
int testsize, ct;
int welsize = 19;

int main()
{
	int N, n;
	char a[3];
	ifstream myfile ("input.in");
	ofstream output ("output.txt", ios::trunc);
	
	myfile >> N;
	myfile.getline(a,3);

	for (n=1;n<=N;n++) {
		ct = 0;
		myfile.getline(test, 510);
		testsize=strlen(test);

		if (testsize > welsize) {
			countfn(0,0);
		}
		else {
			if (!strcmp(test,welcome)) ct=1;
		}
		output << "Case #" << n << ": ";
		if (ct<1000) output << "0";
		if (ct<100) output << "0";
		if (ct<10) output << "0";
		output << ct << "\n";
	}

	return 0;
}

void countfn (int x, int y) {
	int c;
	for (c=y; c<(testsize-(welsize-x)+1); c++) {
		if (test[c]==welcome[x]) {
			if (x<18) countfn(x+1,c+1);
			else ct = (ct++) % 10000;
		}
	}
	return;
}
