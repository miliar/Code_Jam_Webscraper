#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

int oq[1000], bq[1111];
int ocnt = 0, bcnt = 0;

struct Node {
    char bot[11];
    int sta;

    void input() {
        scanf("%s%d", bot, &sta);
        if (bot[0] == 'O') oq[ocnt++] = sta;
        else bq[bcnt++] = sta;
    }
} input[10000];

void init() {
    ocnt = 0, bcnt = 0;
}

void go(int &now, int next) {
    if (now < next) now++;
    else if (now > next) now--;
}

int main() {
    freopen("in", "r", stdin);
       freopen("out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++) {
        init();
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            input[i].input();
        }
        int cnt = 0;
        int now_o = 1, now_b = 1;
        int next_o = 0, next_b = 0;
        for (int i = 0; i < n;) {
            cnt++;
            bool unlock = true;
            if (input[i].bot[0] == 'O' && input[i].sta == now_o && unlock) {
                i++;
                next_o++;
              //  printf("%d O press %d\n", cnt, now_o);
                unlock = false;
            } else{
                int tmp = now_o;
                go(now_o, oq[next_o]);
            //    printf("time: %d   Orange %d---->%d\n",cnt, tmp, now_o);
            }
            if (input[i].bot[0] == 'B' && input[i].sta == now_b && unlock) {
                i++;
                next_b++;
           //     printf("%d B press %d\n", cnt, now_b);
            } else{
                int tmp = now_b;
                go(now_b, bq[next_b]);
          //      printf("time: %d  Black %d----->%d\n", cnt, tmp, now_b);
            }
        }
        printf("Case #%d: %d\n", cas, cnt);
    }
    return 0;
}

