#include <stdio.h>
#include <string.h>

int main(void) {
    char B[1024];
    int N; int k; int j;
    int ANS; int L;
    //                    0123456789012345678
    const char *phrase = "welcome to code jam"; int PL = strlen(phrase);
    FILE *f = fopen("sample.in","r");

    fgets(B,1000,f);
    sscanf(B,"%d",&N);

    int count[20];
    for (k = 0; k < 20; k++) count[k] = 0;
    ANS = 0;
    for (int TEST = 1; TEST <= N; TEST++) {
        for (k = 0; k < 20; k++) count[k] = 0;
        fgets(B,1000,f);
        L = strlen(B);
        for (j = 0; j < L; j++) {
            if (B[j] == 'w') count[0] = (count[0]+1)%10000;
            else{
                for (int z = 1; z < PL; z++) {
                    if (B[j] == phrase[z]) {
                        count[z] += count[z-1];
                        count[z] = count[z]%10000;

                        //for (int f = 0; f < PL; f++) printf("%d;",count[f]);
                        //printf("count[%d] = %d\n",z,count[z]);
                    }
                }
            }
        }

        printf("Case #%d: %04d\n",TEST,count[PL-1]%10000);
    }

    return 0;
}
