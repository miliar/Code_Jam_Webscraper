#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output.txt");

    int n;

    fin >> n;

    for (int i = 0; i != n; ++i) {
        int S, p, N, t, count = 0;
        fin >> N >> S >> p;
        int threshold = p * 3 - 3;

        for (int j = 0; j != N; ++j) {
            fin >> t;
            if (t > threshold) ++count;
            else if ((t == threshold || t == threshold - 1) && S > 0 && t > 1) {
                ++count;
                --S;
            }
        }

        fout << "Case #" << (i + 1) << ": " << count << endl;

    }

    fin.close();
    fout.close();
    return 0;
}
