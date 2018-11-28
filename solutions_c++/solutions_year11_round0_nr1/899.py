#pragma comment(linker, "/STACK:40000000") 

#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>


int main()
{
    freopen("i.txt", "r", stdin);
    freopen("o.txt", "w", stdout);

    int N;
    scanf("%d", &N);
    for (int I = 1; I <= N; ++I) {
        int n, no = 0, nb = 0;
        int o[100], b[100], o_pos[100], b_pos[100];

        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            char c;
            int pos;
            scanf(" %c %d", &c, &pos);
            if (tolower(c) == 'b') {
                b[nb] = pos;
                b_pos[nb] = i;
                ++nb;
            } else {
                o[no] = pos;
                o_pos[no] = i;
                ++no;
            }
        }
        scanf("\n");

        int io = 0, ib = 0, cnt = 0, step = 0, bpos = 1, opos = 1;
        while (io < no || ib < nb) {
            bool fStep = false;
            if (io < no) {
                if (o[io] < opos) {
                    --opos;
                } else if (o[io] > opos) {
                    ++opos;
                } else if (o[io] == opos && o_pos[io] == step && !fStep) {
                    ++step;
                    ++io;
                    fStep = true;
                }
            }
            if (ib < nb) {
                if (b[ib] < bpos) {
                    --bpos;
                } else if (b[ib] > bpos) {
                    ++bpos;
                } else if (b[ib] == bpos && b_pos[ib] == step && !fStep) {
                    ++step;
                    ++ib;
                    fStep = true;
                }
            }

            ++cnt;
        }

        printf("Case #%d: %d\n", I, cnt);
    }

    return 0;
}
