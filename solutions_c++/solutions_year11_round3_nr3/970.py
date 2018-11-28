#include <fstream>

using namespace std;

int main(int argc, char** argv) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int T;
    fin >> T;

    for (int t = 1; t <= T; ++t) {
        int N;
        long long L, H;
        fin >> N >> L >> H;
        long long notes[10000];
        for (int n = 0; n < N; ++n) {
            fin >> notes[n];
        }
        bool endt = false;
        fout << "Case #" << t << ": ";
        for (int i = L; i <= H; ++i) {
            bool possible = true;
            for (int n = 0; n < N; ++n) {
                if (i%notes[n] != 0 && notes[n]%i != 0) {
                    possible = false;
                    break;
                }
            }
            if (possible) {
                fout << i << endl;
                endt = true;
                break;
            }
        }
        if (!endt)
            fout << "NO" << endl;
    }
}

