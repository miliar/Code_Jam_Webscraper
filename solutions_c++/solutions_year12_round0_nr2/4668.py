#include <fstream>

using namespace std;

int main() {
    ofstream fout ("dance2.out");
    ifstream fin ("dance2.in");
    int brtest, brgug, briz, trazena, ret, tgug, ost;

    fin >> brtest;

    for (int i=0; i<brtest; ++i) {
        fin >> brgug >> briz >> trazena;
        ret = 0;
        for (int j=0; j<brgug; ++j) {
            fin >> tgug;
            if (tgug == 0) {
                if (trazena == 0)
                    ret++;
                continue;
            }
            ost = tgug % 3;
            tgug /= 3;
            if (tgug == trazena-2 && ost == 2 && briz > 0) {
                ret++;
                briz--;
            } else if (tgug >= trazena || tgug == trazena-1 && ost > 0)
                ret++;
            else if (tgug == trazena - 1 && ost == 0 && briz > 0) {
                ret++;
                briz--;
            }
        }
        fout << "Case #" << i+1 << ": " << ret << endl;
    }

    return 0;
}
