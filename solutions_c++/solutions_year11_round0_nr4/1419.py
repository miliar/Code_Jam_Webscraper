
#include <cstdio>
#include <cstdlib>

#define MAX 2000

using namespace std;

int ninst;
int R[MAX];
int S[MAX];

int cmpTo(const void *a, const void *b) {
    return ( *((const int*)a) - *((const int*)b) );
}

int main() {
    int T;
    scanf("%i",&T);
    for (int c=0; c<T; c++) {
        scanf("%i",&ninst);
        for (int i=0; i<ninst; i++) {
            scanf("%i",&R[i]); 
            S[i]=R[i];                      
        }
        qsort(S,ninst,sizeof(int),cmpTo);
        int count=0;
        for (int i=0; i<ninst; i++) {
            if (S[i] != R[i])
                count ++;
        }
        printf("Case #%i: %.6lf\n",c+1, (double)count);
    }
}
