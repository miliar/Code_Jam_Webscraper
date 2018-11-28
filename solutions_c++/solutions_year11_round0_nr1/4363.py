#include <cstdio>
#include <cstdlib>
using namespace std;

int main() {
    int t;
    int n;
    int tmp1, k1, k2, k3, cb, co, cpo, cpb, total;
    char tmp;
    int color[200], place[200];
    scanf(" %d", &t);
    for(int j=0;j<t;j++) {
        scanf(" %d", &n);
        k1 = 0;
        for(int i=0;i<n;i++) {
            scanf(" %c %d", &tmp, &tmp1);
            if(tmp == 'O') {
                color[k1] = 0;
            } else {
                color[k1] = 1;
            }
            place[k1] = tmp1;
            k1++;
        }

        k3 = 0; //b
        k2 = 0; //o
        cb = 1; //nextb
        co = 1; //nexto
        while(k2 < k1 && color[k2] == 1)k2++;
        co = place[k2];
        while(k3 < k1 && color[k3] == 0)k3++;
        cb = place[k3];
        cpo = 1;
        cpb = 1;
        total = 0;

        while(1){
            if(k2 < k3 && k2 < k1 && k3 < k1) {
                int dis = co > cpo ? co - cpo : cpo - co;
                total += dis + 1;
                cpo = co;
                if(cpb > cb) {
                    if(cpb - cb <= dis + 1) {
                        cpb = cb;
                    } else {
                        cpb -= dis + 1;
                    }
                } else {
                    if(cb - cpb <= dis + 1) {
                        cpb = cb;
                    } else {
                        cpb += dis +1;
                    }
                }
                k2++;
                while(k2 < k1 && color[k2] == 1)k2++;
                co = place[k2];
            } else if(k3 < k2 && k3 < k1 && k2 < k1) {
                int dis = cb > cpb ? cb - cpb : cpb - cb;
                total += dis + 1;
                cpb = cb;
                if(cpo > co) {
                    if(cpo - co <= dis + 1) {
                        cpo = co;
                    } else {
                        cpo -= dis + 1;
                    }
                } else {
                    if(co - cpo <= dis + 1) {
                        cpo = co;
                    } else {
                        cpo += dis + 1;
                    }
                }
                k3++;
                while(k3 < k1 && color[k3] == 0)k3++;
                cb = place[k3];
            } else if(k2 < k1 && k3 >= k1) {
                while(k2 < k1) {
                    co = place[k2];
                    int dis = co > cpo ? co - cpo : cpo - co;
                    total += dis + 1;
                    cpo = co;
                    k2++;
                }
                printf("Case #%d: %d\n", j+1, total);
                break;
            } else if (k3 < k1 && k2 >= k1) {
                while (k3 < k1) {
                    cb = place[k3];
                    int dis = cb > cpb ? cb - cpb : cpb - cb;
                    total += dis + 1;
                    cpb = cb;
                    k3++;
                }
                printf("Case #%d: %d\n", j+1, total);
                break;
            }   
        }
    }
    return 0;
}
