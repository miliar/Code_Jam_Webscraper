#include <iostream>
#include <fstream>

using namespace std;

void main()
{
    ifstream fin("A-large.in");
    ofstream fout("A.out");
    int T;
    fin >> T;
    for (int tt = 1; tt <= T; ++tt)
    {
        unsigned int n, k;
        fin >> n >> k;
        bool state = false;
        if (k != 0)
        {
            state = (((k + 1) & ((1 << n) - 1)) == 0);
        }

        fout << "Case #" << tt << ": " << (state ? "ON" : "OFF") << endl;
    }
    fout.close();
    fin.close();
}
