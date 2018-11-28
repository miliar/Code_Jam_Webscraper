#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int T, n,C=1;
int v[1024];

int main() {

    for(scanf("%d",&T);T--;) {
        scanf("%d",&n);
        int x = 0, soma=0;
        int menor = 0x7fffffff;
        for (int i=0;i<n;i++) {
            scanf("%d",v+i);
            x = x^v[i];
            if (v[i] < menor)
                menor = v[i];
            soma += v[i];
        }
        printf("Case #%d: ",C++);
        if (x!=0)
            printf("NO\n");
        else
            printf("%d\n",soma-menor);
    }

    return 0;
}
