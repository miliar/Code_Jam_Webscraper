#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

enum {
    PUSH_BUTTON_ORANGE,
    PUSH_BUTTON_BLUE,
};

int run(int pos, list<int>& ls, bool canPush, bool* pushed) {
    if (ls.empty()) return pos;

    int dest = ls.front();
    if (pos == dest) { // push button
        if (canPush) {
            *pushed = true;
            ls.pop_front();
        }
        return pos;
    }
    else { // move to
        int x = dest - pos;
        // printf("pos:%d dest:%d next:%d\n", pos, dest, pos+x/abs(x));
        return pos + x/abs(x);
    }
}

int calc(list<int>& pushRobots, list<int>& orange, list<int>& blue) {
    int op = 1; // orange position
    int bp = 1; // blue   position

    int pushRobot = pushRobots.front();
    pushRobots.pop_front();
    for (int i = 1; ; i++) {
        if (orange.empty() && blue.empty()) return i-1;

        bool pushed = false;
        op = run(op, orange, pushRobot == PUSH_BUTTON_ORANGE, &pushed);
        bp = run(bp, blue,   pushRobot == PUSH_BUTTON_BLUE,   &pushed);

        if (pushed && !pushRobots.empty()) {
            pushRobot = pushRobots.front();
            pushRobots.pop_front();
        }
    }
    assert(false);
}

int main() {
    int ncases;
    scanf("%d", &ncases);
    For(cc, ncases) {
        int n;
        scanf("%d", &n);

        list<int> pushRobots;
        list<int> orange, blue;
        For(i, n) {
            char s[100];
            int no;
            scanf("%s %d", s, &no);
            if (s[0] == 'O') {
                orange.push_back(no);
                pushRobots.push_back(PUSH_BUTTON_ORANGE);
            }
            else {
                blue.push_back(no);
                pushRobots.push_back(PUSH_BUTTON_BLUE);
            }
        }

        printf("Case #%d: %d\n", cc+1, calc(pushRobots, orange, blue));
    }
}
