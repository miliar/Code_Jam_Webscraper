#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <algorithm>

#include <cstdio>

using namespace std;

int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int main() {
    ifstream in("A.in");
    ofstream out("A.out");

    int tests;
    in >> tests;
    for (int t = 1; t <= tests; ++t) {
        int result = 0;

        long long n;
        int pd, pg;

        in >> n >> pd >> pg;

        //int pdd = gcd(pd, 100);

        //pd /= gcd(pd, 100);
        //pg /= gcd(pg, 100);

        int games = 100 / gcd(pd, 100);
        int needed = 100 / gcd(pd, 100) * 100 / gcd(pg, 100);

        bool broken;
        if ((pd != 100 && pg == 100) || (pd != 0 && pg == 0))
            broken = true;
        else if (games <= n && needed >= games)
            broken = false;
        else
            broken = true;

        if (!broken)
            out << "Case #" << t << ": " << "Possible" << endl;
        else
            out << "Case #" << t << ": " << "Broken" << endl;
    }
    return 0;
}
