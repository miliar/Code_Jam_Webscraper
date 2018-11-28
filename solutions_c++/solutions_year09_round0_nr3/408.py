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

int count(const char *s1, const char *s2) {
    const int L1 = strlen(s1);
    const int L2 = strlen(s2);
    if (L1 > L2) return 0;

    int T[L1 * L2];
    memset(T, 0, sizeof(int) * L1 * L2);
    int m = 0;
    for (int j = 0; j < L2; j++) {
	m += s1[0] == s2[j] ? 1 : 0;
	T[j * L1] = m;
    }
    for (int j = 1; j < L2; j++) {
	for (int i = 1; i < L1; i++) {
	    if (i > j) break;
	    int t = T[i + (j - 1) * L1];
	    if (s1[i] == s2[j]) {
		t += T[(i - 1) + (j - 1) * L1];
	    }
	    T[i + j * L1] = t % 10000;
	}
    }
    return T[L1 * L2 - 1];
}

int main(const int argc, const char *argv[]) {
    if (argc != 2) {
	usage(argc, argv);
    }

    const char *welcome = "welcome to code jam";
    int N;
    char line[501];

    ifstream inputfile(argv[1], ifstream::in);
    if (inputfile.is_open()) {
	inputfile >> N;
	inputfile.getline(line, 501); // read newline
	for (int t = 1; t <= N; t++) {
	    inputfile.getline(line, 501);
	    int m = count(welcome, line);

	    cout << "Case #" << t << ": ";
	    if (m < 1000) cout << "0";
	    if (m < 100) cout << "0";
	    if (m < 10) cout << "0";
	    cout << m << endl;
	}
    }
    inputfile.close();
}
