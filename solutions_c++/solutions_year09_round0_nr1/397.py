#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

void usage(const int argc, const char *argv[]) {
    const char *progname = strrchr(argv[0], '/');
    progname = progname ? progname + 1 : argv[0];
    cerr << "Usage: " << progname << " inputfile" << endl;
    exit(2);
}

int matches(const char *word, const char *pattern, int L) {
    int wp = 0;
    int pp = 0;
    while (pattern[pp]) {
	if (pattern[pp] == '(') {
	    pp++;
	    int m = 0;
	    while (pattern[pp] != ')') {
		if (pattern[pp] == word[wp]) {
		    m = 1;
		}
		pp++;
	    }
	    if (m == 0) return 0;
	}
	else {
	    if (pattern[pp] != word[wp]) return 0;
	}
	wp++;
	pp++;
    }
    return 1;
}

int main(const int argc, const char *argv[]) {
    if (argc != 2) {
	usage(argc, argv);
    }

    int L;
    int D;
    int N;

    ifstream inputfile(argv[1], ifstream::in);
    if (inputfile.is_open()) {
	inputfile >> L >> D >> N;
	char words[L*D];
	char w[L+1];
	for (int i = 0; i < D; i++) {
	    inputfile >> w;
	    strncpy(words + i * L, w, L);
	}
	char p[L*(28)+1];
	for (int t = 1; t <= N; t++) {
	    inputfile >> p;
	    int m = 0;
	    for (int i = 0; i < D; i++) {
		m += matches(words + i * L, p, L);
	    }
	    cout << "Case #" << t << ": " << m << endl;
	}
    }
    inputfile.close();
}
