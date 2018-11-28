#include <cstdio>
#include <iostream>
using namespace std;

#define MaxN 100

template <typename T>
T mod (T a) {return a > 0 ? a : -a; }

int T, N;

char R[MaxN];
int P[MaxN];



void solve (int t) {
    int ats = 0;
    int lastB = 0, lastO = 0, last = 0; // kelintas laiko vienetas buvo jo mygtukas. last- paskutinis atliktas veiksmas bendrai.
    //ats - dabar kiek laiko
    int whereB = 1, whereO = 1;
    for (int i = 0; i < N; i++) {
        if (R[i] == 'O') {
            if (last > lastO) {
                //paskutinis judejo kitas robotas
                int t = last - lastO;

                int d = mod(P[i] - whereO);
                //printf("t = %d, d = %d\n", t, d);
                if (t >= d)
                    lastO = last + 1;
                else
                    lastO = lastO + d + 1;
            }else {
                lastO = lastO + mod(P[i] - whereO) + 1;
            }
            last = lastO;
            whereO = P[i]; 
        }else {
            if (last > lastB) {
                int t = last-lastB;
                //tiek laiko galim eit link mygtuko
                int d = mod(P[i] - whereB);
                if (t >= d) {
                    lastB = last + 1;    
                }else {
                    lastB = lastB + d + 1;
                }
            }else {
                lastB = lastB + mod(P[i] - whereB) + 1;
            }
            last = lastB;
            whereB = P[i];
        }
      //  printf("DEBUG: lastO : %d whereO : %d, lastB : %d whereB : %d last : %d\n", lastO, whereO, lastB, whereB, last);
    }
    printf("Case #%d: %d\n",t,last);    
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out","w",stdout);
    scanf("%d\n", &T);
    
    for (int i = 0; i < T; i++) {
        scanf("%d ", &N);
        for (int j = 0; j < N; j++) {
            scanf("%c %d", &R[j], &P[j]);
            if (j < N - 1) scanf(" ");
        }
        scanf("\n");
        //for (int j = 0; j < N; j++)
       //     printf("(%c,%d)", R[j], P[j]);
       // printf("\n");
        solve(i+1);
    }
    
    
    
    
    return 0;    
}
