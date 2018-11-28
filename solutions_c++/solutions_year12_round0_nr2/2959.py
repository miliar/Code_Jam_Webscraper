#include <iostream>

using namespace std;

#define LARGE

int d[100][4];

int main() {

#ifdef LARGE
    FILE *file = fopen("B-large.txt", "w");
#else
    FILE *file = fopen("B-small.txt", "w");
#endif
    int T; cin >> T;
    for (int t = 0; t < T; t++) {
        int N; cin >> N;
        int S; cin >> S;
        int p; cin >> p;

        int num = 0;

        for (int n = 0; n < N; n++){
            int t; cin >> t;
            int a = t / 3;
            int b = t % 3;
            if (!t) b = 0;

            if (a >= p || (b >= 1 && a + 1 >= p)){
                d[t][4] = 1;
                num++;
                for (int i = 0; i < 3; i++){
                    d[t][i] = a;
                    if (b) {
                        d[t][i] += 1;
                        b--;
                    }
                }
            } else if (S && b >= 2 && a + 2 >= p){
                d[t][4] = 1;
                num++;
                S--;
                d[t][0] = a + 2;
                d[t][1] = a;
                d[t][2] = a;
            } else if (S && (b == 0) && (a + 1 == p) && (a - 1 >= 0)){
                d[t][4] = 1;
                num++;
                S--;
                d[t][0] = a + 1;
                d[t][1] = a;
                d[t][2] = a - 1;
            } else {
                d[t][4] = 0;
                for (int i = 0; i < 3; i++){
                    d[t][i] = a;
                    if (b) {
                        d[t][i] += 1;
                        b--;
                    }
                }
            }
        }

        fprintf(file, "Case #%d: ", t + 1);
        fprintf(file, "%d\n", num);
    }

    fclose(file);

    return 0;
}
