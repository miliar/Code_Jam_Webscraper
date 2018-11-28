#include <iostream>
#include <fstream>
using namespace std;

bool is_invalid(int p, int t) {
    if (p > t) return true;
    int b = 3*p - 4;
    if (b < 0) return false;
    if (t < b) return true;
    return false;
}

bool is_surprising(int p, int t) {
    int b = 3*p - 2;
    if (b < 0) return false;
    if (t < b) return true;
    return false;
}

int main() {

    //ifstream ifs ( "pA.txt" , ifstream::in );

    int lc = 1;
    int T = 0;
    int *t = new int[100+1];
    cin >> T;
    cin.get();
    while (!cin.eof()) {
        if (lc > T) break;

        int N, S, p;
        int s = 0, res = 0;
        cin >> N >> S >> p;

        for (int i = 0; i < N; ++i) {
            cin >> t[i];
            if (!is_invalid(p, t[i])) {
                if (is_surprising(p, t[i])) {
                    ++s;
                    if (s <= S) ++res;
                }
                else ++res;
            }
        }

        cout << "Case #" << lc << ": " << res << endl;

        cin.get();
        ++lc;
    }
    delete[] t;

    //ifs.close();

    return 0;
}

