#include <stdio.h>
#include <iostream>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <string>
#include <algorithm>
#include <math.h>

static void process(std::set<int>& table, 
                    int k, 
                    int A,
                    int B,
                    int *total)
{
    std::stringstream ss;
    ss << k;
    std::string str = ss.str();
    const int size = str.size();
    const int mut = (int)pow(10, size);
    int ti = 0;
    for (int i = 0; i < size; ++i) {
        const int f = (int)pow(10, i);
        const int kk = k / f + (k % f) * mut / f;
        if (kk >= A && kk <= B && table.find(kk) == table.end()) {
            table.insert(kk);
            ti++;
        }
    }
    if (ti > 1)
        *total += ti * (ti - 1) / 2;
}

int main(int argc, char *argv[])
{
    int T;
    scanf("%d\n", &T);
    for (int i = 1; i <= T; ++i) {
        std::set<int> table;
        int A, B;
        std::cin >> A >> B;
        int total = 0;
        for (int j = A; j <= B; ++j) {
            if (table.find(j) != table.end()) {
                // processed
                continue;
            }
            process(table, j, A, B, &total);
        }
        printf("Case #%d: %d\n", i, total);
    }
    return 0;
}
