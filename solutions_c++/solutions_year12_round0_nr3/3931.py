#include <cstdio>
#include <cstring>

using namespace std;

int T, A, B;
int TS = 0;
int R, L, M;
char foi[2000048];

int main(){
    int i, t, a, n, e;

    memset(foi, 0, sizeof(foi));
    for(scanf("%d", &T); T--;){
        scanf("%d %d", &A, &B);
        TS++;
        R = 0;
        L = 0;
        a = A;
        M = 1;
        while(a){
            L++;
            M *= 10;
            a /= 10;
        }
        M /= 10;

        for(i = A; i <= B; i++){
            if(foi[i] == TS){
                continue;
            }

            t = 1;
            foi[i] = TS;
            a = i;
            for(n = 1; n < L; n++){
                e = a % 10;
                a = a / 10 + e * M;
                if(e && a >= A && a <= B && foi[a] != TS){
                    t++;
                    foi[a] = TS;
                }
            }

            R += (t * (t - 1)) / 2;
        }

        printf("Case #%d: %d\n", TS, R);
    }
    return 0;
}
