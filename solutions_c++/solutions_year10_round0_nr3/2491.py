/*
 * a.cpp
 *
 *  Created on: May 7, 2010
 *      Author: shane
 */

#include <iostream>
#include <fstream>
#include <queue>
#include <sstream>

using namespace std;

typedef unsigned long ulong;

ulong calc(ulong r, ulong k, queue<ulong> g)
{
    ulong e = 0;

    for (int i = 0; i < r; i++)
    {
        queue<ulong> t;
        ulong p = 0;

        while (!g.empty() && p + g.front() <= k)
        {
            ulong c = g.front();
            g.pop();
            t.push(c);
            p += c;
        }

        e += p;

        while (!t.empty())
        {
            g.push(t.front());
            t.pop();
        }
    }

    return e;
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
        ulong r, k, n;

        in >> r >> k >> n;
        queue<ulong> g;

        for (int i = 0; i < n; i++)
        {
            ulong p;
            in >> p;
            g.push(p);
        }

        in.get();

        ostringstream res;
        res << "Case #" << test << ": " << calc(r, k, g) << endl;
        cout << res.str();
        out << res.str();
    }
    return 0;
}
