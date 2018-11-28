#include<iostream>
#include<cstdio>
#include<cassert>

using namespace std;

int WIN = 1;
int LOSS = 0;
int NP = -1;

int table [105][105];
int N;

double WP[105];
double OWP[105];
double OOWP[105];

double RPI (int i) {
    //printf("WP = %f OWP = %f OOWP = %f\n", WP[i], OWP[i], OOWP[i]);
    return 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
}

double calc_wp(int i, int excl) {
    int total = 0;
    int win = 0;
    for(int j = 0 ; j < N ; j++) {
        if (table[i][j] == NP) continue;
        if (j == excl) continue;
        
        if (table[i][j] == WIN) win++;
        total++;
    }
    if (total == 0) return  0;
    else return ((double)win)/total;
    assert(false);
}

double calc_owp(int i) {
    int total = 0;
    double wp_ = 0;
    for(int j = 0; j < N; j++) {
        if(table[i][j] == NP) continue;
        wp_ += calc_wp(j, i);
        total++;
    }
    if (total == 0) return 0;

    return wp_/total;
}

double calc_oowp(int i) {
    double x = 0;
    double total = 0;
    for(int j = 0; j < N; j++) {
        if(table[i][j] == NP) continue;
        x += OWP[j];
        total++;
    }
    if(total == 0) return 0;
    return x/total;
}

int main() {
    int T;
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {

        char c;
        scanf("%d\n", &N);

        for (int i = 0 ; i < N ; i++) {
            for (int j = 0 ; j < N ; j++) {
                scanf("%c", &c);
                if (c == '.') table[i][j] = NP;
                else if (c == '1') table[i][j] = WIN;
                else if (c == '0') table[i][j] = LOSS;
                else assert(false);
            }
            scanf("%c", &c);
        }

        for (int i = 0 ; i < N ; i++) {
            WP[i] = calc_wp(i, -1);
            //printf("%f ", WP[i]);
        }

        for (int i = 0 ; i < N ; i++) {
            OWP[i] = calc_owp(i);
            //printf("%f ", OWP[i]);
        }

        for (int i = 0 ; i < N ; i++) {
            OOWP[i] = calc_oowp(i);
            //printf("%f ", OOWP[i]);
        }

        printf("Case #%d:\n", t);
        for (int i = 0 ; i < N ; i++) printf("%.8f\n",RPI(i));
    }
}
