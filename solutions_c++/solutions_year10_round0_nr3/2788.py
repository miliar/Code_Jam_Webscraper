#include <cstdio>
#define MAX_GROUPS 105

int skipSize[MAX_GROUPS];
int bestFromHere[MAX_GROUPS];
FILE* fin = fopen("input.txt", "r");


long long run(void) {
    int iterations=0, carSize=0, n_groups=0;
    int groups[MAX_GROUPS];
    long long euros = 0;

    fscanf(fin, "%d %d %d\n", &iterations, &carSize, &n_groups);
    for (int i=0 ; i<n_groups ; i++) {
        fscanf(fin, "%d", &groups[i]);
    }

    //    printf("%d %d %d\n", iterations, carSize, n_groups);
    for (int startPoint=0 ; startPoint<n_groups ; startPoint++) {
        int places=0, cost=0;
        while (cost + groups[(startPoint + places) % n_groups] <= carSize &&
               places != n_groups) {

            cost += groups[(startPoint + places) % n_groups];
            places++;
        }
        skipSize[startPoint]      = places;
        bestFromHere[startPoint]  = cost;
    }

    int pos = 0;
    for (int i=0 ; i<iterations ; i++) {
        euros += bestFromHere[pos % n_groups];
        pos += skipSize[pos % n_groups];
        //        printf("%d: /%lld\n", i, euros);
    }

    /*
    for (int i=0 ; i<n_groups ; i++) {
        printf("(%d %d)\n", bestFromHere[i], skipSize[i]);
    }
    */
    return euros;
}


int main() {
    FILE* fout = fopen("output.txt", "w");

    int n_cases;
    fscanf(fin, "%d", &n_cases);
    for (int test=1 ; test<=n_cases ; test++) {
        fprintf(fout, "Case #%d: %lld\n", test, run());
    }
}
