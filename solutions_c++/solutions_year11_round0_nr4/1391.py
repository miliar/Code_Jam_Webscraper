#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int main() {
//     freopen("input.txt", "rt", stdin);
//     freopen("D-small-attempt0.in", "rt", stdin);
    freopen("D-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tt,a,res,n;
    cin >> tt;
    for (int ii = 1; ii <= tt; ii++) {
        res = 0;
        cin >> n;
        for (int i = 1; i <= n; i++) {
            cin >> a;
            if (a != i)
                res++;
        }
        cout << "Case #" << ii << ": " << res << endl;
    }
    return 0;
}
