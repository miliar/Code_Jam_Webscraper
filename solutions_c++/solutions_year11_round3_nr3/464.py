#include <fstream>

using namespace std;

int main()
{
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small-attempt0.out");

    int t;
    fin >> t;
    for (int cont = 1; cont <= t; ++cont) {
        int n;
        int l, h;
        fin >> n >> l >> h;

        int note[n];
        for (int i = 0; i != n; ++i) {
            fin >> note[i];
        }

        bool result = false;
        int number = 0;
        for (int i = l; i <= h; ++i) {
            bool flag = false;
            for (int j = 0; j != n; ++j) {
                if (note[j] % i != 0 && i % note[j] != 0) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                result = true;
                number = i;
                break;
            }
        }

        fout << "Case #" << cont << ": ";
        if (result) fout << number << endl;
        else fout << "NO" << endl;
    }


    fin.close();
    fout.close();
    return 0;
}
