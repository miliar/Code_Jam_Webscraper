//Google Codejam template
//Sabu Nadarajan 4/2012

//includes
#include <algorithm>
#include <fcntl.h>
#include <fstream>
#include <iostream>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <string>
#include <string.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {

	ifstream ifs(argv[1]);
	streambuf *buf;
	ofstream ofx;
	if (argc>2) {
		ofx.open((string(argv[1])+".output").c_str());
		buf = ofx.rdbuf();
	} else {
		buf = cout.rdbuf();
	}
	ostream myout(buf);
	string line;
	int nnum, A, B, n, m, cnt, i, j, k;

	ifs >> nnum;
	for (i=1; i<=nnum; i++) {
		ifs >> A >> B;
		cnt = 0;
		for (j = A; j < B; j++) {
			if (j>99) {
				k = (j%10)*100+j/10;
				if ((k>j) && (k<=B)) cnt++;
				k = (j%100)*10+j/100;
				if ((k>j) && (k<=B)) cnt++;
			}
			if (j>9) {
					k = (j%10)*10+j/10;
					if ((k>j) && (k<=B)) cnt++;
			}
			if ((j*10)<=B) cnt++;
			if ((j*100)<=B) cnt++;
			if ((j*1000)<=B) cnt++;
		}
		myout << "Case #" << i << ": " << cnt << endl;
	}

	return 0;
}
// End of file
