#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <deque>
#include <queue>
#include <cmath>
#include <new>
#include <map>
#include <set>
using namespace std;

int main()
{
    ifstream fin("1.in");
    ofstream fout("1.out");
    int T, N, K;
    fin >> T;
    int f[31];
    memset(f, 0, sizeof f);
    f[0] = 0;
    for (int i = 1; i <= 30; ++i)
    {
        for (int j = 1; j < i; ++j)
            f[i] += f[j];
        ++f[i];
    }
    
    int poteza[31];
    memset(poteza, 0, sizeof poteza);
    for (int i = 0; i <= 30; ++i)
        for (int j = 1; j <= i; ++j)
            poteza[i] += f[j];
    for (int brojac = 1; brojac <= T; ++brojac)
    {
        fin >> N >> K;
        K -= poteza[N];
        if (K < 0)
            fout << "Case #" << brojac << ": " << "OFF" << endl;
        else if (K % (poteza[N] + 1) == 0)
            fout << "Case #" << brojac << ": " << "ON" << endl;
        else
            fout << "Case #" << brojac << ": " << "OFF" << endl;
    }
    return 0;
}
