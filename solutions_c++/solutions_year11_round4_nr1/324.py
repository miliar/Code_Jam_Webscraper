#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct walk {
    int speed;
    double length;
    friend bool operator < (walk a, walk b) {
        return a.speed < b.speed;
    }
};

walk walkways[1001];
int runTime;
int n;
int runSpeed;

int main() {
    int T, TT;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        int tLength;
        int walkSpeed;
        
        scanf("%d %d %d %d %d", &tLength, &walkSpeed, &runSpeed, &runTime, &n);
        int i, j;
        int total = 0;
        int b, e;
        for (i = 0; i < n; i++) {
            scanf("%d %d %d", &b, &e, &walkways[i].speed);
            walkways[i].length = e - b;
            total+=e-b;
            walkways[i].speed+=walkSpeed;
        }
        walkways[n].speed = walkSpeed;
        walkways[n].length = tLength - total;
        n++;
        
        sort(walkways, walkways+n);
        
        double timeLeft = runTime;
        double Time = 0;
        for (i = 0; i < n; i++) {
            if (timeLeft + 1e-8 >=  double(walkways[i].length) / (walkways[i].speed + runSpeed - walkSpeed)) {
                walkways[i].speed += runSpeed - walkSpeed;
                timeLeft-=double(walkways[i].length)/walkways[i].speed;
            } else {
                walkways[i].length = (double(walkways[i].length) - timeLeft*(walkways[i].speed + runSpeed - walkSpeed)) / walkways[i].speed + timeLeft;
                walkways[i].speed = 1;
                break;
            }
        }
        
        for (i = 0; i < n; i++) {
            Time += walkways[i].length / walkways[i].speed;
        }
        
        printf("Case #%d: %.8lf\n", T, Time);
        
    }
}
