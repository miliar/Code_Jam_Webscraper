#include<cstdio>

#define EPS 0.00000001

int C, D;
int P[205];
int V[205];

double left_most;

bool dist(int t, double time) {
    int p = P[t];
    int v = V[t];
    
    for(int i = 0; i < v ; i++){
        if ( (p - left_most) < D ) {
            double dist_to_travel = D - p + left_most;
            if (dist_to_travel > time) return false;
            left_most = p + dist_to_travel;
        }
        else {
            double dist_can_travel = p - left_most - D;
            dist_can_travel = dist_can_travel < time ?dist_can_travel:time;
            left_most = p - dist_can_travel;
        }
    }
    return true;
}

bool possible(double time) {
    left_most = P[0] - D - time - 10;
    for (int i = 0; i < C; i++) {
        if( !dist(i, time) ) return false;
    }
    return true;
}

double search() {
    double low = 0.0;
    double high = 1000000000.0;
    double mid = (high+low)/2;
    
    while ( (high - low) > EPS){
        mid = (high+low)/2;
        if (possible(mid)) {
            //printf("POSSIBLE %f\n", mid);
            high = mid;
        } else {
            low = mid;
        }
    }
    return mid;
}

int main() {

    int T;
    scanf("%d\n", &T);

    for (int tt = 1 ; tt <= T ; tt++) {

        scanf("%d %d\n", &C, &D);
        for(int i = 0 ; i < C ; i++) {
            scanf("%d %d\n", &P[i], &V[i]);
        }
        printf("Case #%d: %.8f\n", tt, search());
    }
    
}
