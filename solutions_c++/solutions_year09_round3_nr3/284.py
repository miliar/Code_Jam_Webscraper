#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int rel[128];
bool visited[128];
int ordem[128];
int p, q, T;
bool liberado[128];


int libera (int u) {
    int soma = 0;
    liberado[u] = true;
    for (int i=u-1;i>=0;i--) {
        if (liberado[i]) break;
        soma++;
    }
    for (int i=u+1;i<p;i++) {
        if (liberado[i]) break;
        soma++;
    }


    return soma;
}

int resp(int o) {
    int result = 0x3f3f3f3f, tt;

    if (o == q) {
        memset(liberado,false,sizeof(liberado));
        int soma = 0;
        for (int i=0;i<q;i++) {
            soma += libera(ordem[i]);
        }
        return soma;
    }

    for (int i=0;i<q;i++)
        if (!visited[rel[i]]) {
            visited[rel[i]] = true;
            ordem[o] = rel[i];
            tt = resp(o+1);
            visited[rel[i]] = false;
            result = min(tt,result);
        }
    return result;
}

int main() {

    int C = 1;
    scanf("%d",&T);
    while (T--) {
        scanf("%d %d",&p,&q);
        for (int i=0;i<q;i++) {
            int tt;
            scanf("%d",&tt);
            rel[i] = --tt;
        }
        memset(visited,false,sizeof(visited));
        printf("Case #%d: %d\n",C++,resp(0));
    }

    return 0;
}
