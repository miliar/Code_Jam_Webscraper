#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

#define MaxN 1010
#define INF 2000000000

int T;
int L, t, N, C;
int a[MaxN];
int dist[MaxN];
int S[MaxN];


int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out","w", stdout);
    scanf("%d", &T);
    for (int xxx = 1; xxx <= T; xxx++) {
        scanf("%d%d%d%d", &L, &t, &N, &C);
        for (int i = 0; i < C; i++)
            scanf("%d", &a[i]);
        int k = 0;
        S[0] = 0;
        for (int i = 0; i <= N; i++) {
            dist[i] = a[k];
            k = (k+1) % C;
            if (i > 0) S[i] = S[i-1] + dist[i-1];
        }
        int ats = INF;
        if (L == 0) {
            ats = S[N] * 2;
        }else if (L == 1) {
            //a[i] - tarp i'tosios ir i+1'osios zvaigzdes
            //S[i] - nuo 0'ines iki itosios zvaigzdes
            for (int i = 0; i < N; i++) {
                //printf("S[%d]=%d, dist[%d] = %d\n", i, S[i], i, dist[i]);
                int tmp;
                if (S[i]*2 >= t) {
                    tmp = 2 * S[N] - dist[i];
                }else {
                    if (S[i+1]*2 <= t) 
                        tmp = 2 * S[N];
                    else {
                        int t1 = 2 * S[i];//per kiek atejom iki sitos
                        int delta = t - t1;//kiek eisime letai
                        tmp = 2 * S[N] - (dist[i]*2 - delta)/2;
                    }
                }
               // printf("TMP (i = %d) = %d\n", i, tmp);
                ats = min(ats, tmp);
            }
           // printf("S[2] = %d\n", S[2]);
        }else if (L == 2) {
            for (int i = 0; i < N - 1; i++) {
                for (int j = i + 1; j < N; j++) {
                    int tims; //laikas ateit iki (i + 1)'o
                    if (S[i]*2 >= t) {
                        tims = 2 * S[i+1] - dist[i];
                    }else {
                        if (S[i+1]*2 <= t)
                            tims = 2 * S[i + 1];
                        else {
                            int t1 = 2 * S[i];
                            int delta = t - t1;
                            tims = 2 * S[i+1] - (dist[i]*2 - delta)/2;
                        }
                    }
                    int tmp;
                    //tims - po tiek laiko esame i + 1 planetoj.
                    if (tims + (S[j] - S[i+1]) * 2 >= t) {
                        tmp = tims + (S[j] - S[i+1])*2 + dist[j] + (S[N] - S[j+1])*2;
                    }else {
                        if (tims + (S[j+1] - S[i+1])* 2 <= t)
                            tmp = tims + (S[N] - S[i+1]) * 2;
                        else {
                            int t1 = tims + (S[j] - S[i+1]) * 2;
                            int delta = t - t1;
                            tmp = tims + (S[j] - S[i+1]) * 2 + (dist[j]*2 - delta)/2 + (S[N] - S[j+1])*2;                            
                        }
                    }
                    ats = min(ats, tmp);
                }                
            }    
        }
        printf("Case #%d: %d\n", xxx, ats);    
    }
    
    
    
    return 0;    
}
