#include "main.h"

using namespace std;

int main(int argc, char** argv) {
#ifdef DEBUG
    cerr << "Number of arguments: " << argc << endl;
    for (int i = 0; i < argc; i++)
        cerr << "Argument " << i << ": " << endl;
#endif // DEBUG

    if (argc != 2) {
        cout << "Wrong number of arguments!" << endl;
        cout << "Usage: " << argv[0] << " filename" << endl;
    }

    int** cases = new int*[10000];
    int ncases = getTestCases(argv[1], cases);

    for (int i = 0; i < ncases; i++) {
        int n = cases[i][0];
        int k = cases[i][1];

        bool result = runTestCase(n, k);

        cout << "Case #" << (i+1) << ((result) ? ": ON" : ": OFF") << endl;

        delete[] cases[i];
    }

    delete[] cases;

    return (EXIT_SUCCESS);
}

bool runTestCase(int n, int k) {
    int max = (int) pow(2, n);
    int steps = k % max;

    if (steps == (max - 1)) {
        return true;
    } else {
        return false;
    }
}

int getTestCases(char* filename, int** cases) {
    ifstream fin (filename, ifstream::in);

    if (fin.good()) {
        int ncases;

        fin >> ncases;

        for (int i = 0; i < ncases; i++) {
            int n, k;

            fin >> n >> k;

            cases[i] = new int[2];
            cases[i][0] = n;
            cases[i][1] = k;

#ifdef DEBUG
            cerr << "Test case #" << (i+1) << ": " << n << ", " << k << endl;
#endif // DEBUG
        }

        fin.close();

        return ncases;
    } else {
        return 0;
    }
}
