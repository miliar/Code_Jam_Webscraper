#include <fstream>
#include <climits>

using namespace std;

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int T;
    fin >> T;

    for (int t = 1; t <= T; ++t) {
        int N;
        fin >> N;
        unsigned long long sean = 0, patrick = 0, min = INT_MAX;
        unsigned long long candy;
        for (int n = 0; n < N; ++n) {
            fin >> candy;
            sean += candy;
            patrick ^= candy;
            if (candy < min)
                min = candy;
        }
        fout << "Case #" << t << ": ";
        if (patrick != 0)
            fout << "NO";
        else
            fout << sean-min;
        fout << endl;
    }
}

