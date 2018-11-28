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
	string word, orig;
	string::iterator si;
	char trans[] = "yhesocvxduiglbkrztnwjpfmaq";
	char t;
	int nnum;

	ifs >> nnum;
	getline(ifs, line);  //skip newline
	for (int i=1; i<=nnum; i++) {
		getline(ifs, line);
		for (si=line.begin(); si!=line.end(); si++) {
			if ((*si != ' ') && (*si != '\r') && (*si != '\n')) {
			t = trans[*si-'a'];
			*si = t;
			}
		};
		myout << "Case #" << i << ": " << line << endl;
	}

	return 0;
}
// End of file
