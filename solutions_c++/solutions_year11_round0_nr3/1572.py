#include <fstream>

using namespace std;

int main()
{
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");

    int t;
    fin >> t;

    for (int cont = 1; cont <= t; ++cont) {
        int xor_value = 0;
        int total_value = 0;
        int min_value = 1000001;
        int n;
        fin >> n;
        for (int i = 0; i != n; ++i) {
            int temp;
            fin >> temp;
            xor_value ^= temp;
            total_value += temp;
            min_value = (temp < min_value) ? temp : min_value;
        }

        fout << "Case #" << cont << ": ";
        if (xor_value) {
            fout << "NO";
        }
        else {
            fout << (total_value - min_value);
        }
        fout << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
