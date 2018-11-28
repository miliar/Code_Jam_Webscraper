#include <cstdio>
#include <cstdlib>

int compare(const void *a, const void *b) {

    return ((*(int *)a)-(*(int *)b));
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int casos;
    scanf("%d", &casos);

    int vetor1[805];
    int vetor2[805];
    int tam;

    for (int ifor = 1; ifor <= casos; ifor++) {
        scanf("%d", &tam);

        for (int i = 0; i < tam; i++) {
            scanf("%d", &vetor1[i]);
        }
        for (int i = 0; i < tam; i++) {
            scanf("%d", &vetor2[i]);
        }

        qsort(vetor1, tam, sizeof(int), compare);
        qsort(vetor2, tam, sizeof(int), compare);

        /*
        for (int i = 0; i < tam; i++) {
            printf("%d ", vetor1[i]);
        }
        printf("\n");
        for (int i = 0; i < tam; i++) {
            printf("%d ", vetor2[i]);
        }
        printf("\n");
        */

        int resultado = 0;
        for (int i = 0; i < tam; i++) {
            resultado += vetor1[i]*vetor2[tam-1-i];
        }

        printf("Case #%d: %d\n", ifor, resultado);
    }

    return 0;
}
