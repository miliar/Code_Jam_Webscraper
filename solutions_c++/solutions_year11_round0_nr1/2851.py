#include <cstdlib>
#include <climits>
#include <sstream>
#include <string>
#include <iostream>
#include <cstdio>

// STL
#include <algorithm>
#include <vector>
#include <map> // contains multimap
#include <set> // contains multiset
#include <queue> // contains priority_queue
#include <deque>
#include <list>
#include <stack>


using namespace std;

typedef struct _seq {
    int col;
    int pos;
} seq;

int solve(int k) {
    int pos[2]; // 0 = orange / 1 = blue
    int steps = 0, available_steps = 0, tmpi;
    int current_color;
    char tmp;
    seq sol[k];

    for (int i = 0; i < k; ++i) {
        cin >> tmp >> sol[i].pos;
        if (tmp == 'O')
            sol[i].col = 0;
        else sol[i].col = 1;
    }

    current_color = sol[0].col;
    pos[0] = (pos[1] = 1);

    for (int i = 0; i < k; ++i) {
        if (sol[i].col == current_color) {
            tmpi = sol[i].pos - pos[sol[i].col];
            pos[sol[i].col] = sol[i].pos;
            tmpi = tmpi > 0 ? tmpi + 1 : -tmpi + 1;
            available_steps += tmpi;
            steps += tmpi;
        } else {
            tmpi = sol[i].pos - pos[sol[i].col];
            pos[sol[i].col] = sol[i].pos;
            tmpi = tmpi > 0 ? tmpi + 1: -tmpi + 1;
            available_steps -= tmpi;
            if (available_steps < 0) {
                available_steps = -available_steps;
                steps += available_steps;
                current_color = sol[i].col;
            } else {
                available_steps = 1;
                steps += 1;
                current_color = sol[i].col;
            }
        }
    }

    return steps;
}


int main() {
    int numcase, k;

    freopen("A-large.in", "r", stdin);
    //freopen("robots.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> numcase;
    for (int i = 0; i < numcase; ++i) {
        cin >> k;
        cout << "Case #" << i + 1 << ": " << solve(k) << endl;
    }

    return 0;
}
