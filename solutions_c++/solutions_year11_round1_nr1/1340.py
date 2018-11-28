#include <fstream>

using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");

    int t;
    fin >> t;

    for (int i = 1; i <= t; ++i) {
        int n, pd, pg;

        fin >> n >> pd >> pg;

        if ((pg == 100 && pd != 100) || (pg == 0 && pd != 0)) {
            fout << "Case #" << i << ": " << "Broken" << endl;
            continue;
        }

        int count[2];
        count[0] = count[1] = 0;
        while (pd % 2 == 0 && count[0] < 2) {
            ++count[0];
            pd /= 2;
        }
        while (pd % 5 == 0 && count[1] < 2) {
            ++count[1];
            pd /= 5;
        }

        int temp = 1;
        if (count[0] < 2) temp *= (count[0]) ? 2 : 4;
        if (count[1] < 2) temp *= (count[1]) ? 5 : 25;

        if (temp <= n) {
            fout << "Case #" << i << ": " << "Possible" << endl;
            continue;
        }
        else {
            fout << "Case #" << i << ": " << "Broken" << endl;
            continue;
        }

    }

    fin.close();
    fout.close();

    return 0;
}
