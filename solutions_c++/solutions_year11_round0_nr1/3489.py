//
//  main.cpp
//  A
//
//  Created by MMX on 11/05/07.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

class seq {
public:
    int pos;
    char r;
    seq (char a, int b) {
        r = a;
        pos = b;
    }
};

int main (int argc, const char * argv[])
{
    int T, N;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int pos;
        char r;
        int b_pos = 1, o_pos = 1;
        int now = 0, b_free = 0, o_free = 0, need_time = 0;
        vector<seq> input;
        scanf("%d", &N);
        for (int n = 0; n < N; n++) {
            scanf(" %c", &r);
            scanf("%d", &pos);
            seq *s = new seq(r, pos);
            input.push_back(*s);
        }
        for (int i = 0; i < input.size(); i++) {
            pos = input[i].pos;
            if (input[i].r == 'B') {
                need_time = abs(pos - b_pos) - b_free;
                if (need_time > 0) {
                    o_free += need_time;
                    now += need_time;
                }
                b_pos = pos;
                b_free = 0;
                o_free += 1;
                now += 1;
            }
            if (input[i].r == 'O') {
                need_time = abs(pos - o_pos) - o_free;
                if (need_time > 0) {
                    b_free += need_time;
                    now += need_time;
                }
                o_pos = pos;
                o_free = 0;
                b_free += 1;
                now += 1;
            }
        }
        printf("Case #%d: %d\n", t + 1, now);
    }
    return 0;
}

