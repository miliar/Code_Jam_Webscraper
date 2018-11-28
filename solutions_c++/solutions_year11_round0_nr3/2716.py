#include <cstdio>

#define MAX_N 20

//#define DEBUG
#ifdef DEBUG
#define D(x...) fprintf(stderr,x)
#else
#define D(x...)
#endif

int T, N;
unsigned int candy[MAX_N];

void handleCase(int num);
int testMask(unsigned int mask);

int main(int argc, char **argv) {
    freopen(argv[1],"r",stdin);

    scanf("%d",&T);

    for(int i=0;i<T;i++) {
        handleCase(i+1);
    }
}

void handleCase(int num) {
    scanf("%d",&N);

    for(int i=0;i<N;i++) {
        scanf("%u",&candy[i]);
    }

    int best = -1;
    for(unsigned int i=1;i<(1<<N)-1;i++) {
        int thisVal = testMask(i);
        D("thisVal = %d\n",thisVal);
        if(best < thisVal) {
            best = thisVal;
        }
    }
    if(best != -1) {
        printf("Case #%d: %d\n",num,best);
    } else {
        printf("Case #%d: NO\n",num);
    }
}

int testMask(unsigned int mask) {
    D("testing mask %u...\n",mask);
    int sum = 0;
    unsigned int sumSean = 0;
    unsigned int sumPat = 0;
    for(int i=0;i<N;i++) {
        if( (1 << i) & mask ) {
            sum += candy[i];
            sumSean ^= candy[i];
        } else {
            sumPat ^= candy[i];
        }
        D("sum = %d, sumSean = %u, sumPat = %u\n",sum,sumSean,sumPat);
    }
    if(sumSean == sumPat) {
        return sum;
    } else {
        return -1;
    }
}
