#include <fstream>
#include <iostream>
using namespace std;

#define INPUTFILE "D:\A-small.in"
#define OUTPUTFILE "D:\A-small.out"

int main(void) {
	ifstream fi;
	fi.open(INPUTFILE);
	ofstream fo;
	fo.open(OUTPUTFILE);
	int T;
	fi >> T;
	unsigned int N, K;
	for (int i = 1; i <= T; i++) {
		fi >> N >> K;
		//if (i < 20) cout << N << " " << K << endl;
		N = (1 << N) - 1;
		if ((K & N) == N)
			fo << "Case #" << i << ": ON" << endl;
		else
			fo << "Case #" << i << ": OFF" << endl;
	}
	//cin >> K;
	fi.close();
	fo.close();
}