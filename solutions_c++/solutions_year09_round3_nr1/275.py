#include <cstdio>
#include <cstring>

using namespace std;

char str[80];

bool foi[300];
int mapa[300];
int T, C = 1;

int main() {

    scanf("%d",&T);
    while (T--) {
        memset(foi,false,sizeof(foi));
        memset(mapa,0x3f,sizeof(mapa));
        scanf("%s",str);
        mapa[str[0]] = 1;
        foi[str[0]] = true;
        int count = 0;
        int tam = strlen(str);
        for (int i=1;i<tam;i++) {
            if (foi[str[i]]) continue;
            mapa[str[i]] = count++;
            if (count == 1) count++;
            foi[str[i]] = true;
        }
        int base = count == 0 ? 2 : count;
        unsigned long long int resp = 0, pot = 1;
        for (int i=tam-1;i>=0;i--) {
            resp += pot*mapa[str[i]];
            pot *= base;
        }
        printf("Case #%d: %lld\n",C++,resp);
    }

    return 0;
}
