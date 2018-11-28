#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <numeric>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <ctime>
#include <cctype>
#include <fstream>
using namespace std;

int r[10000], x[10000], y[10000], id[10000];

int cmp(int a, int b) {
    return r[a] > r[b];
}

int main() {
    int tott, w, l, n;
    scanf("%d", &tott);
    for (int curt = 0; curt < tott; ++curt) {
        scanf("%d%d%d", &n, &w, &l);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &r[i]);
            id[i] = i;
        }
        sort(id, id + n, cmp);
        int ptr = 1;
        x[id[0]] = 0;
        y[id[0]] = 0;
        int right = r[id[0]];
        while (ptr < n && right + r[id[ptr]] <= w) {
            x[id[ptr]] = right + r[id[ptr]];
            y[id[ptr]] = 0;
            right = x[id[ptr]] + r[id[ptr]];
            ++ptr;
        }

        int top = r[id[0]];
        while (ptr < n) {
            int first = id[ptr];
            x[first] = 0;
            y[first] = top + r[first];
            if (y[first] > l) {
                printf("ERROR\n");
                return 1;
            }
            int right = r[first];
            ++ptr;
            while (ptr < n && right + r[id[ptr]] <= w) {
                x[id[ptr]] = right + r[id[ptr]];
                y[id[ptr]] = y[first];
                right = x[id[ptr]] + r[id[ptr]];
                ++ptr;
            }

            top = top + 2*r[first];
        }

        printf("Case #%d:", curt + 1);
        for (int i = 0; i < n; ++i) {
            printf(" %d %d", x[i], y[i]);
        }
        printf("\n");
    }
    return 0;
}
