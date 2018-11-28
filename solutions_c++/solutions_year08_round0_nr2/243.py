#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

struct st{
    int time;
    char pos;
    bool arrive;
}train[400];

int num;

bool cmp(st train1, st train2){
    if(train1.time != train2.time) return train1.time < train2.time;
    return train1.arrive;
}

int main(){
    int i, j, n, T, N, NA, NB, h, m, atA, atB, a, b;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &N);
    for (n = 1; n <= N; ++n){
        atA = atB = a = b = num = 0;
        scanf("%d", &T);
        scanf("%d%d", &NA, &NB);
        for (i = 0; i < NA; ++i){
            scanf("%d:%d", &h, &m);
            train[num].time = h * 60 + m;
            train[num].pos = 'A';
            train[num].arrive = false;
            ++num;
            scanf("%d:%d", &h, &m);
            train[num].time = h * 60 + m + T;
            train[num].pos = 'B';
            train[num].arrive = true;
            ++num;
        }
        for (i = 0; i < NB; ++i){
            scanf("%d:%d", &h, &m);
            train[num].time = h * 60 + m;
            train[num].pos = 'B';
            train[num].arrive = false;
            ++num;
            scanf("%d:%d", &h, &m);
            train[num].time = h * 60 + m + T;
            train[num].pos = 'A';
            train[num].arrive = true;
            ++num;
        }
        sort(train, train + (NA + NB) * 2, cmp);
        for (i = 0; i < (NA + NB) * 2; ++i){
            if (train[i].arrive){
                if (train[i].pos == 'A'){
                    ++atA;
                }
                else {
                    ++atB;
                }
            }
            else {
                if (train[i].pos == 'A'){
                    if (atA > 0) --atA;
                    else ++a;
                }
                else {
                    if (atB > 0) --atB;
                    else ++b;
                }
            }
        }
        printf("Case #%d: %d %d\n", n, a, b);
    }
    return 0;
}
