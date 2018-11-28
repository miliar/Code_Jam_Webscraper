#include <cstdio>
#include <cstring>

using namespace std;

int T,C=1;
int n, m, v[10010];
char pal[10010][16];
char lista[32];
int tam[16][10010];
int ntam[16];
int Tam[10010];
int mascara[10010][32];

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d:",C++);
        scanf("%d %d",&n,&m);
        memset(ntam,0,sizeof(ntam));
        for (int i=0;i<n;i++) {
            scanf("%s",pal[i]);
            int t = strlen(pal[i]);
            tam[t][ntam[t]++] = i;
            Tam[i] = t;
            memset(mascara[i],0,sizeof(mascara[i]));
            for (int j=0;j<t;j++) {
                int l = pal[i][j]-'a';
                mascara[i][l] |= (1<<j);
            }

        }

        for (int i=0;i<m;i++) {
            scanf("%s",lista);
            int best = -1, indx;
            //pra cada palavra
            for (int j=0;j<n;j++) {
                //escolhi pal[j]
                //comeca com td mnd do msm tamnho
                int N=0;
                for (int k=0;k<ntam[Tam[j]];k++)
                    v[N++] = tam[Tam[j]][k];
                int lose = 0;
                int u=0;
                while (N > 1 and u<26) {
                    int chute = lista[u++] - 'a';
                    //chuto?
                    bool chuta = false;
                    for (int k=0;k<N;k++) if (mascara[v[k]][chute]!=0) {
                        chuta=true;
                        break;
                    }
                    if (!chuta) continue;
                    //acerto?
                    if (mascara[j][chute]==0) {
                        lose++;
                        //deixa qm nao tem o chute
                        int q=0;
                        for (int k=0;k<N;k++) if (mascara[v[k]][chute]==0)
                            v[q++] = v[k];
                        N=q;
                    } else {
                        //aplica mascara
                        int q = 0;
                        for (int k=0;k<N;k++) if (mascara[v[k]][chute] == mascara[j][chute])
                                v[q++] = v[k];
                        N=q;
                    }
                }
                if (lose > best) {
                    best = lose;
                    indx = j;
                }
            }
            //resp eh pal[indx]
            printf(" %s",pal[indx]);
        }
        printf("\n");
    }

    return 0;
}
