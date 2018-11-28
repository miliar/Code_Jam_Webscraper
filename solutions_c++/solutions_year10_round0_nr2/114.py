#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("B-small.in");
ofstream fout("B-small.out");

int N, D, T, prev, delta, when;

int gcd(int x, int y)
{
    return y == 0 ? x : gcd(y, x % y);
}

void solve()
{
    fin >> N;
    prev = 0;
    D = 0;
    fin >> prev;
    for (int i = 0; i < N - 1; ++i)
    {
        fin >> when;
        int delta = abs(when - prev);
        D = gcd(D, delta);
        prev = when;
    }
    fout << (D - when % D) % D << endl;
}

int main()
{
    fin >> T;
    for (int cas = 1; cas <= T; ++cas)
    {
        fout << "Case #" << cas << ": ";
        solve();
    }
    return 0;
}
