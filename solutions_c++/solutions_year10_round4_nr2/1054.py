/* 
 * File:   main.cpp
 * Author: sebas
 *
 * Created on 5 de junio de 2010, 10:39 AM
 */

#include <stdlib.h>
#include <cstdio>
#include <cmath>

#define MAX 1024

#define min(X,Y) ((X)<(Y) ? (X) : (Y));

int c[MAX]; // constrait vector; Minimum ammount of games I want to miss
int cost[MAX]; //cost vector
int p;

int solve() {
    int teams = (int)pow(2,p);
    int offset=0, sol=0;
    do {
        teams >>= 1;
        for (int i=0; i<teams; i++) {
            int j = 2*i;
            int nc = min(c[j],c[j+1]);
            if (nc == 0) {
                sol += cost[offset+i];
                c[i] = nc;
            } else {
                c[i] = nc-1;
            }
        }
        offset += teams;
    } while (teams > 1);
    return sol;
}

int main(int argc, char** argv) {
    int T,teams;
    scanf("%i", &T);
    for (int tc=1; tc<=T; tc++) {
        scanf("%i", &p);
        teams = (int)pow(2,p);
        for (int i=0; i<teams; i++) {
            scanf("%i",&(c[i]));
        }
        int offset=0;
        for (int i=0; i<p; i++) {
            teams >>= 1; // /=2
            for (int j=0; j<teams; j++) {
                scanf("%i",&(cost[offset+j]));
            }
            offset += teams;
        }
        printf("Case #%i: %i\n", tc, solve());
    }
    return (EXIT_SUCCESS);
}

