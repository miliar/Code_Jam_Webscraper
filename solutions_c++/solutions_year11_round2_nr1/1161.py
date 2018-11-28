#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

#define MaxN 110
#define WIN 1
#define LOSS -1
#define NONE 0


int T, N;
char info[MaxN][MaxN];
int win[MaxN], loss[MaxN];
double WP[MaxN], OWP[MaxN], OOWP[MaxN];


int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d\n", &T);
    for (int xxx = 0; xxx < T; xxx++) {
        scanf("%d\n", &N);
        char c;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                scanf("%c", &c);
                if (c == '1')
                    info[i][j] = WIN;
                else if (c == '0') 
                    info[i][j] = LOSS;
                else if (c == '.')
                    info[i][j] = NONE;   
            }
            scanf("\n");
        }
/*        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                printf("%3d", info[i][j]);
            printf("\n");            
        }
        /*
        WP (Winning Percentage) is the fraction of your games that you have won.
    In the example schedule, team A has WP = 1, team B has WP = 0, team C has WP = 2/3, and team D has WP = 0.5.
    OWP (Opponents' Winning Percentage) is the average WP of all your opponents, after first throwing out the games they played against you.
    For example, if you throw out games played against team D, then team B has WP = 0 and team C has WP = 0.5. Therefore team D has OWP = 0.5 * (0 + 0.5) = 0.25. Similarly, team A has OWP = 0.5, team B has OWP = 0.5, and team C has OWP = 2/3.
    OOWP (Opponents' Opponents' Winning Percentage) is the average OWP of all your opponents. OWP is exactly the number computed in the previous step.
    For example, team A has OOWP = 0.5 * (0.5 + 2/3) = 7/12.
        */
        
        for (int i = 0; i < N; i++) {
            win[i] = loss[i] = 0;
            for (int j = 0; j < N; j++)
                if (info[i][j] == WIN)
                    win[i]++;
                else if (info[i][j] == LOSS)
                    loss[i]++;
            WP[i] = (double)(win[i]) / (double)(win[i] + loss[i]);
        }//WP TURIM
        
        for (int i = 0; i < N; i++) {
            double sum = 0;
            for (int j = 0; j < N; j++) if (info[i][j] != NONE) {
                if (info[i][j] == WIN) 
                    sum += (double)(win[j]) / (double)(win[j] + loss[j] - 1);
                else if (info[i][j] == LOSS)
                    sum += (double)(win[j]-1) / (double)(win[j] + loss[j] - 1);
            }
            OWP[i] = sum / (double) (win[i] + loss[i]);
        }
        for (int i = 0; i < N; i++) {
            double sum = 0;
            for (int j = 0; j < N; j++) if (info[i][j] != NONE) {
                sum += OWP[j];
            }
            OOWP[i] = sum / (double) (win[i] + loss[i]);
        }
        printf("Case #%d:\n", xxx + 1);
        for (int i = 0; i < N; i++) 
            printf("%.10lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
    }
    
    
    
    
    return 0;    
}
