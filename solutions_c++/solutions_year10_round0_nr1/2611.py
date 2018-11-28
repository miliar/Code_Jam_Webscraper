#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{
    ifstream in;
    in.open("A-small.in");
    if (!in) {
        cerr << "Err, what's happening with input file." << endl;
        return 1;
    }

    ofstream out;
    out.open("out.txt");
    int t;
    in >> t;

    int n, k;
    for (int i = 0; i < t; ++i) {
        in >> n >> k;

        if (!k || (k + 1) % (int) pow((double) 2, n))
            out << "Case #" << i + 1 << ": OFF";
        else
            out << "Case #" << i + 1 << ": ON";
        if (i != t - 1)
            out << endl;
    }
}
