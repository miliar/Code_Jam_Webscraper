#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

#include <string>
#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <algorithm>

#define INFINITO 0x3f3f3f3f

using namespace std;

#define MAX 512
#define MOD 10000

char linha[MAX];
char welcome[] = "welcome to code jam";
int pd[MAX][MAX];

int main (void) {

    int casos, caso;
    int i, j;

    int ws = strlen(welcome);

    scanf("%d%*c", &casos);
    for (caso=1; caso<=casos; ++caso) {

        gets(linha);

        int size = strlen(linha);

        for (j=0; j<size; ++j) {
            welcome[j] = tolower(welcome[j]);
            pd[0][j] = int(linha[j] == welcome[0]);
        }

        int total;
        for (i=1; i<ws; ++i) {
            total = 0;
            for (j=0; j<size; ++j) {

                if (welcome[i] == linha[j])
                    pd[i][j] = total;
                else
                    pd[i][j] = 0;

                total = ( total + pd[i-1][j] ) % MOD;
            }
        }

        /*
        for (i=0; i<size; ++i) {
            printf(" %c ", linha[i]);
        }
        puts("");
        for (i=0; i<ws; ++i) {
            for (j=0; j<size; ++j) {
                printf("%2d ", pd[i][j]);
            }
            puts("");
        }
        */

        total = 0;
        for (i=0; i<size; ++i) {
            total += pd[ws-1][i];
        }

        printf("Case #%d: %04d\n", caso, total % MOD);
    }

    return 0;
}
