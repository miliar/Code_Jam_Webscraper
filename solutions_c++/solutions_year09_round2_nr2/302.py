#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

string N, ret;

int main(int argc, char **argv) {

    ifstream in(argv[1]);
    ofstream out(argv[2]);

    int T;
    in >> T;
    for (int i = 1; i <= T; ++i) {
        in >> N;
        ret = N;
        out << "Case #" << i << ": ";
        if (next_permutation(N.begin(), N.end()))
            out << N;
        else {
            N = "0" + ret;
            next_permutation(N.begin(), N.end());
            out << N;
        }
        out << "\n";
    }

    return 0;
}
