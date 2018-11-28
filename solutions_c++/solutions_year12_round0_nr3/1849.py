#include <iostream>
#include <set>
#include <string>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;


// def solve(a, b):
//     pairs = set()
//     c = 0
//     for n in range(a, b):
//         ns = str(n)
//         for shift in range(1, len(ns)):
//             nsShifted = ns[-shift:] + ns[:-shift]
//             if nsShifted[0] == '0': continue
//             # print("%s %s" % (ns, nsShifted))
//             nShifted = int(nsShifted)
//             if nShifted > n and nShifted <= b:
//                 pairs.add((n, nShifted))
//     return len(pairs)

int solve(const int a, const int b)
{
    set<pair<int,int> > pairs;
    for (int n = a; n < b; n++) {
        char ns[32];
        sprintf(ns, "%d", n);
        int len = strlen(ns);
        for (int shift = 1; shift < len; shift++) {
            char ms[32];
            for (int j = 0; j < len; j++) {
                int idx = (j-shift);
                if (idx < 0) idx += len;
                ms[j] = ns[ idx ];
            }
            if (ms[0] == '0') continue;
            ms[len] = 0;
            int m = atoi(ms);
            if (m > n && m <= b) {
                // cout << "(" << n << ", " << m << ")" << endl;
                pairs.insert(make_pair<int, int>(n, m));
            }
        }
    }
    return pairs.size();
}

int main()
{
    int numcases; cin >> numcases;
    for (int i = 0; i < numcases; i++) {
        int a; cin >> a;
        int b; cin >> b;
        cout << "Case #" << (i+1) << ": " << solve(a, b) << endl;
    }
    return 0;
}
