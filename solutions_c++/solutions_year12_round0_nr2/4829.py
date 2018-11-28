#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <queue>

using namespace std;

int main() {
    int t;
    scanf ("%d", &t);
    for (int z = 1; z <= t; z++) {
        int n, s, p, polje[105], res = 0;
        scanf ("%d %d %d", &n, &s, &p);
        for (int i = 0; i < n; i++) {
            scanf ("%d", &polje[i]);   
        }   
        
        for (int i = 0; i < n; i++) {
            if (p + 2 * max (0, p - 1) <= polje[i]) {
                res++;   
            } else if (s > 0 && p + 2 * max (0, p - 2) <= polje[i]) {
                res++;
                s--;   
            }
        }        
        printf ("Case #%d: %d\n", z, res);
    }
    return 0;
}
