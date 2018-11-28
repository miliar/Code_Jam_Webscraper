#include <cstdio>
#include <iostream>

using namespace std;

char type[100];
int pos[100];

int abs(int a) {
    if (a < 0) a = -a;
    return a;
}

int main() {
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int t1 = 0; t1 < t; t1++) {
        int n;
        cin >> n;
        for (int i = 0; i < n; i++) cin >> type[i] >> pos[i];
        int dest1 = -1; int dest2 = -1;
        int p1 = 1; int p2 = 1;
        int k = 0;
        while (dest1 < n && type[dest1] != 'O') dest1++;
        while (dest2 < n && type[dest2] != 'B') dest2++;
        while (dest1 < n || dest2 < n) {
            if (dest1 < dest2) {
                int r1 = abs(p1 - pos[dest1]);
                if (dest2 < n) {
                    int r2 = abs(p2 - pos[dest2]);
                    if (r2 <= r1) p2 = pos[dest2]; else
                    if (p2 < pos[dest2]) p2 += (r1 + 1); else p2 -= (r1 + 1);
                }
                p1 = pos[dest1];
                k += r1 + 1;
                dest1++;
                while (dest1 < n && type[dest1] != 'O') dest1++;
            } else {
                int r1 = abs(p2 - pos[dest2]);
                if (dest1 < n) {
                    int r2 = abs(p1 - pos[dest1]);
                    if (r2 <= r1) p1 = pos[dest1]; else
                    if (p1 < pos[dest1]) p1 += (r1 + 1); else p1 -= (r1 + 1);
                }
                p2 = pos[dest2];
                k += r1 + 1;
                dest2++;
                while (dest2 < n && type[dest2] != 'B') dest2++;
            }
        }
        cout << "Case #" << t1 + 1 << ": " << k << endl;
    }
    return 0;
}
