#include <iostream>
#include <fstream>
using namespace std;

/*
 * 
 */

unsigned long pow2(unsigned int w) {
    unsigned long s = 1;
    for (; w > 0; --w) {s *= 2;}
    return s;
}

bool is(int n, int k) {
    if ((k+1) % (pow2(n)) == 0) return true;
    else return false;
}

int main(int argc, char** argv) {

    /*const int y = 4;
    bool g[y];
    int c = 0;

    cout << pow2(10) << endl;

    for (int i = 0; i < y; i++) g[i] = false;

    for (int i = 1; i < 300; i++)
    {
        for (int h = 0; h <= c; h++) {
            if (g[h]) g[h] = false;
            else g[h] = true;
        }
        for (c = 0; c < y; c++)
            if (!g[c]) break;
        cout << c << " ";
        for (int h = 0; h < y; h++)
            if (g[h]) cout << "1";
            else cout << "0";
        cout << " " << i << endl;
    }

    cout << endl << "------------------------------------------" << endl;*/

    ifstream in("/home/r5ha/A-large.in");
    if (!in) {return 0;}
    int t;
    in >> t;

    ofstream ou("/home/r5ha/A.out");
    int n, k;
    for (int i = 1; i <= t; i++) {
        in >> n >> k;
        ou << "Case #" << i << ": " << ((is(n, k)) ? "ON" : "OFF") << endl;
    }

    in.close();
    ou.close();
    
    return 0;
}