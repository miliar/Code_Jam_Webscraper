/*
 * a.cpp
 *
 *  Created on: May 7, 2010
 *      Author: shane
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <math.h>

using namespace std;

bool isOn(long n, long k)
{
    //    if (n == 0)
    //        return true;
    //
    //    if (k == 0)
    //        return false;
    //
    //    if (n == 1)
    //        return k % 2 == 1;

    long long c = 2 * powl(2, n - 1);

    long long f = c - 1;

    if (k < f)
        return false;

    if (k == f)
        return true;

    long long r = k - f;

    return ((k - f) % c) == 0;
}

int main(int argc, char**argv)
{
    string inname = argv[1];
    inname += ".in";

    string outname = argv[1];
    outname += ".out";

    ifstream in(inname.c_str());
    ofstream out(outname.c_str());

    cout << "Reading from : " << inname << endl;
    cout << "Writing to   : " << outname << endl;

    int tests;

    in >> tests;
    cout << "Running test cases: " << tests << endl;

    in.get(); // read past new line

    for (int test = 1; test <= tests; test++)
    {
        string line;
        long n, k;
        in >> n >> k;
        bool on = isOn(n, k);

        ostringstream res;
        res << "Case #" << test << ": " << (on ? "ON" : "OFF") << endl;
        cout << res.str();
        out << res.str();
    }
    return 0;
}
