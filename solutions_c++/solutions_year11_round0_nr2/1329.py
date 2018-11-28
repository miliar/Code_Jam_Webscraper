#include <cstdio>
#include <cstring>


using namespace std;

char s[1024];
int T, K,C=1;
char aux[1024];
int v[1024];
int N, n, D;
int comb[32][32];
bool pau[32][32];

int main() {

    for(scanf("%d",&T);T--;) {
        memset(comb,0xff,sizeof(comb));
        memset(pau,false,sizeof(pau));
        scanf("%d",&K);
        for (int i=0;i<K;i++) {
            scanf("%s",aux);
            comb[aux[0]-'A'][aux[1]-'A'] = aux[2]-'A';
            comb[aux[1]-'A'][aux[0]-'A'] = aux[2]-'A';
        }
        scanf("%d",&D);
        for (int i=0;i<D;i++) {
            scanf("%s",aux);
            pau[aux[0]-'A'][aux[1]-'A'] = true;
            pau[aux[1]-'A'][aux[0]-'A'] = true;
        }
        scanf("%d",&n);
        scanf("%s",s);
        N=0;
        for (int i=0;i<n;i++) {
            int c;
            c = s[i]-'A';
            v[N++] = c;
            alioh:
            if (N-2 >= 0 and comb[v[N-1]][v[N-2]] != -1) {
                int nc = comb[v[N-1]][v[N-2]];
                v[N-2] = nc;
                N--;
                c = v[N-1];
                goto alioh;
            }
            for (int i=0;i<N-1;i++)
                if (pau[v[i]][v[N-1]]) {
                    N=0;
                    break;
                }
        }
        printf("Case #%d: [",C++);
        for (int i=0;i<N;i++) {
            if (i) printf(", ");
            printf("%c",v[i]+'A');
        }
        printf("]\n");
    }

    return 0;
}
