#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

long count(long a, long b);

int main()
{
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small-attempt0.out");

    long a = 0;
    long b = 0;

    int nSamples = 0;
    fin >> nSamples;
    for(int i = 0; i < nSamples; i++) {
        fin >> a >> b;
        fout << "Case #" << i+1 << ": " << count(a, b) << endl;
    }
    return 0;
}

long count(long a, long b) {
    if(a >= b)
        return 0;
    int len = int(log10(a)) + 1;
    if(len != int(log10(b)) + 1 || len <= 1) {
        return 0;
    }

    long npairs = 0;
    for(long int n = a; n <= b; n++) {
        for(int k = 2; k <= len; k++) {
            long head = n / pow(10, len - k + 1);
            long tail = n - head * pow(10, len - k + 1);
            long nRecycle = tail * pow(10, k - 1) + head;
            if(nRecycle > n && nRecycle <= b) {
//                cout << n << "\t" << nRecycle << endl;
                ++npairs;
            }
        }
    }
    return npairs;
}
