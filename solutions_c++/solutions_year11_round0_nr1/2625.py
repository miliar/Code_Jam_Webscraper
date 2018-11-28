#include <stdio.h>
#include <stdlib.h>


struct botstatus {
        int pos, time;
        botstatus() : pos(1), time(0) {}
};

struct pairstatus {
        botstatus s[2];
};

pairstatus press(pairstatus in, char botchar, int button) {
        pairstatus res = in;
        int mover, other;
        if (botchar == 'O') {
                mover = 0;
        } else if (botchar == 'B') {
                mover = 1;
        } else {
                printf("bad bot '%c'\n", botchar);
                exit(1);
        }
        other = 1 - mover;
        int dist = abs(button - res.s[mover].pos);
        res.s[mover].time += dist + 1;
        if (res.s[mover].time <= res.s[other].time) {
                res.s[mover].time = res.s[other].time + 1;
        }
        res.s[mover].pos = button;
        return res;
}

int main() {
        int ncases;
        scanf("%d\n", &ncases);
        int i, j;
        for(i = 1; i <= ncases; i++) {
                pairstatus state;
                int nbuttons;
                scanf("%d", &nbuttons);
                for(j = 0; j < nbuttons; j++) {
                        char bot;
                        int pos;
                        scanf(" %c %d", &bot, &pos);
                        state = press(state, bot, pos);
                }
                int maxtime = (state.s[0].time > state.s[1].time) ? state.s[0].time : state.s[1].time;
                printf("Case #%d: %d\n", i, maxtime);
        }

}
