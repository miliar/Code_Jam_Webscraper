#include <iostream>
#include <fstream>

using namespace std;

int T, N, K;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int main()
{
    fin >> T;
    for (int icase = 1; icase <= T; ++icase)
    {
        fout << "Case #" << icase << ": ";
        fin >> N >> K;
        if ((K + 1) % (1 << N) == 0)
            fout << "ON";
        else
            fout << "OFF";
        fout << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
