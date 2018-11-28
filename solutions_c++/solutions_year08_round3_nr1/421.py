#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <utility>

using namespace std;

int compare(const void *a, const void *b) {
    return (((*(pair<int, int> *)b).first) - ((*(pair<int,int> *)a).first));
}

int main() {

    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int casos;
    scanf("%d", &casos);

    int N, K, L;
    pair<int, int> frequencias[1005];
    //int letrasPorTecla[1005][1005];
    int qtdPorTecla[1005];
    bool marcadosqtdPorTecla[1005];
    int posicoes[1005];


    for (int ifor = 1; ifor <= casos; ifor++) {
        scanf("%d%d%d", &N, &K, &L);

        int temp;
        for (int i = 0; i < L; i++) {
            scanf("%d", &temp);
            frequencias[i] = make_pair(temp, i);
            //qtdPorTecla[i] = 0;
        }

        //memset(marcadosqtdPorTecla, false, sizeof(bool)*K);
        qsort(frequencias, L, sizeof(pair<int, int>), compare);


        for (int i = 0; i < K; i++) {
            //posicoes[frequencias[i].second] = i;
            qtdPorTecla[i] = 0;
        }



        int proximoQtdPorTecla = 0;
        long long int resultado = 0;

        for (int i = 0; i < L; i++) {
            int j = 0;
            while (qtdPorTecla[j] != proximoQtdPorTecla) {
                j++;
            }

            //printf("proximo %d na posicao %d\n", proximoQtdPorTecla, j);

            if (j == K-1) {
                ++proximoQtdPorTecla;
            }

            //letrasPorTecla[j][qtdPorTecla[j]++] = i;
            qtdPorTecla[j]++;
            resultado += qtdPorTecla[j]*frequencias[i].first;
        }

        printf("Case #%d: %lld\n", ifor, resultado);

    }


    return 0;
}
