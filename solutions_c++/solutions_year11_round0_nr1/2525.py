#include<iostream>
#include<vector>

using namespace std;

int getRobot(char r) {
    return r=='O'?0:1;
}

int abs(int x) {
    return x>0?x:-x;
}

int mx(int a, int b){
    return a>b?a:b;
}

int sig(int x) {
    return x>0?x:0;
}

int main() {
    int T;
    scanf("%d\n", &T);
    for(int tt = 1 ; tt <= T ; tt++) {
        int N;
        scanf("%d ", &N);

        int total = 0;
        
        bool b = false, o = false;
        int tb = 0, to = 0;
        int pb = 1, po = 1;

        int bb = 0, bo = 0;
        
        for(int i = 0 ; i < N ; i++) {
            char r;
            int p;
            scanf("%c %d ",&r,&p);
            if(r=='O') {
                to += sig(abs(p - po) - bo) + 1;
                po = p, bo = 0;
                o = true;
            } else {
                tb += sig(abs(p - pb) - bb) + 1;
                pb = p, bb = 0;;
                b = true;
            }

            if(b && o) {
                if(r=='B') {
                    total += mx(to, tb -1) + 1;
                    bo = tb>to?tb-to:1;
                } else {
                    total += mx(tb, to - 1) + 1;
                    bb = to>tb?to-tb:1;
                }
                to = 0, tb = 0;
                b = false, o = false;
            }
            //printf("to,bo = (%d,%d) , tb,bb = (%d,%d), total = %d\n", to, bo, tb, bb, total);
        }

        total += to + tb;
        printf("Case #%d: %d\n", tt, total);
    }
}
