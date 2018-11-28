/* Problema:
 * Fonte:
 * Palavra-chave: */

#include <set>
#include <map>
#include <list>
#include <queue>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <functional>

#define rep(i, N) for(int i=0;i<(N);++i)
#define repd(i, N) for(int i=(N)-1;i>=0;--i)
#define rep3(i, j, N) for(int i=(j);i<(N);++i)
#define repd3(i, j, N) for(int i=(N)-1;i>=(j);--i)

int matriz[50][50];

using namespace std;

int main(void) {
    int T;
    scanf("%d", &T);
    for(int t=0;t<T;++t) {
        int N;
        scanf("%d", &N);
        for(int i=0;i<N;++i) {
            char linha[50];
            scanf("%s", linha);
            for(int j=0;j<N;++j) matriz[i][j] = linha[j] - '0';
        }
        int resp = 0;
        for(int i=0;i<N;++i) {
            for(int j=i;j<N;++j) {
                bool falhou = false;
                for(int k=i+1;k<N;++k) {
                    if(matriz[j][k] == 1) {
                        falhou = true;
                        break;
                    }
                }
                if(not falhou) {
                    int tmp[50];
                    memcpy(tmp, matriz[j], sizeof(int)*N);
                    for(int k = j-1; k>=i;--k) {
                        memcpy(matriz[k+1], matriz[k],sizeof(int)*N);
                    }
                    memcpy(matriz[i], tmp, sizeof(int)*N);
                    resp += j - i;
                    break;
                }
            }
        }
        printf("Case #%d: %d\n", t+1, resp);

    }

    return 0;
}
