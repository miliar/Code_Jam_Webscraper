
#include <cstdio>
//#include <stdlib.h>
#include <algorithm>

#define MAX 1500
#define INF 0x3fffffff
//#define min(X,Y) ( ((X)<(Y)) ? (X) : (Y) )

using namespace std;

int N;
int C[MAX];

int main() {
    int tc;
    scanf("%i",&tc);
    for (int i=0; i<tc; i++) {
        scanf("%i", &N);
        for (int j=0; j<N; j++) {
            scanf("%i",&C[j]);
        }
        int nsum=0, sum=0, vmin=INF;
        for (int j=0; j<N; j++) {
            nsum = nsum ^ C[j];
            sum += C[j];
            vmin = min(vmin, C[j]);
        }
        printf("Case #%i: ", i+1);
        if (nsum == 0)
           printf("%i\n", sum-vmin);
        else
            printf("NO\n");
    }
}

        
