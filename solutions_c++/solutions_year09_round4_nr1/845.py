#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int T, n;
char aux[64];
int v[64];

bool jatrokei[64][64];

int ultimo1(char *tt) {
    int resp = -1;
    for (int i=0;i<n;i++)
        if (tt[i] == '1')
            resp = i;
    return resp;
}

bool ok() {
    for (int i=0;i<n;i++)
        if (v[i] > i)
            return false;
    return true;
}

int main() {

    int C = 1;

    scanf("%d",&T);
    while (T--) {
        scanf("%d",&n);
        for (int i=0;i<n;i++) {
            scanf("%s",aux);
            v[i] = ultimo1(aux);
        }
        int mini = 0;
        while (!ok()) {
            for (int i=0;i<n;i++)
                if (v[i] > i) {
                    //axa o 1o numero ok
                    int m = i;
                    for (int j=i+1;j<n;j++)
                        if (v[j] <= i) { m = j; break; }
                    // empurra ele pra cah
                    for (int k=m;k>=i+1;k--) {
                        int aux = v[k];
                        v[k] = v[k-1];
                        v[k-1] = aux;
                        mini++;
                    }
                }
        }
        printf("Case #%d: %d\n",C++,mini);
    }

    return 0;
}
