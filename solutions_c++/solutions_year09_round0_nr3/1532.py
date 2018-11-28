#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
using namespace std;

char* welcome = " welcome to code jam";
int N;
char line[501];
int **res;

int main() {
    scanf("%d\n", &N);
    for (int z=1; z<=N; z++) {
        int len = 0;
        while (true) {
              char letter;
              int scan = scanf("%c", &letter);
              if ((scan == EOF) || (letter == 10)) break;
              len++; line[len] = letter;
        }
        res = new int*[len+1];
        for (int i=0; i<=len; i++) res[i] = new int[20];
        res[0][0] = 1;
        for (int i=1; i<=19; i++) res[0][i] = 0;
        for (int i=1; i<=len; i++)
            for (int j=0; j<=19; j++) {
                if ((j>0) && (line[i] == welcome[j])) res[i][j] = res[i-1][j]+res[i-1][j-1];
                else res[i][j] = res[i-1][j];
                res[i][j] = res[i][j] % 10000;
            }
        int result = res[len][19];
        printf("Case #%d: ",z);
        if (result < 1000) printf("0");
        if (result < 100) printf("0");
        if (result < 10) printf("0");
        printf("%d\n", result);             
    }    
}
