#include <cstdio>
#include <cstdlib>

double P[1001] = {0.0,0.0,2.0};
double FAC[1001] = {1};

int main(int argc, char* argv[]) {
    for (int K = 1; K < 1001; K++) FAC[K] = FAC[K-1]/K;
    for (int K = 2; K < 1001; K++) {
        double counter = 0.0;
        P[K] = 1.0;
        for (int i = K; i > 0; i--) {
            counter = FAC[i] - counter;
            P[K] += counter * P[K-i];
        }
        P[K] /= counter;
        //printf("%f\n", P[K]);
    }
    int T;
    scanf("%d", &T);
    int D[1000];
    for (int t = 1; t <= T; t++) {
        double answer = 0.0;
        int K; scanf("%d", &K);
        for (int k = 0; k < K; k++)
          scanf("%d", &D[k]);
        for (int k = 0; k < K; k++) {
          int c = 0;
          for (int k2 = k; D[k2];){
            c++;
            int temp = k2;
            k2 = D[k2]-1;
            D[temp] = 0;}
          answer += P[c];
        }
        printf("Case #%d: %f\n", t, answer);
    }
}
