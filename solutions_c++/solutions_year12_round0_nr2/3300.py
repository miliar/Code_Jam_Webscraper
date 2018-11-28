#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("y.out", "w", stdout);

    int t, n, s, p, num, count;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        scanf("%d%d%d", &n, &s ,& p);
        count = 0;
        for (int j = 0; j < n; j++) {
            scanf("%d", &num); // read total scores     
            int sc1 = num / 3, sc2 = (num - sc1) / 2, sc3 = num - sc1 - sc2;
            if (sc1 >= p || sc2 >= p || sc3 >= p)count++;
            else if (s > 0) {
                if (sc1>0&&sc1 == sc2 && sc1 == p - 1) {
                    s--;
                    count++;
                } else if (sc2>0&&sc2 == sc3 && sc2 ==p - 1) {
                    s--;
                    count++;
                } else if (sc1>0&&sc1 == sc3 && sc1 == p - 1) {
                    s--;
                    count++;
                }
            }
        }
        printf("Case #%d: %d\n", (i+1),count);

    }


}